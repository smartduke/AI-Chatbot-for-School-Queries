#!/usr/bin/env python3
"""
Main entry point for the Smart Academy AI Chatbot application.
This script runs the Streamlit application.

Usage:
    python run_app.py
    
    or
    
    streamlit run src/app.py
"""

import os
import sys

def main():
    """Run the Streamlit application"""
    # Add src directory to Python path
    src_path = os.path.join(os.path.dirname(__file__), 'src')
    if src_path not in sys.path:
        sys.path.insert(0, src_path)
    
    # Run Streamlit
    os.system('streamlit run src/app.py')

if __name__ == "__main__":
    print("🎓 Starting Smart Academy AI Chatbot...")
    print("📍 Press Ctrl+C to stop the server\n")
    main()

