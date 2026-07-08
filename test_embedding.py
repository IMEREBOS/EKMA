from backend.embedding_generator import generate_embeddings

chunks = [
    "Python is used for AI.",
    "FastAPI is a backend framework.",
    "Machine Learning predicts data."
]

embeddings = generate_embeddings(chunks)

print(type(embeddings))
print(embeddings.shape)
print(embeddings[0][:10])