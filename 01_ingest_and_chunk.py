# This is a comment. Python ignores lines starting with #
# We are writing a simple data ingestion script for AI

# Step 1: Tell Python we want to work with files
with open('my_knowledge.txt', 'r', encoding='utf-8') as file:
    text = file.read()  # Read the entire file into a variable called "text"

# Step 2: Print what we read (so we can see it worked)
print("=== RAW TEXT LOADED ===")
print(text)
print("\n=== END OF RAW TEXT ===\n")

# Step 3: Chunk the text — split into small pieces (this is CRITICAL for RAG)
chunks = text.split('.')  # Simple split on periods for now

# Step 4: Clean and show the chunks
print("=== CHUNKS CREATED FOR AI ===")
for i, chunk in enumerate(chunks):
    clean_chunk = chunk.strip()  # Remove extra spaces
    if clean_chunk:  # Only show non-empty chunks
        print(f"Chunk {i+1}: {clean_chunk}")