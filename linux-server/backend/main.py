from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import List, Optional
import os
import shutil
from datetime import datetime
import json
import asyncio
from pathlib import Path

from database import Database, DocumentRecord
from ocr_service import OCRService
from ai_service import AIService
from job_matcher import JobMatcher

app = FastAPI(title="AI Document Parser API")

# CORS middleware for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
db = Database()
ocr_service = OCRService()
ai_service = AIService()
job_matcher = JobMatcher()

# Create uploads directory
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@app.on_event("startup")
async def startup_event():
    """Initialize services on startup"""
    db.init_db()
    await ocr_service.initialize()
    print("✅ Server started successfully")


@app.get("/")
async def root():
    return {"message": "AI Document Parser API", "status": "running"}


@app.get("/health")
async def health_check():
    """Server health check endpoint"""
    try:
        # Check database
        db_status = db.check_health()
        
        # Check OCR service
        ocr_status = ocr_service.is_ready()
        
        # Check AI service
        ai_status = ai_service.is_ready()
        
        # Get system stats
        total_docs = db.get_total_documents()
        
        return {
            "status": "healthy" if all([db_status, ocr_status, ai_status]) else "degraded",
            "timestamp": datetime.now().isoformat(),
            "services": {
                "database": "online" if db_status else "offline",
                "ocr": "online" if ocr_status else "offline",
                "ai": "online" if ai_status else "offline"
            },
            "stats": {
                "total_documents_processed": total_docs,
                "uptime": "running"
            }
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }


@app.post("/upload")
async def upload_documents(
    username: str = Form(...),
    files: List[UploadFile] = File(...)
):
    """Upload and process multiple documents"""
    results = []
    
    for file in files:
        try:
            # Validate file type
            if not file.filename.lower().endswith(('.pdf', '.jpg', '.jpeg', '.png')):
                results.append({
                    "filename": file.filename,
                    "status": "error",
                    "error": "Invalid file type. Only PDF, JPG, PNG allowed."
                })
                continue
            
            # Create user directory
            user_dir = UPLOAD_DIR / username
            user_dir.mkdir(exist_ok=True)
            
            # Save file with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_ext = Path(file.filename).suffix
            safe_filename = f"{timestamp}_{file.filename}"
            file_path = user_dir / safe_filename
            
            # Save uploaded file
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            
            # Process document
            result = await process_document(username, str(file_path), file.filename)
            results.append(result)
            
        except Exception as e:
            results.append({
                "filename": file.filename,
                "status": "error",
                "error": str(e)
            })
    
    return {"results": results}


async def process_document(username: str, file_path: str, original_filename: str):
    """Process a single document through OCR and AI analysis"""
    try:
        # Step 1: OCR - Extract text
        print(f"🔍 Processing OCR for {original_filename}...")
        ocr_text = await ocr_service.extract_text(file_path)
        
        if not ocr_text or len(ocr_text.strip()) < 10:
            return {
                "filename": original_filename,
                "status": "error",
                "error": "Could not extract sufficient text from document"
            }
        
        # Step 2: AI Analysis - Categorize and extract skills
        print(f"🤖 Analyzing document with AI...")
        ai_analysis = await ai_service.analyze_document(ocr_text)
        
        # Step 3: Job Matching
        print(f"💼 Finding relevant jobs...")
        job_recommendations = job_matcher.find_matching_jobs(ai_analysis.get("skills", []))
        
        # Step 4: Save to database
        doc_record = DocumentRecord(
            username=username,
            original_filename=original_filename,
            file_path=file_path,
            ocr_text=ocr_text,
            document_type=ai_analysis.get("document_type", "Unknown"),
            skills=json.dumps(ai_analysis.get("skills", [])),
            metadata=json.dumps(ai_analysis.get("metadata", {})),
            job_recommendations=json.dumps(job_recommendations),
            timestamp=datetime.now().isoformat()
        )
        
        doc_id = db.insert_document(doc_record)
        
        return {
            "filename": original_filename,
            "status": "success",
            "document_id": doc_id,
            "data": {
                "document_type": ai_analysis.get("document_type"),
                "skills": ai_analysis.get("skills", []),
                "metadata": ai_analysis.get("metadata", {}),
                "job_recommendations": job_recommendations,
                "ocr_preview": ocr_text[:500] + "..." if len(ocr_text) > 500 else ocr_text
            }
        }
        
    except Exception as e:
        print(f"❌ Error processing document: {str(e)}")
        return {
            "filename": original_filename,
            "status": "error",
            "error": str(e)
        }


@app.get("/documents")
async def get_all_documents(username: Optional[str] = None):
    """Get all processed documents, optionally filtered by username"""
    try:
        documents = db.get_all_documents(username)
        return {
            "status": "success",
            "count": len(documents),
            "documents": documents
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/documents/{document_id}")
async def get_document(document_id: int):
    """Get detailed information about a specific document"""
    try:
        document = db.get_document_by_id(document_id)
        if not document:
            raise HTTPException(status_code=404, detail="Document not found")
        return {
            "status": "success",
            "document": document
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/documents/{document_id}")
async def delete_document(document_id: int):
    """Delete a document and its associated file"""
    try:
        # Get document info
        document = db.get_document_by_id(document_id)
        if not document:
            raise HTTPException(status_code=404, detail="Document not found")
        
        # Delete file from filesystem
        file_path = Path(document["file_path"])
        if file_path.exists():
            file_path.unlink()
        
        # Delete from database
        db.delete_document(document_id)
        
        return {
            "status": "success",
            "message": f"Document {document_id} deleted successfully"
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/stats")
async def get_statistics():
    """Get server statistics"""
    try:
        stats = db.get_statistics()
        return {
            "status": "success",
            "stats": stats
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
