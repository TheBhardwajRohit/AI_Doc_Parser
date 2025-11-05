import sqlite3
from typing import List, Dict, Optional
from dataclasses import dataclass
import json
from datetime import datetime


@dataclass
class DocumentRecord:
    username: str
    original_filename: str
    file_path: str
    ocr_text: str
    document_type: str
    skills: str  # JSON string
    metadata: str  # JSON string
    job_recommendations: str  # JSON string
    timestamp: str
    id: Optional[int] = None


class Database:
    def __init__(self, db_path: str = "documents.db"):
        self.db_path = db_path
        
    def get_connection(self):
        """Get database connection"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def init_db(self):
        """Initialize database with required tables"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS documents (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                original_filename TEXT NOT NULL,
                file_path TEXT NOT NULL,
                ocr_text TEXT,
                document_type TEXT,
                skills TEXT,
                metadata TEXT,
                job_recommendations TEXT,
                timestamp TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Create index for faster queries
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_username ON documents(username)
        """)
        
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_timestamp ON documents(timestamp)
        """)
        
        conn.commit()
        conn.close()
        print("✅ Database initialized")
    
    def insert_document(self, record: DocumentRecord) -> int:
        """Insert a new document record"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO documents (
                username, original_filename, file_path, ocr_text,
                document_type, skills, metadata, job_recommendations, timestamp
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            record.username,
            record.original_filename,
            record.file_path,
            record.ocr_text,
            record.document_type,
            record.skills,
            record.metadata,
            record.job_recommendations,
            record.timestamp
        ))
        
        doc_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return doc_id
    
    def get_all_documents(self, username: Optional[str] = None) -> List[Dict]:
        """Get all documents, optionally filtered by username"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        if username:
            cursor.execute("""
                SELECT id, username, original_filename, document_type, 
                       timestamp, created_at
                FROM documents
                WHERE username = ?
                ORDER BY created_at DESC
            """, (username,))
        else:
            cursor.execute("""
                SELECT id, username, original_filename, document_type, 
                       timestamp, created_at
                FROM documents
                ORDER BY created_at DESC
            """)
        
        rows = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]
    
    def get_document_by_id(self, doc_id: int) -> Optional[Dict]:
        """Get detailed document information by ID"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT * FROM documents WHERE id = ?
        """, (doc_id,))
        
        row = cursor.fetchone()
        conn.close()
        
        if row:
            doc = dict(row)
            # Parse JSON fields
            doc['skills'] = json.loads(doc['skills']) if doc['skills'] else []
            doc['metadata'] = json.loads(doc['metadata']) if doc['metadata'] else {}
            doc['job_recommendations'] = json.loads(doc['job_recommendations']) if doc['job_recommendations'] else []
            return doc
        
        return None
    
    def delete_document(self, doc_id: int) -> bool:
        """Delete a document by ID"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM documents WHERE id = ?", (doc_id,))
        deleted = cursor.rowcount > 0
        
        conn.commit()
        conn.close()
        
        return deleted
    
    def get_total_documents(self) -> int:
        """Get total number of documents"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) as count FROM documents")
        result = cursor.fetchone()
        conn.close()
        
        return result['count'] if result else 0
    
    def get_statistics(self) -> Dict:
        """Get database statistics"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Total documents
        cursor.execute("SELECT COUNT(*) as total FROM documents")
        total = cursor.fetchone()['total']
        
        # Documents by type
        cursor.execute("""
            SELECT document_type, COUNT(*) as count
            FROM documents
            GROUP BY document_type
        """)
        by_type = {row['document_type']: row['count'] for row in cursor.fetchall()}
        
        # Documents by user
        cursor.execute("""
            SELECT username, COUNT(*) as count
            FROM documents
            GROUP BY username
        """)
        by_user = {row['username']: row['count'] for row in cursor.fetchall()}
        
        # Recent activity (last 24 hours)
        cursor.execute("""
            SELECT COUNT(*) as count
            FROM documents
            WHERE datetime(created_at) > datetime('now', '-1 day')
        """)
        recent = cursor.fetchone()['count']
        
        conn.close()
        
        return {
            "total_documents": total,
            "by_document_type": by_type,
            "by_user": by_user,
            "recent_24h": recent
        }
    
    def check_health(self) -> bool:
        """Check if database is accessible"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT 1")
            conn.close()
            return True
        except Exception:
            return False
