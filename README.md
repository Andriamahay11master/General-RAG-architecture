# General RAG Architecture

An AI-powered Document Q&A System using Retrieval-Augmented Generation (RAG) to provide accurate answers based on uploaded documents.

## Features

- **Document Processing**: Load and process text documents from a data directory
- **Intelligent Chunking**: Split documents into meaningful chunks for better retrieval
- **Vector Embeddings**: Use sentence-transformers for high-quality text embeddings
- **Efficient Search**: FAISS vector database for fast similarity search
- **LLM Integration**: Powered by Groq's Llama 3.1 model for natural language responses
- **Web Interface**: Clean chat-based UI for asking questions
- **Source Attribution**: Answers include references to source documents

## Architecture

The system consists of several key components:

- **Loader**: Reads documents from the `data/` directory
- **Chunker**: Splits text into manageable chunks with overlap
- **Embeddings**: Converts text chunks to vector representations
- **Vector Store**: Stores and searches vectors using FAISS
- **Retriever**: Combines loading, chunking, and vector search
- **LLM Engine**: Generates answers using retrieved context
- **Flask App**: Web server with REST API and chat interface

## Project Structure

```
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── back/                 # Backend modules
│   ├── __init__.py
│   ├── answer_engine.py
│   ├── chunker.py        # Text chunking logic
│   ├── embeddings.py     # Embedding generation
│   ├── llm_engine.py     # LLM integration with Groq
│   ├── loader.py         # Document loading
│   ├── retriever.py      # Main retrieval orchestration
│   ├── vectorstore.py    # FAISS vector operations
│   └── test_*.py         # Test scripts for components
├── data/                 # Document storage
│   ├── ai_overview.txt
│   ├── data_science.txt
│   ├── machine_learning.txt
│   ├── natural_language_processing.txt
│   └── sample.txt
├── static/               # Static assets
│   ├── css/
│   │   └── style.css
│   └── scss/             # SCSS source files
│       ├── _animations.scss
│       ├── _chat.scss
│       ├── _layout.scss
│       ├── _mixins.scss
│       ├── _variables.scss
│       └── style.scss
└── templates/            # HTML templates
    └── index.html        # Chat interface
```

## Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd General-RAG-architecture
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```
   Get your API key from [Groq Console](https://console.groq.com/).

## Usage

1. **Add documents**: Place your text documents in the `data/` directory

2. **Run the application**:

   ```bash
   python app.py
   ```

3. **Open your browser** and go to `http://localhost:5000`

4. **Ask questions**: Type questions about your documents in the chat interface

## API Endpoints

- `GET /`: Main chat interface
- `POST /ask`: Submit a question and get an answer
  - Request: `{"question": "Your question here"}`
  - Response: `{"answer": "AI-generated answer with sources"}`

## Dependencies

- **Flask**: Web framework
- **sentence-transformers**: Text embeddings
- **faiss-cpu**: Vector similarity search
- **groq**: LLM API client
- **python-dotenv**: Environment variable management
- **numpy, scipy, scikit-learn**: Scientific computing
- **pandas**: Data manipulation
- **pdfplumber**: PDF processing (for future PDF support)

## Configuration

The system uses the following default configurations (can be modified in the code):

- Embedding model: `all-MiniLM-L6-v2`
- Chunk size: 1000 characters with 200 character overlap
- Retrieval: Top 3 most similar chunks
- LLM: `llama-3.1-8b-instant`

## Testing

Individual components can be tested using the provided test scripts:

- `test_step.py`: Test document loading and chunking
- `test_step2.py`: Test embeddings and vector store
- `test_step3.py`: Test full retrieval pipeline
- `test_groq.py`: Test LLM integration

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source. Please check the license file for details.
