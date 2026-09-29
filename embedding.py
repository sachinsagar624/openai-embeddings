from dotenv import load_dotenv

load_dotenv()

from langchain_openai import OpenAIEmbeddings

embedding = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=64
)

vector = embedding.embed_query("you are my love")

print(vector)
print("Vector length:", len(vector))
