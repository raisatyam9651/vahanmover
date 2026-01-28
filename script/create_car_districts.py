import os
import re
from bs4 import BeautifulSoup

# Change to the parent directory
os.chdir('..')

# Get all car state files
state_files = [f for f in os.listdir('.') if f.startswith('car-transport-') and f.endswith('.php') and f != 'car-transport-service.php']

print(f"Found {len(state_files)} car state files to process")

# Use a bike district file as template (since car district pages should be similar)
# We'll look for an existing bike district file to use as template
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
    
    # Find the "Car Transport By City" section
    # Look for h2 containing "By City"
    city_section = None
    for h2 in soup.find_all('h2'):
        if 'By City' in h2.get_text():
            city_section = h2.find_parent('div', class_='container')
            break
    
    if not city_section:
        print(f"  Warning: Could not find 'By City' section in {state_file}")
        continue
    
    # Find all list items with "Car transport in"
    districts = []
    for li in city_section.find_all('li'):
        span = li.find('span')
        if span:
            text = span.get_text(strip=True)
            if 'Car transport in' in text:
                # Extract district name
                district_name = text.replace('Car transport in', '').strip()
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
        filename = f"car-transport-{slug}.php"
        
        # Skip if already exists
        if os.path.exists(filename):
            print(f"  Skipping {district} (already exists)")
            continue
        
        # Create content by replacing "Anakapalli" with district name and "Bike" with "Car"
        new_content = template_content.replace("Anakapalli", district)
        new_content = new_content.replace("anakapalli", slug)
        
        # Replace "Bike" with "Car" and "bike" with "car" throughout
        new_content = new_content.replace("Bike transport", "Car transport")
        new_content = new_content.replace("bike transport", "car transport")
        new_content = new_content.replace("Bike shifting", "Car shifting")
        new_content = new_content.replace("bike shifting", "car shifting")
        new_content = new_content.replace("Bike relocation", "Car relocation")
        new_content = new_content.replace("bike relocation", "car relocation")
        new_content = new_content.replace("bike-transport-service.php", "car-transport-service.php")
        
        # Update meta tags and titles
        new_content = re.sub(
            r'<title>.*?</title>',
            f'<title>Car Transport in {district} | Safe Vehicle Shifting Services</title>',
            new_content,
            flags=re.DOTALL
        )
        
        # Update meta description
        new_content = re.sub(
            r'<meta name="description"[^>]*content="[^"]*"',
            f'<meta name="description" content="Professional car transport service in {district}. Safe, insured door-to-door car shifting with enclosed carriers and real-time tracking."',
            new_content
        )
        
        # Update keywords
        new_content = re.sub(
            r'<meta name="keywords"[^>]*content="[^"]*"',
            f'<meta name="keywords" content="car transport {district.lower()}, car shifting {district.lower()}, vehicle transport {district.lower()}, car carrier {district.lower()}, car relocation {district.lower()}"',
            new_content
        )
        
        # Write file
        with open(filename, "w", encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"  ✓ Created: {filename}")
        total_created += 1
        
        # Now link in state file
        # Find the span containing this district and replace with anchor
        escaped_district = re.escape(district)
        
        # Pattern to match the span (accounting for multi-line)
        pattern = r'<span\s+style="[^"]*">\s*Car\s+transport\s+in\s+' + escaped_district + r'\s*</span>'
        
        match = re.search(pattern, state_content, re.DOTALL | re.IGNORECASE)
        
        if match:
            # Create replacement anchor
            replacement = f'<a href="{filename}" style="color: var(--color-text-white); font-size: 1rem; text-decoration: none; transition: 0.3s;">Car transport in {district}</a>'
            
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
