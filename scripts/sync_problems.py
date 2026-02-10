import json
import os
import datetime

# Configuration
DATA_FILE = "vondb.json"
OUTPUT_DIR = "content/problems"

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def slugify(text):
    return text.lower().replace(" ", "-").replace("'", "").replace("?", "")

def main():
    print(f"Reading from {DATA_FILE}...")
    
    # Mock data if file doesn't exist
    if not os.path.exists(DATA_FILE):
        print("Creating mock VonDB data...")
        mock_data = [
            {
                "id": "IMO-2025-P1",
                "title": "IMO 2025 Problem 1",
                "source": "IMO 2025",
                "tags": ["Algebra", "Inequalities"],
                "statement": "Let $a, b, c$ be real numbers...",
                "solution": "We proceed by AM-GM...",
                "date": "2025-07-15"
            },
            {
                "id": "USAMO-2024-P3",
                "title": "USAMO 2024 Problem 3",
                "source": "USAMO 2024",
                "tags": ["Number Theory"],
                "statement": "Find all integers $n$ such that...",
                "solution": "Consider modulo $p$...",
                "date": "2024-04-20"
            }
        ]
        with open(DATA_FILE, "w") as f:
            json.dump(mock_data, f, indent=4)
        data = mock_data
    else:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)

    ensure_dir(OUTPUT_DIR)
    
    # Create index file for problems
    index_content = """---
title: "Olympiad Problems"
summary: "A collection of problems I have solved, synced from VonDB."
---
Here you can find a collection of problems I have solved from various mathematical olympiads.
"""
    with open(os.path.join(OUTPUT_DIR, "_index.md"), "w") as f:
        f.write(index_content)

    # Generate problem files
    for problem in data:
        filename = f"{slugify(problem['title'])}.md"
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        content = f"""---
title: "{problem['title']}"
date: {problem['date']}
tags: {json.dumps(problem['tags'])}
source: "{problem['source']}"
---

## Problem
{problem['statement']}

## Solution
{problem['solution']}
"""
        with open(filepath, "w") as f:
            f.write(content)
        print(f"Generated {filename}")

if __name__ == "__main__":
    main()
