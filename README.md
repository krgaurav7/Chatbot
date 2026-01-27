# Chatbot 🧠

A modern, intelligent chatbot application built with FastAPI and LangChain, featuring a Streamlit web interface for interactive conversations. This project demonstrates the implementation of an AI-powered conversational agent with multi-threaded conversation management and streaming capabilities.

## Features ✨

- **FastAPI Backend**: High-performance REST API with automatic OpenAPI documentation
- **LangChain Integration**: Leverages LangChain for agent orchestration and conversation management
- **Thread Management**: Support for multiple concurrent conversation threads with persistent history
- **Streaming Responses**: Real-time streaming of chatbot responses for improved UX
- **Streamlit Frontend**: Interactive web interface for chatting with the bot
- **Database Integration**: MongoDB-based storage for conversation history and thread management
- **State Management**: Sophisticated state machine for managing chat agent behavior

## Tech Stack 🛠️

**Backend:**
- FastAPI 0.128.0
- LangChain (AI/LLM orchestration)
- Uvicorn (ASGI server)
- Python 3.13

**Frontend:**
- Streamlit
- Requests (HTTP client)

**Database:**
- MongoDB

**Additional Libraries:**
- python-dotenv (environment configuration)
- Various AI/ML dependencies

## Project Structure 📁

```
.
├── main.py                 # FastAPI application entry point
├── new_app.py             # Enhanced Streamlit interface with threading
├── app.py                 # Alternative Streamlit interface (basic)
├── src/
│   ├── agents/
│   │   └── chat_agent/
│   │       ├── graph.py           # Chat agent graph builder
│   │       ├── nodes/             # Agent nodes/actions
│   │       ├── states/            # State definitions
│   │       └── tools/             # Agent tools
│   ├── handlers/
│   │   └── chat_handler.py        # Request handlers for chat operations
│   ├── routes/
│   │   └── chat_route.py          # API route definitions
│   ├── services/
│   │   └── database_service.py    # Database operations
│   └── main.py
└── my_env/                # Python virtual environment
```

## Getting Started 🚀

### Prerequisites

- Python 3.13+
- MongoDB instance (local or cloud)
- pip or poetry for dependency management

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/krgaurav7/Chatbot.git
cd Chatbot
```

2. **Create and activate virtual environment:**
```bash
# Windows
python -m venv my_env
my_env\Scripts\activate

# Linux/macOS
python3 -m venv my_env
source my_env/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

Or if using the virtual environment in the repo:
```bash
my_env\Scripts\activate
```

4. **Configure environment variables:**
Create a `.env` file in the root directory:
```bash
DB_URI=mongodb://localhost:27017/chatbot
# Add other required environment variables
```

### Running the Application

#### Option 1: FastAPI Backend + Streamlit Frontend (Recommended)

1. **Start the FastAPI backend:**
```bash
python main.py
```
The API will be available at `http://localhost:8000`
- API documentation: `http://localhost:8000/docs`

2. **In another terminal, start the Streamlit interface:**
```bash
# Enhanced version with threading support
streamlit run new_app.py

# Or basic version
streamlit run app.py
```
The interface will open at `http://localhost:8501`

#### Option 2: Basic Streamlit Only

```bash
streamlit run app.py
```

## API Endpoints 📡

### Chat Endpoints

- **POST** `/chat/{thread_id}` - Send a message and get a response
  - Parameters: `message` (query parameter)
  - Returns: Chat state with messages

- **POST** `/stream/{thread_id}` - Stream chat response
  - Parameters: `message` (query parameter)
  - Returns: Streaming text response

### Thread Management

- **GET** `/chat/threads` - Get all conversation threads
  - Returns: List of thread IDs

- **GET** `/chat/history/{thread_id}` - Get conversation history
  - Returns: Chat state with message history

## Architecture 🏗️

### Backend Architecture

The backend follows a modular architecture:

1. **FastAPI Application** (`main.py`)
   - Manages application lifecycle
   - Database initialization on startup
   - Request routing

2. **Chat Agent** (`src/agents/chat_agent/`)
   - Graph-based agent orchestration
   - State management for conversations
   - Tool integration for extended capabilities

3. **Route Handler** (`src/routes/`)
   - REST endpoint definitions
   - Request/response mapping

4. **Business Logic** (`src/handlers/`)
   - Chat processing logic
   - Streaming response handling
   - Thread and history management

5. **Database Service** (`src/services/`)
   - MongoDB integration
   - Data persistence

### Frontend Architecture

- **Streamlit Interface** (`new_app.py`)
  - Multi-threaded conversation support
  - Real-time chat history
  - Thread management UI
  - Streaming response display

## Usage Examples 💬

### Using the Streamlit Interface

1. Open the Streamlit app in your browser
2. View existing threads or create a new conversation
3. Type your message in the chat input
4. View the bot's response in real-time

### Using the API Directly

```bash
# Get all threads
curl http://localhost:8000/chat/threads

# Send a message
curl -X POST "http://localhost:8000/chat/thread-abc123?message=Hello%20there"

# Stream a response
curl -N "http://localhost:8000/stream/thread-abc123?message=Tell%20me%20a%20story"
```

## Development 👨‍💻

### Project Setup for Development

1. Activate virtual environment
2. Install development dependencies
3. Set up MongoDB locally or use a cloud instance
4. Configure `.env` file with your settings

### Key Files to Modify

- `src/agents/chat_agent/graph.py` - Modify agent behavior
- `src/agents/chat_agent/nodes/` - Add or modify agent actions
- `src/agents/chat_agent/tools/` - Add new tools/capabilities
- `src/handlers/chat_handler.py` - Modify request handling logic

## Environment Variables

Create a `.env` file with the following:

```env
DB_URI=mongodb://localhost:27017/chatbot
# Add other configuration as needed
```

## Troubleshooting 🔧

### Database Connection Issues
- Ensure MongoDB is running: `mongod`
- Check `DB_URI` in `.env` matches your MongoDB setup

### API Not Responding
- Verify FastAPI server is running: `python main.py`
- Check `http://localhost:8000/docs` for API documentation

### Streamlit Issues
- Make sure FastAPI backend is running before starting Streamlit
- Clear Streamlit cache: `streamlit cache clear`

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📄

This project is open source and available under the MIT License.

## Author 👤

**Gaurav Kumar**
- GitHub: [@krgaurav7](https://github.com/krgaurav7)

## Acknowledgments 🙏

- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework
- [LangChain](https://www.langchain.com/) - LLM orchestration framework
- [Streamlit](https://streamlit.io/) - Rapid UI development
- [MongoDB](https://www.mongodb.com/) - NoSQL database

## Support 💬

For support, please open an issue on the GitHub repository.

---

**Happy Chatting! 🚀**
