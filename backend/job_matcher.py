from typing import List, Dict
import random


class JobMatcher:
    def __init__(self):
        # Mock job database with realistic job postings
        self.job_database = [
            {
                "id": 1,
                "title": "Full Stack Developer",
                "company": "TechCorp Solutions",
                "location": "Bangalore, India",
                "type": "Full-time",
                "experience": "2-4 years",
                "salary": "₹8-12 LPA",
                "required_skills": ["Python", "React", "Node.js", "MongoDB", "REST API"],
                "description": "Looking for a full stack developer to build scalable web applications.",
                "posted_date": "2 days ago"
            },
            {
                "id": 2,
                "title": "Data Scientist",
                "company": "DataMinds Analytics",
                "location": "Hyderabad, India",
                "type": "Full-time",
                "experience": "1-3 years",
                "salary": "₹10-15 LPA",
                "required_skills": ["Python", "Machine Learning", "Pandas", "Scikit-Learn", "SQL"],
                "description": "Join our team to work on cutting-edge ML projects and data analysis.",
                "posted_date": "1 week ago"
            },
            {
                "id": 3,
                "title": "Frontend Developer",
                "company": "WebWorks India",
                "location": "Pune, India",
                "type": "Full-time",
                "experience": "1-2 years",
                "salary": "₹6-9 LPA",
                "required_skills": ["React", "JavaScript", "HTML", "CSS", "TypeScript"],
                "description": "Create beautiful and responsive user interfaces for our clients.",
                "posted_date": "3 days ago"
            },
            {
                "id": 4,
                "title": "Backend Developer",
                "company": "CloudTech Systems",
                "location": "Mumbai, India",
                "type": "Full-time",
                "experience": "2-5 years",
                "salary": "₹9-14 LPA",
                "required_skills": ["Java", "Spring", "MySQL", "REST API", "Microservices"],
                "description": "Build robust backend systems and APIs for enterprise applications.",
                "posted_date": "5 days ago"
            },
            {
                "id": 5,
                "title": "Machine Learning Engineer",
                "company": "AI Innovations Lab",
                "location": "Bangalore, India",
                "type": "Full-time",
                "experience": "2-4 years",
                "salary": "₹12-18 LPA",
                "required_skills": ["Python", "TensorFlow", "PyTorch", "Deep Learning", "NLP"],
                "description": "Work on state-of-the-art AI models and deploy them at scale.",
                "posted_date": "1 day ago"
            },
            {
                "id": 6,
                "title": "DevOps Engineer",
                "company": "InfraCloud Technologies",
                "location": "Remote",
                "type": "Full-time",
                "experience": "2-4 years",
                "salary": "₹10-16 LPA",
                "required_skills": ["Docker", "Kubernetes", "AWS", "Jenkins", "CI/CD"],
                "description": "Manage cloud infrastructure and automate deployment pipelines.",
                "posted_date": "4 days ago"
            },
            {
                "id": 7,
                "title": "Mobile App Developer",
                "company": "AppGenius Studio",
                "location": "Delhi NCR, India",
                "type": "Full-time",
                "experience": "1-3 years",
                "salary": "₹7-11 LPA",
                "required_skills": ["React Native", "Flutter", "Android", "iOS", "JavaScript"],
                "description": "Develop cross-platform mobile applications for diverse clients.",
                "posted_date": "1 week ago"
            },
            {
                "id": 8,
                "title": "Data Analyst",
                "company": "Business Intelligence Corp",
                "location": "Chennai, India",
                "type": "Full-time",
                "experience": "0-2 years",
                "salary": "₹5-8 LPA",
                "required_skills": ["SQL", "Python", "Data Science", "Excel", "Tableau"],
                "description": "Analyze business data and create insightful reports and dashboards.",
                "posted_date": "2 days ago"
            },
            {
                "id": 9,
                "title": "Cloud Solutions Architect",
                "company": "CloudFirst Consulting",
                "location": "Bangalore, India",
                "type": "Full-time",
                "experience": "4-6 years",
                "salary": "₹15-22 LPA",
                "required_skills": ["AWS", "Azure", "GCP", "Cloud Computing", "Microservices"],
                "description": "Design and implement cloud-native solutions for enterprise clients.",
                "posted_date": "3 days ago"
            },
            {
                "id": 10,
                "title": "Python Developer",
                "company": "CodeCraft Solutions",
                "location": "Hyderabad, India",
                "type": "Full-time",
                "experience": "1-3 years",
                "salary": "₹6-10 LPA",
                "required_skills": ["Python", "Django", "Flask", "PostgreSQL", "REST API"],
                "description": "Develop backend services and APIs using Python frameworks.",
                "posted_date": "6 days ago"
            },
            {
                "id": 11,
                "title": "UI/UX Designer",
                "company": "DesignHub Creative",
                "location": "Pune, India",
                "type": "Full-time",
                "experience": "2-4 years",
                "salary": "₹7-12 LPA",
                "required_skills": ["Figma", "Adobe XD", "Prototyping", "User Research", "Design"],
                "description": "Create intuitive and beautiful user experiences for digital products.",
                "posted_date": "4 days ago"
            },
            {
                "id": 12,
                "title": "Cybersecurity Analyst",
                "company": "SecureNet Technologies",
                "location": "Mumbai, India",
                "type": "Full-time",
                "experience": "2-5 years",
                "salary": "₹9-15 LPA",
                "required_skills": ["Cybersecurity", "Network Security", "Penetration Testing", "Security"],
                "description": "Protect our systems and data from security threats and vulnerabilities.",
                "posted_date": "1 week ago"
            },
            {
                "id": 13,
                "title": "Software Engineer Intern",
                "company": "StartupHub India",
                "location": "Bangalore, India",
                "type": "Internship",
                "experience": "0-1 years",
                "salary": "₹15,000-25,000/month",
                "required_skills": ["Python", "JavaScript", "Git", "Problem Solving"],
                "description": "Learn and grow with our dynamic startup team. Fresh graduates welcome!",
                "posted_date": "2 days ago"
            },
            {
                "id": 14,
                "title": "Blockchain Developer",
                "company": "CryptoTech Ventures",
                "location": "Remote",
                "type": "Full-time",
                "experience": "2-4 years",
                "salary": "₹12-20 LPA",
                "required_skills": ["Blockchain", "Solidity", "Ethereum", "Web3", "Smart Contracts"],
                "description": "Build decentralized applications and smart contracts on blockchain.",
                "posted_date": "5 days ago"
            },
            {
                "id": 15,
                "title": "QA Automation Engineer",
                "company": "TestPro Solutions",
                "location": "Chennai, India",
                "type": "Full-time",
                "experience": "2-4 years",
                "salary": "₹7-11 LPA",
                "required_skills": ["Selenium", "Python", "Java", "Testing", "Automation"],
                "description": "Automate testing processes and ensure software quality.",
                "posted_date": "3 days ago"
            },
            {
                "id": 16,
                "title": "AI Research Scientist",
                "company": "DeepMind Research Lab",
                "location": "Bangalore, India",
                "type": "Full-time",
                "experience": "3-6 years",
                "salary": "₹18-28 LPA",
                "required_skills": ["Deep Learning", "AI", "Research", "Python", "TensorFlow"],
                "description": "Conduct cutting-edge research in artificial intelligence and publish papers.",
                "posted_date": "1 week ago"
            },
            {
                "id": 17,
                "title": "Project Manager - IT",
                "company": "GlobalTech Enterprises",
                "location": "Mumbai, India",
                "type": "Full-time",
                "experience": "5-8 years",
                "salary": "₹15-25 LPA",
                "required_skills": ["Project Management", "Agile", "Scrum", "Leadership", "Communication"],
                "description": "Lead and manage IT projects from conception to delivery.",
                "posted_date": "4 days ago"
            },
            {
                "id": 18,
                "title": "React Native Developer",
                "company": "MobileFirst Apps",
                "location": "Hyderabad, India",
                "type": "Full-time",
                "experience": "1-3 years",
                "salary": "₹7-12 LPA",
                "required_skills": ["React Native", "JavaScript", "Mobile Development", "React", "Redux"],
                "description": "Build high-performance mobile apps using React Native framework.",
                "posted_date": "2 days ago"
            },
            {
                "id": 19,
                "title": "Database Administrator",
                "company": "DataSafe Systems",
                "location": "Pune, India",
                "type": "Full-time",
                "experience": "3-5 years",
                "salary": "₹9-14 LPA",
                "required_skills": ["SQL", "MySQL", "PostgreSQL", "Database", "Performance Tuning"],
                "description": "Manage and optimize database systems for high availability and performance.",
                "posted_date": "6 days ago"
            },
            {
                "id": 20,
                "title": "Technical Content Writer",
                "company": "TechDocs Media",
                "location": "Remote",
                "type": "Full-time",
                "experience": "1-3 years",
                "salary": "₹5-8 LPA",
                "required_skills": ["Technical Writing", "Documentation", "Communication", "Research"],
                "description": "Create technical documentation, tutorials, and blog posts for developers.",
                "posted_date": "5 days ago"
            }
        ]
    
    def find_matching_jobs(self, user_skills: List[str], max_results: int = 5) -> List[Dict]:
        """Find jobs matching user skills"""
        if not user_skills:
            # Return random jobs if no skills provided
            return random.sample(self.job_database, min(max_results, len(self.job_database)))
        
        # Normalize skills for comparison
        user_skills_lower = [skill.lower() for skill in user_skills]
        
        # Calculate match scores for each job
        job_scores = []
        for job in self.job_database:
            job_skills_lower = [skill.lower() for skill in job["required_skills"]]
            
            # Count matching skills
            matches = sum(1 for skill in user_skills_lower if any(job_skill in skill or skill in job_skill for job_skill in job_skills_lower))
            
            if matches > 0:
                match_percentage = (matches / len(job["required_skills"])) * 100
                job_with_score = job.copy()
                job_with_score["match_score"] = round(match_percentage, 1)
                job_with_score["matching_skills"] = matches
                job_scores.append(job_with_score)
        
        # Sort by match score
        job_scores.sort(key=lambda x: (x["match_score"], x["matching_skills"]), reverse=True)
        
        # Return top matches
        top_matches = job_scores[:max_results]
        
        # If not enough matches, add some random jobs
        if len(top_matches) < max_results:
            remaining = max_results - len(top_matches)
            matched_ids = {job["id"] for job in top_matches}
            other_jobs = [job for job in self.job_database if job["id"] not in matched_ids]
            additional = random.sample(other_jobs, min(remaining, len(other_jobs)))
            
            for job in additional:
                job_copy = job.copy()
                job_copy["match_score"] = 0
                job_copy["matching_skills"] = 0
                top_matches.append(job_copy)
        
        return top_matches
