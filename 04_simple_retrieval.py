# 04_simple_retrieval.py
# Simple semantic search: embed question → find closest chunks

import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity  # easy cosine function

# Load model (same as before)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load your saved chunks & embeddings
chunks = [
    "I am Rohit from Mumbai. I want to become a global data engineer who builds AI systems. My favorite thing is learning by doing, not watching videos. I have SQL knowledge but zero Python yet.",  # Chunk 1
    "videos. I have SQL knowledge but zero Python yet. In 2026 I will have a remote job paying in dollars."  # Chunk 2 - adjust if yours differ
]

embeddings = np.load('my_knowledge_embeddings.npy')

print("Loaded embeddings shape:", embeddings.shape)

# Ask a question
question = "What programming skills do I have right now?"
print("\nQuestion:", question)

# Embed the question
question_vector = model.encode([question])[0]  # shape (384,)

# Compute similarity to all chunks
similarities = cosine_similarity([question_vector], embeddings)[0]

# Find top match
top_idx = np.argmax(similarities)
top_score = similarities[top_idx]

print("\nTop matching chunk (similarity score: {:.3f}):".format(top_score))
print(chunks[top_idx])

# Optional: show all with scores
print("\nAll chunks ranked:")
for i, (score, chunk) in enumerate(sorted(zip(similarities, chunks), reverse=True)):
    print(f"Rank {i+1} (score {score:.3f}): {chunk[:100]}...")