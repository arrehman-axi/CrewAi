#!/usr/bin/env python3
"""
Simple test script to verify Gemini API key works directly.
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
model = genai.GenerativeModel('gemini-1.5-flash')

# Test the API
try:
    response = model.generate_content("Write a 3-sentence blogpost about AI in education")
    print("✅ SUCCESS! Gemini API is working!")
    print("📝 Response:")
    print(response.text)
except Exception as e:
    print(f"❌ ERROR: {e}")
