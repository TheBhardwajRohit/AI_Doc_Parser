import google.generativeai as genai
import os
from typing import Dict, List
import json
import re


class AIService:
    def __init__(self):
        self.model = None
        self.api_key = os.getenv("GEMINI_API_KEY")
        
        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-pro')
    
    def is_ready(self) -> bool:
        """Check if AI service is configured"""
        return self.model is not None and self.api_key is not None
    
    async def analyze_document(self, ocr_text: str) -> Dict:
        """Analyze document text using Gemini API"""
        if not self.is_ready():
            # Fallback to rule-based analysis if API not configured
            return self._fallback_analysis(ocr_text)
        
        try:
            prompt = self._create_analysis_prompt(ocr_text)
            
            response = self.model.generate_content(prompt)
            
            # Parse the response
            analysis = self._parse_ai_response(response.text)
            
            return analysis
        
        except Exception as e:
            print(f"⚠️ AI analysis error: {str(e)}")
            # Fallback to rule-based analysis
            return self._fallback_analysis(ocr_text)
    
    def _create_analysis_prompt(self, text: str) -> str:
        """Create prompt for Gemini API"""
        return f"""Analyze the following academic document text and provide a structured response in JSON format.

Document Text:
{text}

Please analyze and return ONLY a valid JSON object with the following structure:
{{
    "document_type": "one of: Internship Certificate, Skill Certificate, Course Completion Certificate, Academic Transcript, Degree Certificate, Participation Certificate, Achievement Certificate, Workshop Certificate, Training Certificate, Project Certificate, Research Paper, Thesis, Dissertation, or Other",
    "skills": ["list of technical and soft skills mentioned"],
    "metadata": {{
        "institution": "name of institution/organization",
        "duration": "duration or date range if mentioned",
        "grade_or_score": "grade/score if mentioned",
        "field_of_study": "field or domain",
        "key_achievements": ["list of achievements or highlights"]
    }}
}}

Important:
- Extract ALL technical skills (programming languages, tools, frameworks, technologies)
- Extract soft skills (leadership, communication, teamwork, etc.)
- Be specific and accurate
- Return ONLY the JSON object, no additional text
"""
    
    def _parse_ai_response(self, response_text: str) -> Dict:
        """Parse AI response and extract JSON"""
        try:
            # Try to find JSON in the response
            json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
            
            if json_match:
                json_str = json_match.group(0)
                analysis = json.loads(json_str)
                return analysis
            else:
                # If no JSON found, return default structure
                return self._get_default_analysis()
        
        except json.JSONDecodeError:
            print("⚠️ Could not parse AI response as JSON")
            return self._get_default_analysis()
    
    def _fallback_analysis(self, text: str) -> Dict:
        """Rule-based fallback analysis when AI is not available"""
        text_lower = text.lower()
        
        # Determine document type
        document_type = "Other"
        
        if any(word in text_lower for word in ["internship", "intern"]):
            document_type = "Internship Certificate"
        elif any(word in text_lower for word in ["course completion", "successfully completed"]):
            document_type = "Course Completion Certificate"
        elif any(word in text_lower for word in ["workshop", "seminar"]):
            document_type = "Workshop Certificate"
        elif any(word in text_lower for word in ["training", "trained"]):
            document_type = "Training Certificate"
        elif any(word in text_lower for word in ["participation", "participated"]):
            document_type = "Participation Certificate"
        elif any(word in text_lower for word in ["achievement", "award"]):
            document_type = "Achievement Certificate"
        elif any(word in text_lower for word in ["degree", "bachelor", "master", "diploma"]):
            document_type = "Degree Certificate"
        elif any(word in text_lower for word in ["transcript", "grade"]):
            document_type = "Academic Transcript"
        elif any(word in text_lower for word in ["skill", "proficiency"]):
            document_type = "Skill Certificate"
        
        # Extract skills using keyword matching
        skills = self._extract_skills_keywords(text)
        
        # Extract basic metadata
        metadata = {
            "institution": self._extract_institution(text),
            "duration": "Not specified",
            "grade_or_score": "Not specified",
            "field_of_study": self._extract_field(text),
            "key_achievements": []
        }
        
        return {
            "document_type": document_type,
            "skills": skills,
            "metadata": metadata
        }
    
    def _extract_skills_keywords(self, text: str) -> List[str]:
        """Extract skills using keyword matching"""
        text_lower = text.lower()
        skills = []
        
        # Technical skills keywords
        tech_skills = [
            "python", "java", "javascript", "c++", "c#", "ruby", "php", "swift", "kotlin",
            "react", "angular", "vue", "node.js", "django", "flask", "spring", "express",
            "sql", "mysql", "postgresql", "mongodb", "redis", "elasticsearch",
            "aws", "azure", "gcp", "docker", "kubernetes", "jenkins", "git",
            "machine learning", "deep learning", "ai", "data science", "nlp",
            "html", "css", "typescript", "rest api", "graphql",
            "agile", "scrum", "devops", "ci/cd", "microservices",
            "tensorflow", "pytorch", "scikit-learn", "pandas", "numpy",
            "android", "ios", "flutter", "react native",
            "blockchain", "web3", "solidity", "ethereum"
        ]
        
        # Soft skills keywords
        soft_skills = [
            "leadership", "communication", "teamwork", "problem solving",
            "critical thinking", "time management", "project management",
            "presentation", "collaboration", "analytical", "creative"
        ]
        
        all_skills = tech_skills + soft_skills
        
        for skill in all_skills:
            if skill in text_lower:
                # Capitalize properly
                skills.append(skill.title())
        
        return list(set(skills))  # Remove duplicates
    
    def _extract_institution(self, text: str) -> str:
        """Try to extract institution name"""
        # Look for common patterns
        lines = text.split('\n')
        for line in lines[:5]:  # Check first 5 lines
            if any(word in line.lower() for word in ["university", "college", "institute", "academy", "school"]):
                return line.strip()
        return "Not specified"
    
    def _extract_field(self, text: str) -> str:
        """Extract field of study"""
        text_lower = text.lower()
        
        fields = {
            "Computer Science": ["computer science", "cs", "software", "programming"],
            "Data Science": ["data science", "data analytics", "big data"],
            "Artificial Intelligence": ["artificial intelligence", "ai", "machine learning", "deep learning"],
            "Web Development": ["web development", "frontend", "backend", "full stack"],
            "Mobile Development": ["mobile development", "android", "ios", "app development"],
            "Cybersecurity": ["cybersecurity", "security", "ethical hacking"],
            "Cloud Computing": ["cloud computing", "aws", "azure", "gcp"],
            "Business": ["business", "management", "mba"],
            "Engineering": ["engineering", "mechanical", "electrical", "civil"]
        }
        
        for field, keywords in fields.items():
            if any(keyword in text_lower for keyword in keywords):
                return field
        
        return "General"
    
    def _get_default_analysis(self) -> Dict:
        """Return default analysis structure"""
        return {
            "document_type": "Other",
            "skills": [],
            "metadata": {
                "institution": "Not specified",
                "duration": "Not specified",
                "grade_or_score": "Not specified",
                "field_of_study": "General",
                "key_achievements": []
            }
        }
