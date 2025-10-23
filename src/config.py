import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# School Configuration
SCHOOL_NAME = "Smart Academy"
SCHOOL_ADDRESS = "123 Education Street, Learning City"
SCHOOL_PHONE = "(555) 123-4567"
SCHOOL_EMAIL = "info@smartacademy.edu"

# Chat Configuration
MAX_TOKENS = 1000
TEMPERATURE = 0.7
MODEL = "gpt-4o-mini"
