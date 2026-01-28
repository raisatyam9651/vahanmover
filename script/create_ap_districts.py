import os
import re

districts = [
    "Bapatla",
    "Chittoor",
    "Dr. B. R. Ambedkar Konaseema",
    "East Godavari",
    "Eluru",
    "Guntur",
    "Kakinada",
    "Krishna",
    "Kurnool",
    "Nandyal",
    "Nellore",
    "NTR",
    "Palnadu",
    "Parvathipuram Manyam",
    "Prakasam",
    "Srikakulam",
    "Sri Sathya Sai",
    "Tirupati",
    "Visakhapatnam",
    "Vizianagaram",
    "West Godavari",
    "YSR Kadapa"
]

template_file = "bike-transport-anakapalli.php"
state_file = "bike-transport-andhra-pradesh.php"

# Ensure we are in the right directory
if not os.path.exists(template_file):
    print(f"Error: Template file {template_file} not found.")
    exit(1)

with open(template_file, "r") as f:
    template_content = f.read()

with open(state_file, "r") as f:
    state_content = f.read()

for district in districts:
    print(f"Processing {district}...")
    
    # 1. Generate Filename
    # specialized handling for names with dots or special formatting if needed, 
    # but general slugify should work: lowercase, replace spaces/dots with hyphens, remove multiple hyphens.
    slug = district.lower().replace(".", "").replace(" ", "-")
    slug = re.sub(r'-+', '-', slug) # collapse multiple dashes
    filename = f"bike-transport-{slug}.php"
    
    # 2. Create Content
    # Naive replacement of "Anakapalli" with "District Name"
    # The template has "Anakapalli" in various places. 
    # We should match case if possible, but simplest is usually strictly replacing the proper noun.
    
    new_content = template_content.replace("Anakapalli", district)
    
    # Write new file
    with open(filename, "w") as f:
        f.write(new_content)
    print(f"  Created {filename}")
    
    # 3. Link in State Page
    # We look for: <span ...>Bike transport in {district}</span>
    # And replace with: <a href="{filename}" ...>Bike transport in {district}</a>
    
    # The search pattern needs to be robust to whitespace/newlines as we saw before.
    # Pattern: <span style="[^"]*">Bike transport in\s+DISTRICT</span>
    
    # Escape district for regex (e.g. dots in Dr. B. R.)
    escaped_district = re.escape(district)
    
    # Regex to find the span. Note: \s+ matches spaces/newlines between words if they were split.
    # The original file has "Bike transport in [District]" inside a span. 
    # The span tag itself has style attributes.
    
    pattern = r'(<span style="[^"]*">)(\s*Bike transport in\s+' + escaped_district + r'\s*)(</span>)'
    
    match = re.search(pattern, state_content, re.DOTALL | re.IGNORECASE)
    
    if match:
        # We found it. Now construct replacement.
        # We want to keep the style from the span but apply it to the anchor, 
        # PLUS add text-decoration: none and maybe transition.
        # The original span style: color: var(--color-text-white); font-size: 1rem;
        # We should change it to match the already linked items:
        # style="color: var(--color-text-white); font-size: 1rem; text-decoration: none; transition: 0.3s;"
        
        replacement_style = 'style="color: var(--color-text-white); font-size: 1rem; text-decoration: none; transition: 0.3s;"'
        
        # New tag
        new_tag = f'<a href="{filename}" {replacement_style}>'
        end_tag = '</a>'
        
        # The content inside the tag (e.g. "Bike transport in Chittoor")
        inner_text = match.group(2)
        
        # Perform replacement in the big string
        # We need to replace the correctly matched group.
        # match.group(0) is the whole <span ...>...</span> block
        
        original_block = match.group(0)
        new_block = f'{new_tag}{inner_text}{end_tag}'
        
        state_content = state_content.replace(original_block, new_block)
        print(f"  Linked in {state_file}")
    else:
        print(f"  Warning: Could not find entry for '{district}' in {state_file}")

# Save the updated state file
with open(state_file, "w") as f:
    f.write(state_content)

print("Batch creation completed.")
