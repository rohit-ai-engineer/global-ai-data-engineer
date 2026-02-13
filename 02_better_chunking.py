# 02_better_chunking.py - Version 2.1
# Improved: better sentence-aware splitting, cleaner cuts, no mid-word breaks

import re

def smart_chunk(text, max_chunk_size=200, overlap=50):
    """
    Split text into overlapping chunks with preference for sentence boundaries.
    
    - Tries to end chunks at sentence ends (. ! ?)
    - Falls back to word boundaries if needed
    - Ensures no chunk exceeds max_chunk_size
    - Adds overlap for context preservation
    """
    chunks = []
    start = 0
    text_length = len(text)
    
    while start < text_length:
        # Define the ideal end position
        end = min(start + max_chunk_size, text_length)
        
        # Look for the last sentence end (. ! ?) in the window
        sentence_match = re.search(r'[.!?]\s*', text[start:end][::-1])
        if sentence_match:
            # Found a sentence end → adjust end to after it
            sentence_end_from_reverse = sentence_match.start()
            end = end - sentence_end_from_reverse
        
        # If no sentence end, fall back to last space (word boundary)
        else:
            space_pos = text.rfind(' ', start, end)
            if space_pos != -1 and space_pos > start:
                end = space_pos + 1  # include the space
        
        # Extract chunk
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        
        # Move forward with overlap (but don't go backward)
        start = end - overlap
        if start >= end:  # safety against bad overlap
            start = end
    
    return chunks


# === Main execution ===
with open('my_knowledge.txt', 'r', encoding='utf-8') as file:
    full_text = file.read()

print("=== FULL TEXT LOADED ===")
print(full_text)
print(f"\nTotal length: {len(full_text)} chars\n")

chunks = smart_chunk(full_text, max_chunk_size=200, overlap=60)

print("=== SMART CHUNKS (sentence-aware, overlap, size-controlled) ===")
for i, chunk in enumerate(chunks, 1):
    print(f"Chunk {i} (length: {len(chunk)} chars):")
    print(chunk)
    print("─" * 70)