import faiss
import numpy as np


class VectorStore:
    def __init__(self):
        self.index = None

    def create_index(self, embeddings):
        """
        Create a FAISS index from embeddings.
        """

        embeddings = np.array(embeddings).astype("float32")

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(embeddings)

    def search(self, query_embedding, k=3):
        """
        Search the top-k similar embeddings.
        """

        query_embedding = np.array([query_embedding]).astype("float32")

        distances, indices = self.index.search(query_embedding, k)

        return distances, indices