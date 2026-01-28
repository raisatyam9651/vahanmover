import os
import re

# Mapping: "City Name" -> "Target PHP File"
CITY_PAGE_MAP = {
    "Mumbai": "car-transport-maharashtra.php",
    "Bangalore": "car-transport-karnataka.php",
    "Hyderabad": "car-transport-telangana.php",
    "Chennai": "car-transport-tamil-nadu.php",
    "Kolkata": "car-transport-west-bengal.php",
    "Pune": "car-transport-maharashtra.php",
    "Ahmedabad": "car-transport-gujarat.php",
    "Jaipur": "car-transport-rajasthan.php",
    "Lucknow": "car-transport-uttar-pradesh.php",
    "Surat": "car-transport-gujarat.php",
    "Indore": "car-transport-madhya-pradesh.php",
    "Patna": "car-transport-bihar.php",
    "Nagpur": "car-transport-maharashtra.php",
    "Bhopal": "car-transport-madhya-pradesh.php",
    "Vadodara": "car-transport-gujarat.php",
    "Ludhiana": "car-transport-punjab.php",
    "Kochi": "car-transport-kerala.php",
    "Visakhapatnam": "car-transport-andhra-pradesh.php",
    "Agra": "car-transport-uttar-pradesh.php",
    "Nashik": "car-transport-maharashtra.php",
    "Raipur": "car-transport-chhattisgarh.php",
    "Bhubaneswar": "car-transport-odisha.php"
    # Delhi and Chandigarh are skipped as no dedicated page exists
}

def update_links(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return

    original_content = content
    
    for city, target_file in CITY_PAGE_MAP.items():
        # Regex explanation:
        # We look for: <a href="#" ...>Car Transport in City</a>
        # We want to be careful not to break the tag structure.
        # We match: (<a\s+href=")(#)(".*?Car Transport in\s+)(City)(</a>)
        # Replacing group 2 (#) with the target file.
        
        # Simpler approach: Replace the specific string sequence
        # We assume the structure is consistent: <a href="#" style="...">Car Transport in [City]</a>
        # We can search for `href="#"` followed eventually by `Car Transport in [City]` inside the same tag?
        # Actually, the file content shows:
        # <a href="#"\n style="...">Car\n Transport in Delhi</a>
        # The newlines might be tricky.
        
        # Let's use a regex that matches the href="#" attribute and the city text, allowing for attributes and whitespace.
        # Pattern:
        # <a \s+ href="#" ( [^>]*? ) > \s* Car \s+ Transport \s+ in \s+ CITY \s* </a>
        
        pattern = re.compile(
            r'(<a\s+href=")(#)("[^>]*>\s*Car\s+Transport\s+in\s+' + re.escape(city) + r'\s*</a>)',
            re.IGNORECASE | re.DOTALL
        )
        
        # Replacement function to insert the target file
        def replace_match(match):
            return match.group(1) + target_file + match.group(3)
            
        content = pattern.sub(replace_match, content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated links in {filepath}")
    else:
        # print(f"No changes in {filepath}")
        pass

def main():
    current_dir = os.getcwd()
    if os.path.basename(current_dir) == 'script':
         directory = "../"
    else:
         directory = "./"
         
    print(f"Scanning directory: {os.path.abspath(directory)}")
    
    count = 0
    for filename in os.listdir(directory):
        if filename.startswith('car-transport-') and filename.endswith('.php'):
            update_links(os.path.join(directory, filename))
            count += 1
            
    print(f"Processed {count} files.")

if __name__ == "__main__":
    main()
