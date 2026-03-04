import os
import faiss
import numpy as np
from openai import OpenAI

client = OpenAI()

documents = []
doc_texts = []

for file in os.listdir("docs"):
    with open(f"docs/{file}") as f:
        text = f.read()
        documents.append(file)
        doc_texts.append(text)

embeddings = []

for text in doc_texts:
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    embeddings.append(response.data[0].embedding)

embeddings = np.array(embeddings).astype("float32")

index = faiss.IndexFlatL2(len(embeddings[0]))
index.add(embeddings)

faiss.write_index(index, "vector.index")

np.save("docs.npy", doc_texts)

print("Documents embedded successfully")