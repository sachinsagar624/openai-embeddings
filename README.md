# OpenAI Text Embeddings

This project demonstrates how to generate text embeddings using **OpenAI's `text-embedding-3-large` model** with LangChain.

## Model

* **Model:** `text-embedding-3-large`
* **Provider:** OpenAI
* **Framework:** LangChain
* **Purpose:** Convert text into numerical vector representations

## Project Structure

```text
openai-embeddings/
│
├── embedding.py
├── requirements.txt
└── README.md
```

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project directory:

```text
OPENAI_API_KEY=your_openai_api_key
```

**Do not upload the `.env` file or your API key to GitHub.**

## How It Works

The project uses the `OpenAIEmbeddings` class to convert text into a numerical vector.

Example:

```python
embedding = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=64
)

vector = embedding.embed_query("you are my love")
```

The generated vector contains **64 dimensions** because the code explicitly sets:

```text
dimensions=64
```

## How to Run

Run the Python file:

```bash
python embedding.py
```

The program prints:

1. The generated embedding vector
2. The vector length

## Technologies Used

* Python
* LangChain
* OpenAI Embeddings
* `text-embedding-3-large`
* python-dotenv

## Learning Objective

This project demonstrates how to:

1. Use OpenAI embedding models with LangChain.
2. Convert text into numerical vectors.
3. Generate embeddings using `embed_query()`.
4. Understand vector dimensions.
5. Prepare embeddings for applications such as semantic search and Retrieval-Augmented Generation (RAG).

## Author

**Sachin Sagar**
