import os
import re

def deduplicate_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return

    # Regex to find the Header "Car Transport By City"
    # Matches: Car Transport <span ...>By City</span>
    # Handling potential newlines and attributes
    # The snippet from view_file: Car Transport <span\n                        style="color: var(--color-primary);">By City</span>
    pattern = re.compile(r'Car Transport\s*<span[^>]*>\s*By City\s*</span>', re.IGNORECASE | re.DOTALL)
    
    matches = list(pattern.finditer(content))
    
    if len(matches) < 2:
        print(f"Skipping {filepath}: Found {len(matches)} matches (expected >= 2).")
        return

    print(f"Processing {filepath}: Found {len(matches)} matches. Removing the first one.")
    
    # We want to remove the section containing the FIRST match.
    first_match = matches[0]
    match_start = first_match.start()
    
    # Find the start of the section containing this match
    # We look backwards from match_start for "<section"
    # We take the LAST match of "<section" that appears before the title
    section_start_matches = list(re.finditer(r'<section', content[:match_start], re.IGNORECASE))
    
    if not section_start_matches:
        print(f"Could not find opening <section> for the first match in {filepath}.")
        return
        
    section_start_index = section_start_matches[-1].start()
    
    # Find the end of the section
    # We look forwards from match_start for "</section>"
    section_end_match = re.search(r'</section>', content[match_start:], re.IGNORECASE)
    if not section_end_match:
        print(f"Could not find closing </section> for the first match in {filepath}.")
        return
        
    # The end index is relative to match_start
    section_end_index = match_start + section_end_match.end()
    
    # Construct new content
    # Remove the section. 
    new_content = content[:section_start_index] + content[section_end_index:]
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {filepath}.")

def main():
    # Detect if running from root or script dir
    current_dir = os.getcwd()
    if os.path.basename(current_dir) == 'script':
         directory = "../"
    else:
         directory = "./"
         
    print(f"Scanning directory: {os.path.abspath(directory)}")
    
    count = 0
    for filename in os.listdir(directory):
        if filename.startswith('car-transport-') and filename.endswith('.php'):
            # Skip the main service page as it shouldn't have the duplicate district section
            # (It has "Pan India Car Transport Coverage" instead)
            if filename == 'car-transport-service.php':
                continue
            
            deduplicate_file(os.path.join(directory, filename))
            count += 1
            
    print(f"Scanned {count} files.")

if __name__ == "__main__":
    main()
