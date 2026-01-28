import os
import re
from bs4 import BeautifulSoup

# Change to the parent directory
os.chdir('..')

print("Comprehensive Analysis of All Car Transport Pages")
print(f"{'='*80}\n")

# Get ALL car transport files
all_car_files = [f for f in os.listdir('.') if f.startswith('car-transport-') and f.endswith('.php')]

# Separate state pages from district pages
state_pages = [
    'car-transport-andhra-pradesh.php', 'car-transport-arunachal-pradesh.php',
    'car-transport-assam.php', 'car-transport-bihar.php', 'car-transport-chhattisgarh.php',
    'car-transport-goa.php', 'car-transport-gujarat.php', 'car-transport-haryana.php',
    'car-transport-himachal-pradesh.php', 'car-transport-jharkhand.php',
    'car-transport-karnataka.php', 'car-transport-kerala.php', 'car-transport-madhya-pradesh.php',
    'car-transport-maharashtra.php', 'car-transport-manipur.php', 'car-transport-meghalaya.php',
    'car-transport-mizoram.php', 'car-transport-nagaland.php', 'car-transport-odisha.php',
    'car-transport-punjab.php', 'car-transport-rajasthan.php', 'car-transport-sikkim.php',
    'car-transport-tamil-nadu.php', 'car-transport-telangana.php', 'car-transport-tripura.php',
    'car-transport-uttar-pradesh.php', 'car-transport-uttarakhand.php', 'car-transport-west-bengal.php'
]

district_pages = [f for f in all_car_files if f not in state_pages and f != 'car-transport-service.php']

print(f"Total car transport files: {len(all_car_files)}")
print(f"State pages: {len(state_pages)}")
print(f"District pages: {len(district_pages)}")
print(f"Service page: 1")
print(f"\n{'='*80}\n")

# Check all state pages for broken links
print("CHECKING STATE PAGES FOR BROKEN LINKS:")
print(f"{'='*80}\n")

total_links_checked = 0
total_broken = 0
broken_links = []

for state_file in sorted(state_pages):
    if not os.path.exists(state_file):
        print(f"⚠️  State file not found: {state_file}")
        continue
    
    # Read state file
    with open(state_file, "r", encoding='utf-8') as f:
        state_content = f.read()
    
    # Parse HTML to find all links
    soup = BeautifulSoup(state_content, 'html.parser')
    
    # Find the "Car Transport By City" section
    city_section = None
    for h2 in soup.find_all('h2'):
        if 'By City' in h2.get_text():
            city_section = h2.find_parent('div', class_='container')
            break
    
    if not city_section:
        print(f"⚠️  {state_file}: No 'By City' section found")
        continue
    
    # Find all links in the city section
    links = city_section.find_all('a', href=True)
    
    state_broken = []
    
    for link in links:
        href = link.get('href')
        if href and href.startswith('car-transport-') and href.endswith('.php'):
            total_links_checked += 1
            # Check if file exists
            if not os.path.exists(href):
                district_name = link.get_text().replace('Car transport in', '').strip()
                state_broken.append({
                    'file': href,
                    'district': district_name
                })
                total_broken += 1
    
    if state_broken:
        print(f"❌ {state_file}: {len(state_broken)} broken link(s)")
        for item in state_broken:
            print(f"   Missing: {item['file']} → {item['district']}")
            broken_links.append({
                'state': state_file,
                'file': item['file'],
                'district': item['district']
            })
    else:
        link_count = len([l for l in links if l.get('href', '').startswith('car-transport-')])
        print(f"✅ {state_file}: All {link_count} links valid")

print(f"\n{'='*80}")
print(f"FINAL SUMMARY")
print(f"{'='*80}")
print(f"State pages checked: {len(state_pages)}")
print(f"Total district links checked: {total_links_checked}")
print(f"Broken links found: {total_broken}")
print(f"District pages available: {len(district_pages)}")
print(f"{'='*80}\n")

if broken_links:
    print("BROKEN LINKS DETAILS:")
    print(f"{'='*80}")
    for link in broken_links:
        print(f"State: {link['state']}")
        print(f"  Missing file: {link['file']}")
        print(f"  District: {link['district']}\n")
    
    # Save for creating missing pages
    with open('script/broken_links.txt', 'w', encoding='utf-8') as f:
        for link in broken_links:
            f.write(f"{link['file']}|{link['district']}|{link['state']}\n")
    print(f"✓ Broken links saved to script/broken_links.txt")
else:
    print("✅ NO BROKEN LINKS FOUND! All state pages have valid district links.")
