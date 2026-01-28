import os
import re
from bs4 import BeautifulSoup

# Get all state files
state_files = [f for f in os.listdir('.') if f.startswith('bike-transport-') and f.endswith('.php') and f != 'bike-transport-service.php']

# Exclude district files we already created
exclude_patterns = [
    'anakapalli', 'anantapur', 'alluri', 'annamayya', 'bapatla', 'chittoor',
    'dr-b', 'east', 'eluru', 'guntur', 'kakinada', 'krishna', 'kurnool',
    'nandyal', 'nellore', 'ntr', 'palnadu', 'parvathipuram', 'prakasam',
    'srikakulam', 'sri-sathya', 'tirupati', 'visakhapatnam', 'vizianagaram',
    'west', 'ysr'
]

state_files = [f for f in state_files if not any(pattern in f for pattern in exclude_patterns)]

print(f"Found {len(state_files)} state files to process")

# Use Anakapalli as template
template_file = "bike-transport-anakapalli.php"
if not os.path.exists(template_file):
    print(f"Error: Template file {template_file} not found.")
    exit(1)

with open(template_file, "r", encoding='utf-8') as f:
    template_content = f.read()

total_created = 0
total_linked = 0

for state_file in sorted(state_files):
    print(f"\n{'='*60}")
    print(f"Processing: {state_file}")
    print(f"{'='*60}")
    
    # Read state file
    with open(state_file, "r", encoding='utf-8') as f:
        state_content = f.read()
    
    # Parse HTML to find district list
    soup = BeautifulSoup(state_content, 'html.parser')
    
    # Find the "Bike Transport By City" section
    # Look for h2 containing "By City"
    city_section = None
    for h2 in soup.find_all('h2'):
        if 'By City' in h2.get_text():
            city_section = h2.find_parent('div', class_='container')
            break
    
    if not city_section:
        print(f"  Warning: Could not find 'By City' section in {state_file}")
        continue
    
    # Find all list items with "Bike transport in"
    districts = []
    for li in city_section.find_all('li'):
        text = li.get_text(strip=True)
        if 'Bike transport in' in text:
            # Extract district name
            district_name = text.replace('Bike transport in', '').strip()
            districts.append(district_name)
    
    print(f"  Found {len(districts)} districts")
    
    if len(districts) == 0:
        print(f"  Warning: No districts found in {state_file}")
        continue
    
    # Create pages for each district
    for district in districts:
        # Generate filename
        slug = district.lower().replace(".", "").replace(" ", "-")
        slug = re.sub(r'-+', '-', slug)
        filename = f"bike-transport-{slug}.php"
        
        # Skip if already exists
        if os.path.exists(filename):
            print(f"  Skipping {district} (already exists)")
            continue
        
        # Create content by replacing "Anakapalli" with district name
        new_content = template_content.replace("Anakapalli", district)
        new_content = new_content.replace("anakapalli", slug)
        
        # Write file
        with open(filename, "w", encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"  ✓ Created: {filename}")
        total_created += 1
        
        # Now link in state file
        # Find the span containing this district and replace with anchor
        escaped_district = re.escape(district)
        
        # Pattern to match the span (accounting for multi-line)
        pattern = r'<span\s+style="[^"]*">\s*Bike\s+transport\s+in\s+' + escaped_district + r'\s*</span>'
        
        match = re.search(pattern, state_content, re.DOTALL | re.IGNORECASE)
        
        if match:
            # Create replacement anchor
            replacement = f'<a href="{filename}" style="color: var(--color-text-white); font-size: 1rem; text-decoration: none; transition: 0.3s;">Bike transport in {district}</a>'
            
            # Replace in content
            state_content = state_content.replace(match.group(0), replacement)
            print(f"  ✓ Linked: {district}")
            total_linked += 1
        else:
            print(f"  ⚠ Could not link: {district} (pattern not found)")
    
    # Save updated state file
    with open(state_file, "w", encoding='utf-8') as f:
        f.write(state_content)
    
    print(f"  Updated: {state_file}")

print(f"\n{'='*60}")
print(f"SUMMARY")
print(f"{'='*60}")
print(f"Total pages created: {total_created}")
print(f"Total links updated: {total_linked}")
print(f"States processed: {len(state_files)}")
print(f"{'='*60}")
