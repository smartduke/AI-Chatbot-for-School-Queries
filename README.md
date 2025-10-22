# 🎓 AI Chatbot for School Queries

An intelligent AI-powered chatbot application that helps students, parents, and staff get instant answers about school schedules, homework, events, and policies. Built with modern technologies and designed for ease of use.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28.1-red.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Demo](#-demo)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Customization](#-customization)
- [Features in Detail](#-features-in-detail)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

## ✨ Features

### Core Functionality
- 🤖 **AI-Powered Responses**: Natural language conversations using OpenAI GPT-4o-mini
- 📅 **School Schedule Management**: View daily schedules and class timings
- 📚 **Homework Tracking**: Check assignments and due dates
- 🎉 **Event Information**: Get details about upcoming school events
- 📋 **Policy Access**: Quick access to school policies and guidelines
- 📞 **Contact Directory**: Staff contact information at your fingertips

### Advanced Features
- 💾 **Chat History**: Automatically saves and restores conversations
- 📥 **Download Transcripts**: Export chat history as formatted text files
- 🔍 **Search Functionality**: Search through chat history instantly
- 🌐 **Multi-Language Support**: Available in 6 languages (English, Spanish, French, Hindi, German, Chinese)
- 👤 **User Avatars**: Visual distinction between user and AI messages
- ⏰ **Timestamps**: Track when messages were sent
- 🔄 **Auto-Retry**: Automatic retry mechanism for failed API requests
- ⚠️ **Error Handling**: User-friendly error messages with recovery suggestions
- ✅ **API Validation**: Validates API key on startup

### User Experience
- 🎨 **Modern UI**: Clean, intuitive interface with gradient designs
- 📱 **Responsive Design**: Works seamlessly on desktop and mobile
- ⚡ **Quick Actions**: One-click access to common queries
- 🎯 **Example Questions**: Built-in suggestions to get started
- 🗑️ **Clear Chat**: Easy conversation reset
- 📊 **Message Counter**: Track conversation length

## 🛠️ Tech Stack

### Backend
- **Python 3.7+**: Core programming language
- **OpenAI API**: GPT-4o-mini model for natural language processing
- **python-dotenv**: Environment variable management

### Frontend
- **Streamlit 1.28.1**: Web application framework
- **HTML/CSS**: Custom styling and layout
- **JavaScript**: Interactive elements and auto-scroll

### Data Management
- **Pickle**: Chat history persistence
- **JSON**: School data storage and API communication
- **Pandas**: Data manipulation

### Development Tools
- **Git**: Version control
- **pip**: Package management

## 🎥 Demo

### Screenshots

**Main Interface**
- Clean chat interface with avatars
- Sidebar with quick actions
- Real-time AI responses

**Key Features**
- Search through chat history
- Download conversation transcripts
- Multi-language support
- Mobile-responsive design

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.7 or higher**
  ```bash
  python --version
  ```

- **pip** (Python package installer)
  ```bash
  pip --version
  ```

- **OpenAI API Key**
  - Sign up at [OpenAI Platform](https://platform.openai.com/)
  - Generate an API key from your account dashboard

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/ai-chatbot-school-queries.git
cd ai-chatbot-school-queries
```

### Step 2: Create Virtual Environment (Optional but Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- streamlit==1.28.1
- openai==1.3.0
- python-dotenv==1.0.0
- pandas==2.1.3
- datetime

## ⚙️ Configuration

### Step 1: Set Up Environment Variables

Create a `.env` file in the project root directory:

```bash
touch .env
```

Add your OpenAI API key to the `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

**⚠️ Important**: Never commit your `.env` file to version control. It's already included in `.gitignore`.

### Step 2: Customize School Data (Optional)

Edit `school_data.py` to add your school's information:

```python
# Update school schedules
SCHOOL_SCHEDULE = {
    "Monday": {
        "8:00 AM - 8:45 AM": "Your Class Name",
        # ... add more classes
    }
}

# Update events
UPCOMING_EVENTS = [
    {
        "date": "2024-01-15",
        "event": "Your Event Name",
        "time": "Event Time",
        "location": "Event Location"
    }
]

# Update homework assignments, policies, and contact info
```

### Step 3: Configure Settings (Optional)

Edit `config.py` to customize:

```python
# School Information
SCHOOL_NAME = "Your School Name"
SCHOOL_ADDRESS = "Your School Address"
SCHOOL_PHONE = "Your Phone Number"
SCHOOL_EMAIL = "Your Email"

# AI Model Settings
MODEL = "gpt-4o-mini"  # or "gpt-3.5-turbo"
TEMPERATURE = 0.7
MAX_TOKENS = 1000
```

## 🎮 Usage

### Running the Application

#### Method 1: Using Streamlit Command

```bash
streamlit run app.py
```

The app will automatically open in your default browser at `http://localhost:8501`

#### Method 2: Using the Launcher Script

```bash
python run.py
```

### Using the Chatbot

1. **Start Chatting**: Type your question in the input field and press Enter
2. **Quick Actions**: Use sidebar buttons for common queries
3. **Search**: Use the search box to find specific messages
4. **Download**: Click "Download Transcript" to save your conversation
5. **Clear Chat**: Use "Clear Chat" button to start fresh
6. **Change Language**: Select your preferred language from the dropdown

### Example Questions

**Schedule Questions:**
- "What's my schedule for Monday?"
- "When is my math class?"
- "What time is lunch?"

**Homework Questions:**
- "What homework is due this week?"
- "What's assigned for math class?"
- "Any assignments for English?"

**Event Questions:**
- "What events are happening this month?"
- "When is the science fair?"
- "Tell me about upcoming activities"

**General Questions:**
- "What are the school policies?"
- "How can I contact the principal?"
- "What's the dress code?"

## 📁 Project Structure

```
ai-chatbot-school-queries/
│
├── app.py                      # Main Streamlit application
├── config.py                   # Configuration settings
├── school_data.py             # School information and data
├── requirements.txt           # Python dependencies
├── run.py                     # Launcher script
├── README.md                  # This file
├── .env                       # Environment variables (create this)
├── .gitignore                 # Git ignore rules
├── chat_history.pkl           # Auto-generated chat history (ignored by git)
│
└── (virtual environment)      # Optional: venv/
```

### File Descriptions

- **app.py**: Main application with UI, chat logic, and API integration
- **config.py**: Centralized configuration for school info and AI settings
- **school_data.py**: Sample school data (schedules, events, homework, policies)
- **requirements.txt**: All Python package dependencies
- **run.py**: Simple launcher script with dependency checking
- **.env**: Environment variables (API keys) - **NOT in repository**
- **chat_history.pkl**: Automatically saved chat conversations

## 🎨 Customization

### Changing School Information

1. Open `config.py`
2. Update the school configuration section:
   ```python
   SCHOOL_NAME = "Your School Name"
   SCHOOL_ADDRESS = "Your Address"
   SCHOOL_PHONE = "Your Phone"
   SCHOOL_EMAIL = "Your Email"
   ```

### Updating School Data

1. Open `school_data.py`
2. Modify the data structures:
   - `SCHOOL_SCHEDULE`: Weekly class schedules
   - `UPCOMING_EVENTS`: School events and activities
   - `HOMEWORK_ASSIGNMENTS`: Subject-wise homework
   - `SCHOOL_POLICIES`: Rules and guidelines
   - `CONTACT_INFO`: Staff contact information

### Customizing UI Colors

Edit the CSS section in `app.py` (lines 20-88):

```python
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #YOUR_COLOR1, #YOUR_COLOR2);
    }
    /* ... modify other styles ... */
</style>
""", unsafe_allow_html=True)
```

### Changing AI Model

In `config.py`, update:

```python
MODEL = "gpt-4o-mini"  # Options: "gpt-3.5-turbo", "gpt-4", "gpt-4o-mini"
TEMPERATURE = 0.7      # Range: 0.0 to 1.0 (higher = more creative)
MAX_TOKENS = 1000      # Response length limit
```

## 🔍 Features in Detail

### Chat History Persistence
- Conversations automatically save to `chat_history.pkl`
- Restored when you reopen the app
- Survives browser refreshes and app restarts

### Download Transcripts
- Formatted text files with timestamps
- Includes all messages from the session
- Organized with clear headers and separators
- Perfect for record-keeping or sharing

### Search Functionality
- Real-time search through all messages
- Case-insensitive matching
- Shows filtered results instantly
- Easy to clear and reset

### Multi-Language Support
- **English**: Default language
- **Spanish**: Español
- **French**: Français
- **Hindi**: हिंदी
- **German**: Deutsch
- **Chinese**: 中文

AI automatically responds in the selected language!

### Error Handling
- **Automatic Retries**: 3 attempts with exponential backoff
- **User-Friendly Messages**: Clear explanations of errors
- **Recovery Suggestions**: Helps users fix issues
- **Network Resilience**: Handles connection problems gracefully

### API Key Validation
- Checks key format on startup
- Validates before making requests
- Clear error messages if invalid
- Prevents unnecessary API calls

## 🐛 Troubleshooting

### Common Issues

**1. API Key Not Working**
```
Error: API key validation failed
```
**Solution:**
- Check your API key in the `.env` file
- Ensure it starts with `sk-`
- Verify you have API credits on OpenAI
- Make sure the key has proper permissions

**2. App Won't Start**
```
ModuleNotFoundError: No module named 'streamlit'
```
**Solution:**
```bash
pip install -r requirements.txt
```

**3. Chat History Error**
```
Error loading chat history
```
**Solution:**
```bash
# Delete the corrupted file
rm chat_history.pkl
# Restart the app
streamlit run app.py
```

**4. Connection Timeout**
```
Error after 3 attempts: Connection timeout
```
**Solution:**
- Check your internet connection
- Verify OpenAI service status
- Try again after a few minutes
- Check firewall settings

**5. Import Errors**
```
ImportError: cannot import name 'X' from 'Y'
```
**Solution:**
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

### Getting Help

If you encounter issues:

1. Check the [Issues](https://github.com/yourusername/ai-chatbot-school-queries/issues) page
2. Review [OpenAI Documentation](https://platform.openai.com/docs)
3. Check [Streamlit Documentation](https://docs.streamlit.io/)
4. Create a new issue with:
   - Error message
   - Steps to reproduce
   - Python version
   - Operating system

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Ways to Contribute

1. **Report Bugs**: Open an issue describing the bug
2. **Suggest Features**: Share your ideas for improvements
3. **Submit Pull Requests**: Fix bugs or add features
4. **Improve Documentation**: Help make the README clearer
5. **Share Feedback**: Let us know how you're using the app

### Contribution Guidelines

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Standards

- Follow PEP 8 style guidelines
- Add comments for complex logic
- Update documentation for new features
- Test your changes thoroughly
- Keep commits focused and atomic

## 📄 License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2024 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 🎓 Learning Outcomes

This project demonstrates:

- **API Integration**: Working with OpenAI's GPT models
- **Prompt Engineering**: Crafting effective AI prompts
- **UI Development**: Building interactive web apps with Streamlit
- **Data Management**: Organizing and structuring information
- **State Management**: Handling user sessions and data persistence
- **Error Handling**: Implementing robust error recovery
- **User Experience**: Creating intuitive interfaces
- **Python Programming**: Advanced Python concepts and best practices

## 🚀 Future Enhancements

Potential features for future versions:

- 🗄️ Database integration (PostgreSQL/MongoDB)
- 👥 User authentication and profiles
- 📧 Email notifications for events
- 📱 Native mobile app
- 🎤 Voice input/output
- 📊 Analytics dashboard
- 🔌 School management system integration
- 🎮 Gamification elements
- 📅 Calendar integration (Google Calendar)
- 🤖 Advanced AI features (sentiment analysis, personalization)

## 📞 Contact

**Project Maintainer**: [Your Name]

- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com
- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)

**Project Link**: [https://github.com/yourusername/ai-chatbot-school-queries](https://github.com/yourusername/ai-chatbot-school-queries)

## 🙏 Acknowledgments

- [OpenAI](https://openai.com/) for providing the GPT API
- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Python Community](https://www.python.org/community/) for excellent packages
- All contributors and users of this project

## ⭐ Show Your Support

If you find this project helpful, please consider:

- ⭐ Starring the repository
- 🍴 Forking it for your own use
- 📢 Sharing it with others
- 🐛 Reporting bugs
- 💡 Suggesting new features

## 📊 Project Status

- **Status**: Active Development
- **Version**: 1.0.0
- **Last Updated**: October 2024
- **Maintained**: Yes

---

**Made with ❤️ for education and learning**

*Empowering schools with AI-powered communication*