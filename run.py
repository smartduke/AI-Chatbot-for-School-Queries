#!/usr/bin/env python3
"""
Launcher script for the AI Chatbot for School Queries
"""

import subprocess
import sys
import os

def check_dependencies():
    """Check if required packages are installed"""
    try:
        import streamlit
        import openai
        import dotenv
        import pandas
        print("✅ All dependencies are installed!")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def main():
    """Main launcher function"""
    print("🎓 Starting AI Chatbot for School Queries...")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("app.py"):
        print("❌ Error: app.py not found!")
        print("Please make sure you're in the correct directory.")
        return
    
    # Check dependencies
    if not check_dependencies():
        return
    
    # Check for API key
    if not os.path.exists(".env"):
        print("⚠️  Warning: .env file not found!")
        print("You can set your OpenAI API key in the app's sidebar.")
        print("Or create a .env file with: OPENAI_API_KEY=your_key_here")
        print()
    
    print("🚀 Launching Streamlit app...")
    print("The app will open in your default browser.")
    print("Press Ctrl+C to stop the server.")
    print("=" * 50)
    
    try:
        # Run the Streamlit app
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"], check=True)
    except KeyboardInterrupt:
        print("\n👋 Goodbye! Thanks for using the AI Chatbot!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running the app: {e}")
        print("Try running: streamlit run app.py")

if __name__ == "__main__":
    main()
