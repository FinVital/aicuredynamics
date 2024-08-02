import fitz  # PyMuPDF
import pytesseract
import cv2
from pytesseract import Output
import openai
import numpy as np
import os

# Set OpenAI API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

def extract_text_from_image(image_file):
    """Extract text from an image using OCR."""
    try:
        # Read the uploaded image file
        file_bytes = np.asarray(bytearray(image_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        
        # Convert image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Apply thresholding
        _, thresh_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)
        
        # Configure Tesseract
        custom_config = r'--oem 3 --psm 6'
        
        # Extract text using Tesseract
        details = pytesseract.image_to_data(thresh_image, output_type=Output.DICT, config=custom_config)
        extracted_text = ""
        n_boxes = len(details['text'])
        
        # Collect text from detected boxes
        for i in range(n_boxes):
            if int(details['conf'][i]) > 50:
                extracted_text += details['text'][i] + " "
        
        return extracted_text.strip()
    except Exception as e:
        print(f"Error extracting text from image: {e}")
        return "Error extracting text from image."

def extract_text_from_pdf(pdf_file):
    """Extract text from a PDF file."""
    try:
        document = fitz.open(stream=pdf_file.read(), filetype="pdf")
        text = ""
        for page_num in range(len(document)):
            page_text = document[page_num].get_text()
            text += page_text
        return text.strip()
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return "Error extracting text from PDF."

def analyze_genomic_data(text):
    """Simulate ultra-fast genomic analysis using GPT-3.5-turbo."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that provides ultra-fast genomic analysis using deep learning to identify biomarkers linked to specific diseases."},
                {"role": "user", "content": f"Analyze this genomic data: {text}"}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error analyzing genomic data: {e}")
        return "Error analyzing genomic data."

def predict_disease(text):
    """Enhance disease prediction accuracy using GPT-3.5-turbo."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that uses deep learning to provide hyper-accurate disease predictions for early intervention."},
                {"role": "user", "content": f"Provide disease predictions based on this data: {text}"}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error predicting disease: {e}")
        return "Error predicting disease."

def map_biomarkers_dynamically(text):
    """Create dynamic biomarker maps for personalized treatment."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that creates dynamic biomarker maps to provide real-time insights for continuous personalized treatment."},
                {"role": "user", "content": f"Map biomarkers dynamically based on this data: {text}"}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error mapping biomarkers: {e}")
        return "Error mapping biomarkers."

# Additional helper functions can be added here if needed.
