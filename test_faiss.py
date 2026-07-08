from backend.embedding_generator import generate_embeddings
from backend.vector_store import VectorStore

chunks = [
    "Python is used for AI.",
    "Java is an object-oriented language.",
    "FastAPI is used for backend development.",
    "Machine Learning predicts data."
]

embeddings = generate_embeddings(chunks)

store = VectorStore()

store.create_index(embeddings)

query = "Backend Framework"

query_embedding = generate_embeddings([query])[0]

distances, indices = store.search(query_embedding)

print("Distances:")
print(distances)

print()

print("Indices:")
print(indices)

print()

print("Best Matching Chunks:")

for idx in indices[0]:
    print(chunks[idx])