import os

def apply_links(target_file, source_file):
    with open(source_file, 'r') as f:
        link_content = f.read()

    with open(target_file, 'r') as f:
        target_content = f.read()

    # Define the block to replace
    # We will replace the entire grid content inner HTML
    start_marker = '<!-- Column 1 -->'
    end_marker = '<!-- Column 4 -->'
    
    # Verify markers exist
    if start_marker not in target_content or end_marker not in target_content:
        print(f"Markers not found in {target_file}")
        return

    # Find the end of the 4th column UL
    # The structure is <!-- Column 4 --> ... </ul>
    # We can search for the closing </ul> after the end_marker
    
    start_idx = target_content.find(start_marker)
    
    # Find the pos of '</ul>' after '<!-- Column 4 -->'
    col4_idx = target_content.find(end_marker)
    ul_end_idx = target_content.find('</ul>', col4_idx) + 5 # include </ul>
    
    if ul_end_idx == 4: # -1 + 5
        print(f"Could not find end of Column 4 in {target_file}")
        return

    # Construct new content we'll just use the content from source_file
    # Note: source_file content has <!-- Column 1 --> at the top
    
    new_content = target_content[:start_idx] + link_content + target_content[ul_end_idx:]
    
    with open(target_file, 'w') as f:
        f.write(new_content)
    print(f"Updated {target_file}")

if __name__ == "__main__":
    base_dir = "/Users/bp/Desktop/Shifter"
    
    print("Updating Bike Page...")
    apply_links(os.path.join(base_dir, "bike-transport-noida.php"), os.path.join(base_dir, "script/bike_noida_links.html"))
    
    print("Updating Car Page...")
    apply_links(os.path.join(base_dir, "car-transport-noida.php"), os.path.join(base_dir, "script/car_noida_links.html"))
