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
# Available models (as of October 2025):
# - "gpt-4o" - Latest GPT-4 Optimized (most capable, balanced)
# - "gpt-4o-mini" - Faster, cheaper version
# - "gpt-4-turbo" - Previous generation turbo
# - "gpt-4" - Standard GPT-4
# - "o1-preview" - Advanced reasoning model
# - "o1-mini" - Faster reasoning model

# Current model in use
MODEL = "gpt-4o"  # Using latest GPT-4 Optimized model

# Alternative models (uncomment to switch)
# MODEL = "o1-preview"  # For advanced reasoning tasks
# MODEL = "gpt-4o-mini"  # For faster/cheaper responses
# MODEL = "gpt-4-turbo"  # Previous generation
