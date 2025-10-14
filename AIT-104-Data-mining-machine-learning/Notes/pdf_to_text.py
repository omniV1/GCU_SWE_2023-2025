#!/usr/bin/env python3
"""
Simple PDF to text converter
Usage: python pdf_to_text.py input.pdf output.txt
"""

import sys
from pypdf import PdfReader

def pdf_to_text(pdf_path, txt_path):
    """Convert PDF to text file"""
    try:
        reader = PdfReader(pdf_path)
        text = ""
        
        print(f"Processing {len(reader.pages)} pages...")
        
        for i, page in enumerate(reader.pages):
            text += f"\n--- Page {i+1} ---\n"
            text += page.extract_text()
            text += "\n"
        
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(text)
        
        print(f"Successfully converted to {txt_path}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pdf_to_text.py input.pdf output.txt")
        sys.exit(1)
    
    pdf_to_text(sys.argv[1], sys.argv[2])
