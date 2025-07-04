# Multimodal RAG - Extract Texts and Images

This project demonstrates a Multimodal Retrieval-Augmented Generation (RAG) pipeline that extracts text and images from PDF documents, summarizes them using OpenRouter (via Gemini API), and stores embeddings for efficient retrieval using Chroma and Sentence Transformers (via HuggingFace).

## Features
- **PDF Parsing:** Extracts both text and images from PDF files using PyMuPDF.
- **Image Summarization:** Uses OpenRouter (via Gemini API) to summarize images and tables for retrieval.
- **Text Embedding:** Splits and embeds text using Sentence Transformers (HuggingFace Embeddings).
- **Vector Store:** Stores and retrieves document embeddings with Chroma.
- **Orchestration:** Utilizes LangChain for managing the retrieval and generation pipeline.
- **LLM-based QA:** Uses OpenRouter for question-answering over retrieved content.

## Dependencies
Install all dependencies with:

```bash
pip install -r requirements.txt
```

### Main Libraries
- **PyMuPDF (`pymupdf`):** For extracting text and images from PDFs.
- **Pillow (`pillow`):** For image processing and saving.
- **LangChain (`langchain`, `langchain-community`, `langchain-core`):** For orchestrating the RAG pipeline.
- **Chroma (`langchain_community.vectorstores`):** For vector storage and retrieval.
- **Sentence Transformers (`sentence-transformers`, `langchain-huggingface`):** For embedding document splits using HuggingFace models.
- **OpenAI (`openai`):** For interfacing with OpenRouter API.
- **python-dotenv:** For loading environment variables (API keys, etc.).

## Environment Variables
Create a `.env` file in the project root with your API keys:

```
OPENROUTER_API_KEY=your_openrouter_api_key_here
OPENROUTER_URL=https://openrouter.ai/v1
MODEL_NAME=google/gemini-2.0-flash-001
```

**Note:** `.env`, `extracted_images/`, and `training_documents/` are included in `.gitignore` and will not be committed to version control.

## Usage
1. Place your PDF file (e.g., `1706.03762v7.pdf`) in the project directory.
2. Run the Jupyter notebook `notebook.ipynb` step by step:
    - Extracts text and images from the PDF.
    - Summarizes images/tables using OpenRouter (via Gemini API).
    - Splits and embeds text/images using Sentence Transformers (HuggingFace Embeddings).
    - Stores embeddings in Chroma for retrieval.
    - Uses OpenRouter for LLM-based question-answering over the retrieved content.
3. All extracted images are saved in the `extracted_images/` folder.
4. You can use the `training_documents/` folder to store any additional documents for training or experimentation. This folder is ignored by git.

## Project Structure
```
├── 1706.03762v7.pdf
├── extracted_images/
│   └── image_X_Y.png
├── training_documents/
│   └── ...
├── notebook.ipynb
├── requirements.txt
├── .env  # (not committed)
├── .gitignore
```

## Notes
- Make sure to set your API keys in the `.env` file before running the notebook.
- Start your Jupyter environment from a terminal where the environment variables are loaded, or use `python-dotenv` as shown in the notebook.
- The `extracted_images/` and `training_documents/` folders are ignored by git and are safe for storing generated or experimental data.
- Document splits and embeddings are handled by Sentence Transformers (HuggingFace). LLM-based image summarization and QA are handled through OpenRouter.
- OpenRouter is used to access both Gemini and other LLMs without dealing with individual API quotas and rate limits.

## License
MIT License
