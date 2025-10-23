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

# Model Configuration
# Official OpenAI Model Names (October 2025)
# Reference: https://platform.openai.com/docs/quickstart

# Latest Models (GPT-5 Series):
# - "gpt-5" - Latest GPT-5 (most capable, multimodal)
# - "gpt-5-mini" - Smaller, faster GPT-5 (affordable)

# GPT-4 Models:
# - "chatgpt-4o-latest" - Latest GPT-4 Optimized (auto-updates)
# - "gpt-4o" - GPT-4 Optimized (multimodal, 128K context)
# - "gpt-4o-mini" - Smaller, faster GPT-4o

# Reasoning Models (for complex logic):
# - "o1-preview" - Advanced reasoning (128K context)
# - "o1-mini" - Faster reasoning (128K context)

# Legacy Models:
# - "gpt-4-turbo" - Previous generation
# - "gpt-4" - Original GPT-4

# CURRENT MODEL IN USE
MODEL = "gpt-5"  # Latest GPT-5 model (as per OpenAI docs)

# Alternative model options (uncomment to switch):
# MODEL = "gpt-5-mini"          # Faster & cheaper GPT-5
# MODEL = "chatgpt-4o-latest"   # Auto-updates to latest GPT-4
# MODEL = "gpt-4o"              # Stable GPT-4 Optimized
# MODEL = "gpt-4o-mini"         # Faster & cheaper GPT-4
# MODEL = "o1-preview"          # Best for complex reasoning
# MODEL = "o1-mini"             # Faster reasoning
