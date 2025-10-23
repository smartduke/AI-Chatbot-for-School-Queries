# 📁 Project Structure Documentation

## Overview

This document provides a detailed explanation of the project's file and folder organization.

## Directory Tree

```
AI-Chatbot-for-School-Queries/
│
├── 📂 src/                         # Source Code
│   ├── __init__.py                # Package initializer
│   ├── app.py                     # Main application (500+ lines)
│   ├── config.py                  # Configuration settings
│   ├── school_data.py             # School information data
│   └── run.py                     # Internal launcher script
│
├── 📂 docs/                        # Documentation
│   ├── SETUP.md                   # Quick setup guide
│   ├── CONTRIBUTING.md            # Contribution guidelines
│   ├── GITHUB_UPLOAD_GUIDE.md     # GitHub upload instructions
│   └── PROJECT_STRUCTURE.md       # This file
│
├── 📂 guides/                      # Learning Materials
│   ├── COMPLETE_LEARNING_GUIDE.md # 20-chapter tutorial
│   ├── COMPLETE_LEARNING_GUIDE.pdf# PDF version of guide
│   ├── QUICK_REFERENCE.md         # One-page reference
│   └── BLOG_ARTICLE.md            # Marketing content
│
├── 📂 assets/                      # Static Assets
│   └── (screenshots, logos, etc.)
│
├── 📄 run_app.py                  # Main entry point
├── 📄 requirements.txt            # Dependencies
├── 📄 README.md                   # Project overview
├── 📄 LICENSE                     # MIT License
├── 📄 .env                        # Environment variables (not in repo)
├── 📄 .gitignore                  # Git ignore patterns
├── 📄 chat_history.pkl            # Chat history (auto-generated)
│
└── 📂 venv/                       # Virtual environment (optional)
```

---

## 📂 Source Code (`/src/`)

The `src/` directory contains all the Python source code for the application.

### `__init__.py`
- **Purpose**: Python package initializer
- **Content**: Package metadata (version, author)
- **Size**: ~7 lines
- **Dependencies**: None

### `app.py`
- **Purpose**: Main Streamlit application
- **Content**:
  - UI components and styling
  - Chat interface logic
  - OpenAI API integration
  - Session state management
  - Chat history persistence
  - Search and filter functionality
- **Size**: ~500+ lines
- **Key Functions**:
  - `get_openai_response()`: API communication
  - `display_chat_message()`: Message rendering
  - `save_chat_history()`: Persistence
  - `load_chat_history()`: History restoration
  - `search_messages()`: Search functionality
  - `validate_api_key()`: API key validation
- **Dependencies**: 
  - streamlit
  - openai
  - config
  - school_data
  - pickle
  - datetime
  - httpx

### `config.py`
- **Purpose**: Centralized configuration
- **Content**:
  - OpenAI API settings
  - School information
  - Model parameters
  - Environment variable loading
- **Size**: ~20 lines
- **Configuration Items**:
  - `OPENAI_API_KEY`: API authentication
  - `SCHOOL_NAME`: Institution name
  - `SCHOOL_ADDRESS`: Physical address
  - `SCHOOL_PHONE`: Contact number
  - `SCHOOL_EMAIL`: Email address
  - `MODEL`: AI model name
  - `TEMPERATURE`: Response creativity
  - `MAX_TOKENS`: Response length
- **Dependencies**: 
  - python-dotenv
  - os

### `school_data.py`
- **Purpose**: School information database
- **Content**:
  - Weekly class schedules
  - Upcoming events
  - Homework assignments
  - School policies
  - Contact information
- **Size**: ~150 lines
- **Data Structures**:
  - `SCHOOL_SCHEDULE`: Dict of daily schedules
  - `UPCOMING_EVENTS`: List of event dictionaries
  - `HOMEWORK_ASSIGNMENTS`: List of assignment dictionaries
  - `SCHOOL_POLICIES`: List of policy dictionaries
  - `CONTACT_INFO`: List of staff contacts
- **Dependencies**: None

### `run.py`
- **Purpose**: Internal launcher with dependency checks
- **Content**:
  - Dependency verification
  - Environment checks
  - Streamlit process launcher
- **Size**: ~60 lines
- **Dependencies**: 
  - subprocess
  - sys
  - os

---

## 📂 Documentation (`/docs/`)

The `docs/` directory contains technical documentation and guides.

### `SETUP.md`
- **Purpose**: Quick start installation guide
- **Content**:
  - Step-by-step setup instructions
  - Common issues and solutions
  - Environment configuration
  - First-time setup tips
- **Size**: ~120 lines
- **Audience**: New users, developers

### `CONTRIBUTING.md`
- **Purpose**: Contribution guidelines
- **Content**:
  - How to contribute
  - Code standards
  - Pull request process
  - Issue reporting
  - Development workflow
- **Size**: ~80 lines
- **Audience**: Contributors, developers

### `GITHUB_UPLOAD_GUIDE.md`
- **Purpose**: GitHub repository setup
- **Content**:
  - Git initialization
  - Repository creation
  - Push instructions
  - Best practices
- **Size**: ~300 lines
- **Audience**: Project maintainers

### `PROJECT_STRUCTURE.md`
- **Purpose**: Project organization documentation
- **Content**: This file!
- **Audience**: All users and contributors

---

## 📂 Learning Materials (`/guides/`)

The `guides/` directory contains educational content for learning purposes.

### `COMPLETE_LEARNING_GUIDE.md`
- **Purpose**: Comprehensive learning resource
- **Content**:
  - 20 detailed chapters
  - Code explanations
  - Best practices
  - Exercises and quizzes
  - Project challenges
  - Advanced topics
- **Size**: ~6,500+ lines
- **Chapters**:
  1. Introduction to AI Chatbots
  2. Understanding the Tech Stack
  3. Project Setup
  4. Configuration Management
  5. School Data Structure
  6. Streamlit Basics
  7. Building the User Interface
  8. State Management
  9. Chat Logic Implementation
  10. OpenAI API Integration
  11. Prompt Engineering
  12. Error Handling
  13. Advanced Features
  14. Testing & Debugging
  15. Deployment
  16. Security Best Practices
  17. Performance Optimization
  18. Customization Guide
  19. Troubleshooting
  20. Future Enhancements
- **Format**: Markdown
- **Audience**: Students, learners

### `COMPLETE_LEARNING_GUIDE.pdf`
- **Purpose**: Printable version of the guide
- **Content**: Same as MD version
- **Size**: ~15,000+ lines (formatted)
- **Format**: PDF
- **Use Case**: Offline reading, printing, sharing

### `QUICK_REFERENCE.md`
- **Purpose**: One-page reference card
- **Content**:
  - Quick commands
  - Key concepts
  - Code snippets
  - Troubleshooting tips
  - Common patterns
- **Size**: ~450 lines
- **Format**: Markdown
- **Audience**: All users (quick lookup)

### `BLOG_ARTICLE.md`
- **Purpose**: Marketing and promotional content
- **Content**:
  - Project overview
  - Benefits and features
  - Use cases
  - Pricing suggestions
  - Call to action
  - FAQ
- **Size**: ~650 lines
- **Format**: Markdown (blog-ready)
- **Audience**: Potential buyers, website visitors

---

## 📂 Static Assets (`/assets/`)

The `assets/` directory is for static files like images and logos.

**Typical Contents**:
- Screenshots of the application
- Logo images
- Icon files
- Demo GIFs
- Architecture diagrams

**Usage**: Referenced in README and documentation

---

## 📄 Root Files

### `run_app.py`
- **Purpose**: Main entry point for the application
- **Usage**: `python run_app.py`
- **Content**:
  - Path setup
  - Streamlit launcher
  - User-friendly messages
- **Size**: ~30 lines

### `requirements.txt`
- **Purpose**: Python dependencies
- **Content**:
  ```
  streamlit==1.28.1
  openai==1.3.0
  python-dotenv==1.0.0
  pandas==2.1.3
  datetime
  httpx
  ```
- **Usage**: `pip install -r requirements.txt`

### `README.md`
- **Purpose**: Main project documentation
- **Content**:
  - Project overview
  - Features list
  - Installation guide
  - Usage instructions
  - Customization guide
  - Troubleshooting
  - Contributing guidelines
- **Size**: ~560 lines
- **Format**: Markdown

### `LICENSE`
- **Purpose**: Software license
- **Content**: MIT License text
- **Size**: ~20 lines

### `.env`
- **Purpose**: Environment variables
- **Content**:
  ```
  OPENAI_API_KEY=your_key_here
  ```
- **⚠️ Note**: Not in repository, create manually
- **Security**: Never commit this file

### `.gitignore`
- **Purpose**: Git ignore patterns
- **Content**:
  - `.env`
  - `chat_history.pkl`
  - `__pycache__/`
  - `venv/`
  - `*.pyc`
  - `.DS_Store`

### `chat_history.pkl`
- **Purpose**: Saved chat conversations
- **Format**: Python pickle file
- **Auto-generated**: Created on first chat
- **Ignored by Git**: Yes

---

## 🔄 File Dependencies

### Dependency Graph

```
run_app.py
    └── src/app.py
            ├── src/config.py
            │       └── .env
            ├── src/school_data.py
            └── chat_history.pkl

requirements.txt
    └── (all Python packages)

docs/
    └── (standalone documentation)

guides/
    └── (standalone learning materials)
```

---

## 📊 File Statistics

| Directory | Files | Total Lines | Purpose |
|-----------|-------|-------------|---------|
| `/src/` | 5 | ~700 | Source code |
| `/docs/` | 4 | ~800 | Documentation |
| `/guides/` | 4 | ~22,000+ | Learning materials |
| `/assets/` | Variable | N/A | Media files |
| Root | 6 | ~600 | Configuration |
| **Total** | **19+** | **~24,000+** | Complete project |

---

## 🎯 Design Principles

### 1. **Separation of Concerns**
- **Source code** in `/src/`
- **Documentation** in `/docs/`
- **Learning materials** in `/guides/`
- **Configuration** at root

### 2. **Modularity**
- Each file has a single responsibility
- Clear import structure
- Easy to maintain and update

### 3. **Accessibility**
- Clear naming conventions
- Comprehensive documentation
- Multiple entry points

### 4. **Scalability**
- Easy to add new features
- Organized for growth
- Clean architecture

### 5. **User-Friendliness**
- Simple run commands
- Clear file purposes
- Helpful README

---

## 🚀 Navigation Guide

### For New Users
1. Start with: `README.md`
2. Then read: `docs/SETUP.md`
3. Run: `python run_app.py`

### For Learners
1. Read: `guides/COMPLETE_LEARNING_GUIDE.md`
2. Reference: `guides/QUICK_REFERENCE.md`
3. Practice: Modify `src/school_data.py`

### For Contributors
1. Read: `docs/CONTRIBUTING.md`
2. Study: `docs/PROJECT_STRUCTURE.md` (this file)
3. Code: `src/app.py`

### For Customization
1. Data: `src/school_data.py`
2. Settings: `src/config.py`
3. UI: `src/app.py`

---

## 📝 File Naming Conventions

### Python Files
- Lowercase with underscores: `school_data.py`
- Descriptive names: `config.py`, not `conf.py`

### Documentation
- UPPERCASE: `README.md`, `SETUP.md`
- Descriptive: `PROJECT_STRUCTURE.md`

### Directories
- Lowercase, plural: `docs/`, `guides/`, `assets/`
- Abbreviations: `src/` (source)

---

## 🔐 Security Considerations

### Sensitive Files
- `.env` - **NEVER commit**
- `chat_history.pkl` - **User privacy**
- API keys - **Environment variables only**

### .gitignore Coverage
All sensitive files are properly ignored:
- ✅ `.env`
- ✅ `chat_history.pkl`
- ✅ `__pycache__/`
- ✅ `venv/`

---

## 📦 Deployment Structure

When deploying, ensure:
1. ✅ All `/src/` files are included
2. ✅ `requirements.txt` is present
3. ✅ `run_app.py` or similar entry point
4. ✅ `.env` is created (not from repo)
5. ✅ Documentation is available

---

## 🎓 Best Practices

### When Adding New Files
1. **Source code** → `/src/`
2. **Documentation** → `/docs/`
3. **Learning materials** → `/guides/`
4. **Images/media** → `/assets/`

### When Modifying Structure
1. Update this document
2. Update `README.md`
3. Test all entry points
4. Check imports

### When Sharing Project
1. Include complete `/src/`
2. Include `/docs/` and `/guides/`
3. Provide `.env.example`
4. Update README

---

## 🔍 Quick File Finder

**Need to:**
- Run the app? → `run_app.py`
- Configure settings? → `src/config.py`
- Add school data? → `src/school_data.py`
- Modify UI? → `src/app.py`
- Learn how it works? → `guides/COMPLETE_LEARNING_GUIDE.md`
- Quick reference? → `guides/QUICK_REFERENCE.md`
- Set up project? → `docs/SETUP.md`
- Contribute? → `docs/CONTRIBUTING.md`
- Understand structure? → `docs/PROJECT_STRUCTURE.md` (this file!)

---

## 📞 Need Help?

If you're confused about the structure:
1. Read the `README.md` first
2. Check this document for details
3. Review `docs/SETUP.md` for setup
4. Open an issue on GitHub

---

**Last Updated**: October 2025
**Version**: 1.0.0  
**Maintainer**: Smart Duke

