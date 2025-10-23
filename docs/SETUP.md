# 🚀 Quick Setup Guide

## Prerequisites

- Python 3.7+
- pip
- OpenAI API Key

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-chatbot-school-queries.git
cd ai-chatbot-school-queries
```

### 2. Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root:

```bash
# On Windows
type nul > .env

# On macOS/Linux
touch .env
```

Add your OpenAI API key to `.env`:

```
OPENAI_API_KEY=your_actual_api_key_here
```

**Get your API key:**
1. Go to https://platform.openai.com/
2. Sign up or log in
3. Navigate to API Keys section
4. Create new secret key
5. Copy and paste it in the .env file

### 5. Run the Application

```bash
streamlit run app.py
```

Or use the launcher:

```bash
python run.py
```

The app will open in your browser at `http://localhost:8501`

## Customization (Optional)

### Update School Information

Edit `config.py`:
```python
SCHOOL_NAME = "Your School Name"
SCHOOL_ADDRESS = "Your Address"
SCHOOL_PHONE = "Your Phone"
SCHOOL_EMAIL = "Your Email"
```

### Add Your School Data

Edit `school_data.py`:
- Update `SCHOOL_SCHEDULE` with your class schedules
- Add your events to `UPCOMING_EVENTS`
- Update `HOMEWORK_ASSIGNMENTS`
- Modify `SCHOOL_POLICIES`
- Update `CONTACT_INFO`

## Troubleshooting

**Issue: ModuleNotFoundError**
```bash
pip install -r requirements.txt
```

**Issue: API Key Invalid**
- Check your `.env` file
- Ensure API key starts with `sk-`
- Verify you have API credits

**Issue: Port Already in Use**
```bash
streamlit run app.py --server.port 8502
```

## Support

For issues, check the main README.md or create an issue on GitHub.

