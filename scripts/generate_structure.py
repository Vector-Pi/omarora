import os
import os
from datetime import date

# Define the site structure
site_structure = {
    "mathematics": {
        "title": "Mathematics",
        "weight": 10,
        "subpages": [
            "Beginners Guide to Advanced Mathematics",
            "Prerequisites for Mathematical Research",
            "Olympiad Problem-Solving & Resources",
            "My Math Projects",
            "Reading Notes & Papers"
        ]
    },
    "theoretical-physics": {
        "title": "Theoretical Physics",
        "weight": 11,
        "subpages": [
            "Starting with Theoretical Physics",
            "Math Prerequisites for QFT & GR",
            "My Research & Publications",
            "Open Problems I’m Exploring",
            "Lecture Notes & Summaries"
        ]
    },
    "astronomy": {
        "title": "Astronomy",
        "weight": 12,
        "subpages": [
            "Astronomy for Beginners",
            "Telescopes & Observation Guides",
            "Cosmology & Astrophysics Notes",
            "My Astronomy Projects",
            "Inspiring Papers & Books"
        ]
    },
    "quantitative-finance": {
        "title": "Quantitative Finance",
        "weight": 13,
        "subpages": [
            "Introduction to Quantitative Finance",
            "Math & Coding Prerequisites",
            "My Trading Projects",
            "Research in Market Microstructure",
            "Resources & Backtesting Tutorials"
        ]
    },
    "philosophy": {
        "title": "Philosophy",
        "weight": 14,
        "subpages": [
            "Schools of Thought",
            "Personal Philosophy Notes",
            "Great Thinkers & Essays",
            "Philosophy for STEM Students"
        ]
    },
    "history": {
        "title": "History",
        "weight": 15,
        "subpages": [
            "History of Mathematics & Physics",
            "Financial History & Market Evolution",
            "Biographies & Key Figures",
            "Book Reviews & Summaries",
            "Lessons from History"
        ]
    },
    "art-music": {
        "title": "Art & Music",
        "weight": 16,
        "subpages": [
            "Music I Create & Listen To",
            "Inspiration from Art & Science",
            "Creative Process & Tools",
            "Recommendations & Reviews"
        ]
    }
}

base_content_dir = "content"
today = date.today().strftime("%Y-%m-%d")

menu_items = []

# Existing static items (Home, Now, Blog, Handouts need to be preserved or re-added if we replace the whole list)
# We will generate the *new* part of the menu list.

for section_slug, data in site_structure.items():
    section_title = data["title"]
    section_dir = os.path.join(base_content_dir, section_slug)
    
    # 1. Create Directory
    os.makedirs(section_dir, exist_ok=True)
    
    # 2. Create _index.md (Section Main Page)
    index_path = os.path.join(section_dir, "_index.md")
    with open(index_path, "w") as f:
        f.write(f"---\n")
        f.write(f"title: \"{section_title}\"\n")
        f.write(f"date: {today}\n")
        f.write(f"summary: \"Resources and articles on {section_title}.\"\n")
        f.write(f"---\n\n")
        f.write(f"Welcome to the {section_title} section. Here you will find various articles and resources.\n")
    
    print(f"Created/Updated section: {section_slug}")

    # Add Parent Menu Item
    menu_items.append({
        "identifier": section_slug,
        "name": section_title,
        "url": f"/{section_slug}/",
        "weight": data["weight"]
    })

    # 3. Create Subpages
    for i, subpage_title in enumerate(data["subpages"]):
        # Create a slug from the title
        slug = subpage_title.lower().replace(" & ", "-").replace(" ", "-").replace(",", "").replace("'", "").replace("(", "").replace(")", "").replace(".", "")
        file_path = os.path.join(section_dir, f"{slug}.md")
        
        with open(file_path, "w") as f:
            f.write(f"---\n")
            f.write(f"title: \"{subpage_title}\"\n")
            f.write(f"date: {today}\n")
            f.write(f"parent: \"{section_title}\"\n")
            f.write(f"---\n\n")
            f.write(f"# {subpage_title}\n\n")
            f.write(f"Content for {subpage_title} goes here.\n")
        
        # Add Child Menu Item
        menu_items.append({
            "identifier": f"{section_slug}-{slug}",
            "name": subpage_title,
            "url": f"/{section_slug}/{slug}/",
            "parent": section_slug,
            "weight": i + 1
        })
        
        print(f"  - Created subpage: {subpage_title} -> {file_path}")

# Output the Menu YAML to a file for easy copying
with open("generated_menu.yaml", "w") as f:
    f.write("menu:\n  main:\n")
    # Add existing static items first (Home, Now, Blog, Handouts) - actually we'll just output the NEW list and User can merge
    # But to make it copy-pasteable, let's just dump the list items
    
    for item in menu_items:
        f.write(f"    - identifier: \"{item['identifier']}\"\n")
        f.write(f"      name: \"{item['name']}\"\n")
        f.write(f"      url: \"{item['url']}\"\n")
        if "parent" in item:
             f.write(f"      parent: \"{item['parent']}\"\n")
        f.write(f"      weight: {item['weight']}\n")

print("\nSuccess! Content generated. Menu configuration saved to 'generated_menu.yaml'.")
