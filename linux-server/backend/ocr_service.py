import easyocr
from typing import Optional
import cv2
import numpy as np
from pathlib import Path
import fitz  # PyMuPDF for PDF handling


class OCRService:
    def __init__(self):
        self.reader = None
        self.is_initialized = False
    
    async def initialize(self):
        """Initialize EasyOCR reader (lazy loading)"""
        if not self.is_initialized:
            print("🔄 Initializing EasyOCR (this may take a moment)...")
            # Initialize with English language
            self.reader = easyocr.Reader(['en'], gpu=False)
            self.is_initialized = True
            print("✅ EasyOCR initialized")
    
    def is_ready(self) -> bool:
        """Check if OCR service is ready"""
        return self.is_initialized and self.reader is not None
    
    async def extract_text(self, file_path: str) -> str:
        """Extract text from image or PDF file"""
        if not self.is_ready():
            await self.initialize()
        
        file_path = Path(file_path)
        
        if file_path.suffix.lower() == '.pdf':
            return await self._extract_from_pdf(str(file_path))
        else:
            return await self._extract_from_image(str(file_path))
    
    async def _extract_from_image(self, image_path: str) -> str:
        """Extract text from image file"""
        try:
            # Read image
            image = cv2.imread(image_path)
            
            if image is None:
                raise ValueError(f"Could not read image: {image_path}")
            
            # Perform OCR
            results = self.reader.readtext(image)
            
            # Extract text from results
            text_lines = [result[1] for result in results]
            extracted_text = '\n'.join(text_lines)
            
            return extracted_text
        
        except Exception as e:
            print(f"❌ Error in OCR extraction: {str(e)}")
            raise
    
    async def _extract_from_pdf(self, pdf_path: str) -> str:
        """Extract text from PDF file"""
        try:
            extracted_text = []
            
            # Open PDF
            pdf_document = fitz.open(pdf_path)
            
            for page_num in range(len(pdf_document)):
                page = pdf_document[page_num]
                
                # Try text extraction first (for text-based PDFs)
                text = page.get_text()
                
                if text.strip():
                    extracted_text.append(text)
                else:
                    # If no text, convert page to image and use OCR
                    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # 2x zoom for better quality
                    img_array = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
                    
                    # Convert to RGB if needed
                    if pix.n == 4:  # RGBA
                        img_array = cv2.cvtColor(img_array, cv2.COLOR_RGBA2RGB)
                    
                    # Perform OCR on image
                    results = self.reader.readtext(img_array)
                    text_lines = [result[1] for result in results]
                    extracted_text.append('\n'.join(text_lines))
            
            pdf_document.close()
            
            return '\n\n'.join(extracted_text)
        
        except Exception as e:
            print(f"❌ Error in PDF extraction: {str(e)}")
            raise
    
    def preprocess_image(self, image: np.ndarray) -> np.ndarray:
        """Preprocess image for better OCR results"""
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Apply thresholding
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        # Denoise
        denoised = cv2.fastNlMeansDenoising(thresh)
        
        return denoised
