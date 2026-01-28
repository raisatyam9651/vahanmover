import re

def link_bike_states():
    file_path = 'bike-transport-service.php'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Mapping of State Name to Slug
    # Derived from file listing:
    # bike-transport-andhra-pradesh.php
    # etc.
    
    # We will search for: <span ...>Bike transport in {State}</span>
    # And replace with: <a href="bike-transport-{slug}.php" ...>Bike transport in {State}</a>
    
    # Regex to capture the span and the state name
    # <span style="color: var(--color-text-white); font-size: 1rem;">Bike transport in Andhra\n                                Pradesh</span>
    # Note the newlines and spaces in the file content we saw earlier.
    
    # Pattern:
    # <span style="color: var(--color-text-white); font-size: 1rem;">Bike transport in (.*?)</span>
    
    # We need to be careful with matching.
    
    # Let's define the slug mapping logic.
    # Usually it's lowercase, spaces to hyphens.
    
    def replace_match(match):
        full_match = match.group(0)
        state_text = match.group(1) # e.g. "Andhra\n                                Pradesh"
        
        # Clean up state name for slug generation
        clean_state = re.sub(r'\s+', ' ', state_text).strip()
        slug = clean_state.lower().replace(' ', '-')
        
        # Construct the link
        # Preserving the original text formatting (newlines and indentation) inside the anchor text if possible, 
        # but clean state name is probably better for display? 
        # The original code had specific formatting.
        # Let's just use the captured state_text in the link text to minimize visual disruption,
        # or cleanup the link text. Let's cleanup the link text to be single line?
        # The file has heavy indentation.
        
        # <a href="bike-transport-{slug}.php" style="color: var(--color-text-white); font-size: 1rem; text-decoration: none; transition: 0.3s;">Bike transport in {state_text}</a>
        
        # Note: The 'Bike transport in ' part is outside the capturing group in my proposed regex above?
        # Let's look at the regex again.
        
        return f'<a href="bike-transport-{slug}.php" style="color: var(--color-text-white); font-size: 1rem; text-decoration: none; transition: 0.3s;">Bike transport in {state_text}</a>'

    # The pattern in the file:
    # <span style="color: var(--color-text-white); font-size: 1rem;">Bike transport in Andhra
    #                                 Pradesh</span>
    
    # Regex:
    # <span\s+style="color:\s*var\(--color-text-white\);\s*font-size:\s*1rem;">Bike transport in\s+(.*?)</span>
    
    pattern = re.compile(r'<span\s+style="color:\s*var\(--color-text-white\);\s*font-size:\s*1rem;">Bike transport in\s+(.*?)</span>', re.DOTALL)
    
    new_content = pattern.sub(replace_match, content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
    else:
        print("No changes made. Pattern might not have matched.")

if __name__ == "__main__":
    link_bike_states()
