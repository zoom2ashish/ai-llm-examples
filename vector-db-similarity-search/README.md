# Vector Database Similarity Search

## Overview
This project implements a vector database for similarity search using Chroma. It processes documents (PDF or Markdown), generates embeddings for text chunks, and allows querying through a Gradio-based user interface.

## Features
- Extract text from PDF and Markdown files.
- Chunk large text into smaller segments for efficient embedding.
- Generate embeddings using the `OllamaEmbeddings` model.
- Store and query embeddings in a Chroma vector database.
- Interactive Gradio interface for querying the database.

## How It Works
1. **Text Extraction**: The `extract_text_from_document` function extracts text from PDF or Markdown files.
2. **Text Chunking**: The `chunk_text` function splits the extracted text into smaller chunks with optional overlap.
3. **Embedding Generation**: The `add_text_to_collection` function generates embeddings for the text chunks using the `OllamaEmbeddings` model.
4. **Vector Database**: The Chroma vector database stores the embeddings and allows querying for similar content.
5. **Query Interface**: A Gradio-based UI enables users to input queries and retrieve relevant results.

## File Structure
- `main.py`: Main script containing the implementation of text extraction, embedding generation, and the Gradio interface.
- `Itinerary.md`: Sample Markdown file used as input for the vector database.

## Requirements
Install the required dependencies using the following command:
```bash
pip install chromadb pypdf sentence-transformers langchain-ollama gradio
```
## Running the Example
To run the example, execute the following command:
```bash
python main.py
```
This will start the Gradio interface where query inputs can be entered.

## Example Input
* Input: "What is the itinerary for the trip?"
* Output: Relevant sections of the itinerary document.

## Functions Overview
- `extract_text_from_document(file_path)`: Extracts text from a PDF or Markdown file.
- `chunk_text(text, chunk_size=1000, overlap=200)`: Splits text into smaller chunks with optional overlap.
- `add_text_to_collection(text, collection)`: Generates embeddings for the text and adds them to the Chroma collection.
- `query_collection(query, collection)`: Queries the Chroma collection for similar text based on the input query.
- `main()`: Main function to run the Gradio interface and handle user queries.
-
## Future Improvements
- Add support for more document formats (e.g., DOCX, HTML).
- Implement more advanced text chunking strategies.
- Enhance the Gradio interface with more features (e.g., file upload, result visualization).
- Integrate additional embedding models for comparison.

# Technologies Used
- Python
- ChromaDB for vector storage
- Ollama for embedding generation
- Gradio for the user interface
- PyPDF for PDF extraction

# License
This project is licensed under the MIT License.