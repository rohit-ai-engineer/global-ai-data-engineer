# 03_generate_embeddings.py
# Turn text chunks into numerical vectors (embeddings) for semantic search

from sentence_transformers import SentenceTransformer
import numpy as np
import re

# Load a small, fast, free embedding model (~80 MB download first time)
print("Loading embedding model... (may take 1-2 minutes first run)")
model = SentenceTransformer('all-MiniLM-L6-v2')
print("Model loaded! Each chunk becomes a vector of 384 numbers.")

# Smart chunk function (reused from before)
def smart_chunk(text, max_chunk_size=200, overlap=60):
    chunks = []
    start = 0
    text_length = len(text)
    
    while start < text_length:
        end = min(start + max_chunk_size, text_length)
        
        # Try to end at sentence boundary
        sentence_match = re.search(r'[.!?]\s*', text[start:end][::-1])
        if sentence_match:
            end = end - sentence_match.start()
        else:
            # Fall back to last space
            space_pos = text.rfind(' ', start, end)
            if space_pos != -1 and space_pos > start:
                end = space_pos + 1
        
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        
        # Move start forward by (chunk_size - overlap)
        # This prevents infinite loop when overlap >= chunk size
        step = max_chunk_size - overlap
        if step <= 0:
            step = max_chunk_size // 2  # safety if overlap is too large
        
        start += step
        
        # Safety: if no progress, force advance
        if start >= end:
            start = end + 1
    
    return chunks

# Load your knowledge file (only once!)
print("Loading text file...")
with open('my_knowledge.txt', 'r', encoding='utf-8') as file:
    full_text = file.read()
print("Text loaded successfully. Length:", len(full_text), "characters")

# Chunk the text
print("Starting chunking...")
chunks = smart_chunk(full_text)
print("Chunking complete. Number of chunks:", len(chunks))
if chunks:
    print("First chunk sample:", chunks[0][:100] + "..." if len(chunks[0]) > 100 else chunks[0])
else:
    print("Warning: No chunks created!")

# Generate embeddings
print("Starting embeddings encoding... (this may take a few seconds)")
embeddings = model.encode(chunks, show_progress_bar=True, device='cpu')  # force CPU for now
print("Encoding finished! Embeddings shape:", embeddings.shape)

# Show preview
print("\n=== EMBEDDINGS PREVIEW ===")
for i, (chunk, vector) in enumerate(zip(chunks, embeddings), 1):
    print(f"Chunk {i} ({len(chunk)} chars):")
    print(chunk)
    print(f"Vector (first 6 of 384 numbers): {vector[:6]} ...")
    print("─" * 70)

# Save for later
np.save('my_knowledge_embeddings.npy', embeddings)
print("Saved embeddings to file: my_knowledge_embeddings.npy")