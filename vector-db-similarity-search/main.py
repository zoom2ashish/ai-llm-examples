import chromadb
from chromadb.config import Settings
from pypdf import PdfReader
import os
from sentence_transformers import SentenceTransformer
from langchain_ollama import OllamaEmbeddings
import gradio as gr

def extract_text_from_document(file_path):
    """
    Extract text from a PDF file.
    """
    _, ext = os.path.splitext(file_path)

    if ext.lower() == ".pdf":
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() if page.extract_text() else ""
        text = text.strip()
        return text
    elif ext.lower() == ".md":
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
        return text

    raise ValueError("Unsupported file format. Only PDF files are supported.")


def create_chroma_collection():
    """
    Create a Chroma collection.
    """
    client = chromadb.PersistentClient("./.chromadb")
    collection = client.get_or_create_collection(name="documents_collection")
    return collection


def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    length = len(text)
    while start < length:
        end = min(start + chunk_size, length)
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap  # move forward with overlap
    return chunks


def add_text_to_collection(collection, text, chunk_size=500, overlap=50):
    """
    Add chunked text to the Chroma collection.
    """
    embedder = OllamaEmbeddings(model="nomic-embed-text")

    # Split text into chunks
    chunks = chunk_text(text, chunk_size=chunk_size, overlap=overlap)

    # Generate embeddings for all chunks
    embeddings = embedder.embed_documents(chunks)

    # Add chunks to collection with unique IDs
    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=[str(hash(chunk)) for chunk in chunks]
    )

def query_chroma_collection(collection, query):
    """
    Query the Chroma collection and return results as a string.
    """
    embedder = OllamaEmbeddings(model="nomic-embed-text")
    query_embedding = embedder.embed_query(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    # results["documents"] is a list of lists, one per query (we have one query)
    docs = results["documents"][0] if results["documents"] else []

    return "\n\n".join(docs) if docs else "No results found."


# Add Gradio UI to query the vector database
def gradio_interface(collection):
    """
    Gradio interface for querying the vector database.
    """
    def query_vector_db(query):
        results = query_chroma_collection(collection, query)
        return results


    with gr.Blocks() as demo:
        gr.Markdown("## Vector Database Similarity Search")
        with gr.Row():
            with gr.Column():
                query_input = gr.Textbox(label="Enter your query:")
                submit_button = gr.Button("Submit")
            with gr.Column():
                results_output = gr.Markdown(label="Results:")

        submit_button.click(fn=query_vector_db, inputs=[query_input], outputs=[results_output])

    demo.launch()

def main():
    """
    Main function to run the application.
    """
    # Initialize the Chroma client
    texts = extract_text_from_document("vector-db-similarity-search/Itinerary.md")

    collection = create_chroma_collection()
    add_text_to_collection(collection, texts)

    # # Query the collection
    # query = "What is the itinerary for the trip?"
    # results = query_chroma_collection(collection, query)
    # print(results)

    # Launch the Gradio interface
    gradio_interface(collection)





if __name__ == "__main__":
    main()