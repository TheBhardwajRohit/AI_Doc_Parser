# Key Code Snippets for PPT Presentation

## 7 Essential code snippets for 5 slides - showcasing the most impressive parts of your AI Document Parser project.

---

## Slide Distribution Strategy:
- **Slide 1:** Snippet #1 (Backend Setup)
- **Slide 2:** Snippets #2 + #3 (Document Pipeline + OCR)
- **Slide 3:** Snippets #4 + #5 (AI Analysis)
- **Slide 4:** Snippet #6 (Job Matching)
- **Slide 5:** Snippet #7 (Frontend Integration)

---

## SLIDE 1: Backend Architecture Setup

### Snippet #1: FastAPI Application with Service Initialization
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Document Parser API")

# Enable cross-origin requests for split deployment
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize all services
db = Database()
ocr_service = OCRService()
ai_service = AIService()
job_matcher = JobMatcher()

@app.on_event("startup")
async def startup_event():
    db.init_db()
    await ocr_service.initialize()
```

**Explanation:** Sets up FastAPI backend with CORS for Windows-Linux communication and initializes all processing services (Database, OCR, AI, Job Matcher).

---

## SLIDE 2: Document Processing Pipeline & OCR

### Snippet #2: 4-Step Processing Pipeline
```python
async def process_document(username: str, file_path: str, original_filename: str):
    # Step 1: OCR - Extract text from document
    ocr_text = await ocr_service.extract_text(file_path)
    
    # Step 2: AI Analysis - Classify document and extract skills
    ai_analysis = await ai_service.analyze_document(ocr_text)
    
    # Step 3: Job Matching - Find relevant opportunities
    job_recommendations = job_matcher.find_matching_jobs(
        ai_analysis.get("skills", [])
    )
    
    # Step 4: Database Storage - Save all results
    doc_id = db.insert_document(doc_record)
    
    return {"status": "success", "document_id": doc_id, "data": ai_analysis}
```

**Explanation:** Core processing pipeline that orchestrates OCR extraction, AI-powered analysis, intelligent job matching, and persistent storage in a sequential async workflow.

---

### Snippet #3: Intelligent PDF Processing (Hybrid Approach)
```python
async def _extract_from_pdf(self, pdf_path: str) -> str:
    pdf_document = fitz.open(pdf_path)
    extracted_text = []
    
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        text = page.get_text()  # Try direct text extraction
        
        if text.strip():
            extracted_text.append(text)  # Text-based PDF
        else:
            # Scanned PDF: Convert to image and apply OCR
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # 2x quality
            img_array = np.frombuffer(pix.samples, dtype=np.uint8)
            results = self.reader.readtext(img_array)
            extracted_text.append('\n'.join([r[1] for r in results]))
    
    return '\n\n'.join(extracted_text)
```

**Explanation:** Hybrid PDF processing that intelligently handles both text-based and scanned PDFs - attempts direct extraction first, then uses OCR for image-based pages.

---

## SLIDE 3: AI-Powered Document Analysis

### Snippet #4: Google Gemini Integration with Fallback
```python
async def analyze_document(self, ocr_text: str) -> Dict:
    if not self.is_ready():
        return self._fallback_analysis(ocr_text)  # Rule-based backup
    
    try:
        # Create structured prompt for AI
        prompt = self._create_analysis_prompt(ocr_text)
        
        # Call Google Gemini AI model
        response = self.model.generate_content(prompt)
        
        # Parse JSON response
        analysis = self._parse_ai_response(response.text)
        return analysis
        
    except Exception as e:
        print(f"AI analysis failed: {e}")
        return self._fallback_analysis(ocr_text)  # Graceful degradation
```

**Explanation:** Leverages Google Gemini AI for intelligent document classification and skill extraction, with automatic fallback to rule-based analysis ensuring 100% uptime.

---

### Snippet #5: Structured Prompt Engineering for AI
```python
def _create_analysis_prompt(self, text: str) -> str:
    return f"""Analyze the following academic document and return ONLY a valid JSON object:

Document Text: {text}

Required JSON Structure:
{{
    "document_type": "Internship Certificate | Skill Certificate | Course Completion...",
    "skills": ["Python", "Machine Learning", "Leadership", "Communication"],
    "metadata": {{
        "institution": "University/Company name",
        "duration": "Date range or duration",
        "grade_or_score": "Grade/Score if mentioned",
        "field_of_study": "Computer Science | Data Science | Engineering...",
        "key_achievements": ["Achievement 1", "Achievement 2"]
    }}
}}

Extract ALL technical skills (languages, frameworks, tools) and soft skills (leadership, teamwork).
"""
```

**Explanation:** Carefully engineered prompt that instructs AI to extract structured information in JSON format, ensuring consistent and parseable responses for downstream processing.

---

## SLIDE 4: Intelligent Job Matching Algorithm

### Snippet #6: Skill-Based Job Recommendation Engine
```python
def find_matching_jobs(self, user_skills: List[str], max_results: int = 5) -> List[Dict]:
    user_skills_lower = [skill.lower() for skill in user_skills]
    job_scores = []
    
    for job in self.job_database:  # 20+ real job postings
        job_skills_lower = [skill.lower() for skill in job["required_skills"]]
        
        # Calculate skill overlap using fuzzy matching
        matches = sum(1 for skill in user_skills_lower 
                     if any(job_skill in skill or skill in job_skill 
                           for job_skill in job_skills_lower))
        
        if matches > 0:
            # Calculate match percentage
            match_percentage = (matches / len(job["required_skills"])) * 100
            job_with_score = job.copy()
            job_with_score["match_score"] = round(match_percentage, 1)
            job_with_score["matching_skills"] = matches
            job_scores.append(job_with_score)
    
    # Sort by match score and return top 5
    job_scores.sort(key=lambda x: (x["match_score"], x["matching_skills"]), reverse=True)
    return job_scores[:max_results]
```

**Explanation:** Intelligent matching algorithm that compares user skills with 20+ job postings, calculates match percentages using fuzzy matching, and returns top 5 most relevant opportunities ranked by relevance.

---

## SLIDE 5: Frontend Integration & Real-time Monitoring

### Snippet #7: React Frontend with Real-time Updates
```typescript
// Parallel API calls for efficiency
const fetchData = async () => {
  const [healthRes, docsRes, statsRes] = await Promise.all([
    axios.get(`${API_URL}/health`),      // Server health status
    axios.get(`${API_URL}/documents`),   // All processed documents
    axios.get(`${API_URL}/stats`)        // System statistics
  ])
  
  setHealth(healthRes.data)
  setDocuments(docsRes.data.documents)
  setStats(statsRes.data.stats)
}

// Auto-refresh dashboard every 30 seconds
useEffect(() => {
  fetchData()  // Initial load
  const interval = setInterval(fetchData, 30000)  // Refresh timer
  return () => clearInterval(interval)  // Cleanup on unmount
}, [])

// File upload handler
const handleUpload = async (files: File[]) => {
  const formData = new FormData()
  formData.append('username', username)
  files.forEach(file => formData.append('files', file))
  
  const response = await axios.post(`${API_URL}/upload`, formData, {
    headers: { 'Content-Type': 'multipart/form-data' }
  })
  
  onUploadComplete(response.data.results)  // Display results
}
```

**Explanation:** React frontend that performs parallel API calls for efficiency, implements auto-refresh for real-time monitoring, and handles multi-file uploads with progress tracking.

---

## Summary: 7 Snippets Across 5 Slides

| Slide | Snippet | Focus | Lines |
|-------|---------|-------|-------|
| **1** | #1 | Backend Setup & Service Initialization | 18 |
| **2** | #2 | Document Processing Pipeline | 14 |
| **2** | #3 | Hybrid PDF Processing | 15 |
| **3** | #4 | AI Analysis with Fallback | 16 |
| **3** | #5 | Structured AI Prompting | 18 |
| **4** | #6 | Job Matching Algorithm | 20 |
| **5** | #7 | Frontend Integration & Real-time Updates | 22 |

**Total:** 7 snippets, ~123 lines of code across 5 slides

---

## Key Technologies Showcased:

**Backend:**
- FastAPI (Python) - High-performance async API
- EasyOCR + OpenCV - OCR text extraction
- Google Gemini AI - Document analysis
- PyMuPDF (fitz) - PDF processing
- SQLite - Database storage

**Frontend:**
- Next.js 14 + React 18 - Modern web framework
- TypeScript - Type-safe development
- Axios - HTTP client
- Tailwind CSS - Styling

**Architecture:**
- 3-Tier Client-Server
- Split Deployment (Windows + Linux)
- RESTful API
- Async processing pipeline

---

## Presentation Strategy:

### Slide 1: Backend Foundation
- Show how FastAPI sets up the server
- Highlight CORS for split deployment
- Emphasize service initialization pattern

### Slide 2: Document Processing
- Display the 4-step pipeline (OCR → AI → Jobs → DB)
- Show hybrid PDF processing intelligence
- Emphasize async/await for performance

### Slide 3: AI Intelligence
- Demonstrate Google Gemini integration
- Show structured prompt engineering
- Highlight fallback mechanism for reliability

### Slide 4: Job Matching
- Explain the matching algorithm
- Show fuzzy skill matching logic
- Demonstrate ranking and scoring

### Slide 5: Frontend Excellence
- Show parallel API calls for speed
- Demonstrate real-time monitoring
- Highlight user experience features

---

## Recommended Slide Structure (Total: 12-15 slides)

1. **Title Slide** - Project name, team, date
2. **Problem Statement** - Why this project matters
3. **Solution Overview** - High-level approach
4. **Architecture Diagram** - Visual system overview
5. **Technology Stack** - All technologies used
6. **CODE SLIDE 1** - Backend Setup (Snippet #1)
7. **CODE SLIDE 2** - Processing Pipeline (Snippets #2, #3)
8. **CODE SLIDE 3** - AI Analysis (Snippets #4, #5)
9. **CODE SLIDE 4** - Job Matching (Snippet #6)
10. **CODE SLIDE 5** - Frontend Integration (Snippet #7)
11. **Demo/Screenshots** - Live demo or UI screenshots
12. **Results & Metrics** - Performance, accuracy, stats
13. **Key Features** - Unique selling points
14. **Future Enhancements** - Scalability, improvements
15. **Conclusion & Q&A** - Summary and questions

---

## Presentation Tips:

1. **Start Strong** - Open with problem statement and architecture diagram
2. **Code Walkthrough** - Explain each snippet line-by-line if needed
3. **Visual Balance** - Mix code slides with diagrams and screenshots
4. **Highlight Innovation:**
   - Hybrid PDF processing (text + OCR)
   - AI with graceful fallback
   - Intelligent fuzzy job matching
   - Real-time monitoring dashboard
5. **Demo Impact** - Live demo or video recording is powerful
6. **Emphasize Scale** - Modular design allows easy expansion
7. **Practice Timing** - 1-2 minutes per code slide

---

## Code Formatting Tips for PPT:

- Use **syntax highlighting** (most PPT tools support this)
- Keep snippets **readable** (14-16pt font minimum)
- Add **comments** in code for clarity
- Use **dark background** with light text for better contrast
- **Highlight key lines** with arrows or different colors
- **Animate code** line-by-line if presenting complex logic
- Include **output examples** or screenshots alongside code

---

## Quick Reference: What Each Snippet Demonstrates

1. **#1** - Professional API setup with middleware and service architecture
2. **#2** - Async pipeline orchestration and workflow management
3. **#3** - Intelligent document handling with adaptive processing
4. **#4** - AI integration with robust error handling
5. **#5** - Advanced prompt engineering for structured AI responses
6. **#6** - Custom algorithm development for business logic
7. **#7** - Modern frontend with real-time capabilities

---

Good luck with your presentation! 🚀
