import streamlit as st
import openai
from datetime import datetime
import json
import config
import os
import pickle
import time
from io import StringIO
from school_data import SCHOOL_SCHEDULE, UPCOMING_EVENTS, HOMEWORK_ASSIGNMENTS, SCHOOL_POLICIES, CONTACT_INFO

# Configure Streamlit page
st.set_page_config(
    page_title="Smart Academy AI Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .user-message {
        background-color: #007bff;
        color: white;
        padding: 0.75rem 1rem;
        border-radius: 15px 15px 5px 15px;
        margin: 0.75rem 0;
        text-align: right;
        position: relative;
        max-width: 80%;
        margin-left: auto;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    
    .bot-message {
        background-color: #e9ecef;
        color: #333;
        padding: 0.75rem 1rem;
        border-radius: 15px 15px 15px 5px;
        margin: 0.75rem 0;
        position: relative;
        max-width: 80%;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    
    .message-avatar {
        width: 35px;
        height: 35px;
        border-radius: 50%;
        display: inline-block;
        text-align: center;
        line-height: 35px;
        font-size: 18px;
        margin: 0 8px;
    }
    
    .user-avatar {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .bot-avatar {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    }
    
    .stButton > button {
        background-color: #667eea;
        color: white;
        border: none;
        border-radius: 20px;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }
    
    .stButton > button:hover {
        background-color: #5a6fd8;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Chat history file path
CHAT_HISTORY_FILE = "chat_history.pkl"

# Helper functions for chat persistence
def save_chat_history():
    """Save chat history to file"""
    try:
        with open(CHAT_HISTORY_FILE, 'wb') as f:
            pickle.dump(st.session_state.messages, f)
    except Exception as e:
        st.error(f"Error saving chat history: {e}")

def load_chat_history():
    """Load chat history from file"""
    try:
        if os.path.exists(CHAT_HISTORY_FILE):
            with open(CHAT_HISTORY_FILE, 'rb') as f:
                return pickle.load(f)
    except Exception as e:
        st.error(f"Error loading chat history: {e}")
    return []

def clear_chat_history():
    """Clear chat history"""
    st.session_state.messages = []
    if os.path.exists(CHAT_HISTORY_FILE):
        os.remove(CHAT_HISTORY_FILE)

def download_chat_transcript():
    """Generate chat transcript for download"""
    transcript = f"Smart Academy AI Assistant - Chat Transcript\n"
    transcript += f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    transcript += "="*60 + "\n\n"
    
    for msg in st.session_state.messages:
        role = "You" if msg["role"] == "user" else "AI Assistant"
        timestamp = msg.get("timestamp", "N/A")
        content = msg["content"]
        transcript += f"[{timestamp}] {role}:\n{content}\n\n"
        transcript += "-"*60 + "\n\n"
    
    return transcript

def search_messages(query):
    """Search messages by query string"""
    if not query:
        return st.session_state.messages
    
    query_lower = query.lower()
    filtered = []
    for msg in st.session_state.messages:
        if query_lower in msg["content"].lower():
            filtered.append(msg)
    return filtered

def validate_api_key():
    """Validate OpenAI API key"""
    try:
        if not config.OPENAI_API_KEY or config.OPENAI_API_KEY == "":
            return False, "API key is missing"
        if not config.OPENAI_API_KEY.startswith("sk-"):
            return False, "Invalid API key format"
        return True, "API key is valid"
    except Exception as e:
        return False, str(e)

def translate_text(text, target_language):
    """Translate text to target language"""
    language_map = {
        "Spanish": "es",
        "French": "fr",
        "Hindi": "hi",
        "German": "de",
        "Chinese": "zh"
    }
    
    # For now, we'll append instruction to OpenAI to respond in that language
    # In production, you'd use a translation API
    return f"[Translate to {target_language}] {text}"

# Initialize session state
if "messages" not in st.session_state:
    # Try to load existing chat history
    st.session_state.messages = load_chat_history()
if "user_input" not in st.session_state:
    st.session_state.user_input = ""
if "submit_query" not in st.session_state:
    st.session_state.submit_query = False
if "query_to_submit" not in st.session_state:
    st.session_state.query_to_submit = ""
if "search_query" not in st.session_state:
    st.session_state.search_query = ""
if "selected_language" not in st.session_state:
    st.session_state.selected_language = "English"
if "api_validated" not in st.session_state:
    # Validate API key on startup
    is_valid, message = validate_api_key()
    st.session_state.api_validated = is_valid
    if not is_valid:
        st.error(f"⚠️ API Key Validation Failed: {message}")

def get_openai_response(user_message, context="", max_retries=3):
    """Get response from OpenAI API with retry mechanism"""
    import httpx
    
    for attempt in range(max_retries):
        try:
            # Set up OpenAI client with explicit configuration to avoid proxy issues
            # Clear any proxy-related environment variables
            for key in list(os.environ.keys()):
                if 'PROXY' in key.upper() or 'proxy' in key:
                    del os.environ[key]
            
            # Set the API key
            os.environ["OPENAI_API_KEY"] = config.OPENAI_API_KEY
            
            # Create httpx client without proxies
            http_client = httpx.Client()
            
            # Initialize OpenAI client with explicit http_client
            client = openai.OpenAI(http_client=http_client)
            
            # Add language instruction if not English
            language_instruction = ""
            if st.session_state.selected_language != "English":
                language_instruction = f"\n\nIMPORTANT: Please respond in {st.session_state.selected_language} language."
            
            # Create system prompt with school context
            system_prompt = f"""
            You are a helpful AI assistant for {config.SCHOOL_NAME}. You help students, parents, and staff with school-related queries.
            
            School Information:
            - Name: {config.SCHOOL_NAME}
            - Address: {config.SCHOOL_ADDRESS}
            - Phone: {config.SCHOOL_PHONE}
            - Email: {config.SCHOOL_EMAIL}
            
            Available Information:
            - School Schedule: {json.dumps(SCHOOL_SCHEDULE, indent=2)}
            - Upcoming Events: {json.dumps(UPCOMING_EVENTS, indent=2)}
            - Homework Assignments: {json.dumps(HOMEWORK_ASSIGNMENTS, indent=2)}
            - School Policies: {json.dumps(SCHOOL_POLICIES, indent=2)}
            - Contact Information: {json.dumps(CONTACT_INFO, indent=2)}
            
            Guidelines:
            1. Be friendly, helpful, and professional
            2. Provide accurate information based on the school data
            3. If you don't know something, suggest contacting the school directly
            4. Keep responses concise but informative
            5. Use the school's name and branding appropriately
            {language_instruction}
            
            Context: {context}
            """
            
            response = client.chat.completions.create(
                model=config.MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=config.MAX_TOKENS,
                temperature=config.TEMPERATURE
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            if attempt < max_retries - 1:
                # Wait before retrying
                time.sleep(1 * (attempt + 1))
                continue
            else:
                return f"⚠️ Error after {max_retries} attempts: {str(e)}\n\nPlease check your internet connection and API key, then try again."
    
    return "⚠️ Unable to get response. Please try again later."

def display_chat_message(message, is_user=True, timestamp=None, message_id=None):
    """Display a chat message with avatars and timestamp"""
    if timestamp is None:
        timestamp = datetime.now().strftime("%I:%M %p")
    
    # Generate unique message ID if not provided
    if message_id is None:
        message_id = f"msg_{len(st.session_state.messages)}"
    
    if is_user:
        st.markdown(f'''
        <div style="display: flex; align-items: flex-start; justify-content: flex-end; margin: 0.75rem 0;">
            <div class="user-message">
                <div>{message}</div>
                <div style="font-size: 0.75rem; opacity: 0.7; margin-top: 0.25rem;">{timestamp}</div>
            </div>
            <span class="message-avatar user-avatar">👤</span>
        </div>
        ''', unsafe_allow_html=True)
    else:
        st.markdown(f'''
        <div style="display: flex; align-items: flex-start; margin: 0.75rem 0;">
            <span class="message-avatar bot-avatar">🤖</span>
            <div class="bot-message">
                <div>{message}</div>
                <div style="font-size: 0.75rem; opacity: 0.7; margin-top: 0.25rem;">{timestamp}</div>
            </div>
        </div>
        ''', unsafe_allow_html=True)

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🎓 Smart Academy AI Assistant</h1>
        <p>Your intelligent guide for school information, schedules, and events</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        # Settings
        st.markdown("### ⚙️ Settings")
        
        # Language Selector
        languages = ["English", "Spanish", "French", "Hindi", "German", "Chinese"]
        selected_lang = st.selectbox("🌐 Language", languages, index=languages.index(st.session_state.selected_language))
        if selected_lang != st.session_state.selected_language:
            st.session_state.selected_language = selected_lang
        
        st.markdown("---")
        
        # Search Chat History
        st.markdown("### 🔍 Search Chat")
        search_query = st.text_input("Search messages", placeholder="Type to search...", key="search_input")
        if search_query:
            st.session_state.search_query = search_query
            filtered_msgs = search_messages(search_query)
            st.info(f"Found {len(filtered_msgs)} message(s)")
        else:
            st.session_state.search_query = ""
        
        st.markdown("---")
        
        # Quick Info Sections
        st.markdown("### 📅 Today's Schedule")
        today = datetime.now().strftime("%A")
        if today in SCHOOL_SCHEDULE:
            for time, subject in SCHOOL_SCHEDULE[today].items():
                st.text(f"{time}: {subject}")
        
        st.markdown("---")
        
        st.markdown("### 📋 Quick Actions")
        if st.button("📚 View All Schedules"):
            st.session_state.query_to_submit = "Show me the school schedule"
            st.session_state.submit_query = True
        
        if st.button("📅 Upcoming Events"):
            st.session_state.query_to_submit = "What events are coming up?"
            st.session_state.submit_query = True
        
        if st.button("📝 Homework Assignments"):
            st.session_state.query_to_submit = "What homework is assigned?"
            st.session_state.submit_query = True
        
        if st.button("📞 Contact Information"):
            st.session_state.query_to_submit = "How can I contact the school?"
            st.session_state.submit_query = True
        
        st.markdown("---")
        
        # Chat Management
        st.markdown("### 💬 Chat Management")
        
        # Message count
        message_count = len(st.session_state.messages)
        st.metric("Total Messages", message_count)
        
        # Download transcript
        if message_count > 0:
            transcript = download_chat_transcript()
            st.download_button(
                label="📥 Download Transcript",
                data=transcript,
                file_name=f"chat_transcript_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain",
                use_container_width=True
            )
        
        # Clear chat button
        if st.button("🗑️ Clear Chat", use_container_width=True):
            clear_chat_history()
            st.success("Chat cleared!")
            st.rerun()
        
        st.markdown("---")
        
        # School Info
        st.markdown("### 🏫 School Information")
        st.markdown(f"""
        **{config.SCHOOL_NAME}**
        
        📍 {config.SCHOOL_ADDRESS}
        
        📞 {config.SCHOOL_PHONE}
        
        ✉️ {config.SCHOOL_EMAIL}
        """)
    
    # Main chat interface
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("### 💬 Chat with the AI Assistant")
        
        # Chat container with auto-scroll
        chat_container = st.container()
        
        with chat_container:
            # Get messages to display (filtered or all)
            messages_to_display = search_messages(st.session_state.search_query) if st.session_state.search_query else st.session_state.messages
            
            if not messages_to_display and st.session_state.search_query:
                st.info("🔍 No messages found matching your search.")
            
            # Display chat messages with timestamps, avatars, and reactions
            for idx, message in enumerate(messages_to_display):
                timestamp = message.get("timestamp", datetime.now().strftime("%I:%M %p"))
                message_id = f"msg_{idx}"
                if message["role"] == "user":
                    display_chat_message(message["content"], is_user=True, timestamp=timestamp, message_id=message_id)
                else:
                    display_chat_message(message["content"], is_user=False, timestamp=timestamp, message_id=message_id)
            
            # Auto-scroll to bottom using JavaScript
            if messages_to_display:
                st.markdown("""
                <script>
                    var chatContainer = window.parent.document.querySelector('[data-testid="stVerticalBlock"]');
                    if (chatContainer) {
                        chatContainer.scrollTop = chatContainer.scrollHeight;
                    }
                </script>
                """, unsafe_allow_html=True)
        
        # Chat input with form for Enter key submission
        with st.form(key="chat_form", clear_on_submit=True):
            user_input = st.text_input("Ask me anything about school:", 
                                      placeholder="e.g., What's my schedule for tomorrow?",
                                      key="input_field")
            submit_button = st.form_submit_button("Send")
            
            if submit_button and user_input:
                st.session_state.query_to_submit = user_input
                st.session_state.submit_query = True
        
        # Process query from either input field or quick action buttons
        if st.session_state.submit_query and st.session_state.query_to_submit:
            # Get current timestamp
            current_time = datetime.now().strftime("%I:%M %p")
            
            # Add user message to chat with timestamp
            st.session_state.messages.append({
                "role": "user", 
                "content": st.session_state.query_to_submit,
                "timestamp": current_time
            })
            
            # Get AI response
            with st.spinner("🤔 Thinking..."):
                try:
                    ai_response = get_openai_response(st.session_state.query_to_submit)
                except Exception as e:
                    ai_response = f"⚠️ Error: {str(e)}\n\nPlease try again or contact support if the issue persists."
            
            # Add AI response to chat with timestamp
            response_time = datetime.now().strftime("%I:%M %p")
            st.session_state.messages.append({
                "role": "assistant", 
                "content": ai_response,
                "timestamp": response_time
            })
            
            # Save chat history
            save_chat_history()
            
            # Reset submission state
            st.session_state.submit_query = False
            st.session_state.query_to_submit = ""
            
            # Rerun to display new messages
            st.rerun()
    
    with col2:
        st.markdown("### 💡 Example Questions")
        st.markdown("""
        **Schedule Questions:**
        - What's my schedule for Monday?
        - When is my math class?
        - What time is lunch?
        
        **Event Questions:**
        - What events are happening this month?
        - When is the science fair?
        - Tell me about upcoming activities
        
        **Homework Questions:**
        - What homework is due this week?
        - What's assigned for math class?
        - Any assignments for English?
        
        **General Questions:**
        - What are the school policies?
        - How can I contact the principal?
        - What's the dress code?
        """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 1rem;">
        <p>🤖 Powered by OpenAI GPT • 🎓 Smart Academy • Made with ❤️ using Streamlit</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
