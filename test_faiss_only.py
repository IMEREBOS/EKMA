import faiss
import numpy as np

print("FAISS Version:", faiss.__version__)

embeddings = np.random.rand(5, 384).astype("float32")

index = faiss.IndexFlatL2(384)

index.add(embeddings)

query = np.random.rand(1, 384).astype("float32")

distances, indices = index.search(query, 3)

print("Distances:")
print(distances)

print("Indices:")
print(indices)