import os
import shutil

# List of Noida Locations (Sectors and Areas)
locations = [
    "Sector 1", "Sector 2", "Sector 3", "Sector 4", "Sector 5", "Sector 6",
    "Sector 10", "Sector 11", "Sector 12", "Sector 14", "Sector 15", "Sector 16", "Sector 16A", "Sector 18",
    "Sector 19", "Sector 20", "Sector 21", "Sector 22", "Sector 23", "Sector 24", "Sector 25", "Sector 26",
    "Sector 27", "Sector 28", "Sector 29", "Sector 30", "Sector 31", "Sector 33", "Sector 34", "Sector 35",
    "Sector 36", "Sector 37", "Sector 39", "Sector 40", "Sector 41", "Sector 42", "Sector 43", "Sector 44",
    "Sector 45", "Sector 46", "Sector 47", "Sector 48", "Sector 49", "Sector 50", "Sector 51", "Sector 52",
    "Sector 53", "Sector 55", "Sector 56", "Sector 57", "Sector 58", "Sector 59", "Sector 60", "Sector 61",
    "Sector 62", "Sector 63", "Sector 64", "Sector 65", "Sector 66", "Sector 67", "Sector 70", "Sector 71",
    "Sector 72", "Sector 73", "Sector 74", "Sector 75", "Sector 76", "Sector 77", "Sector 78", "Sector 79",
    "Sector 80", "Sector 81", "Sector 82", "Sector 93", "Sector 100", "Sector 104", "Sector 105", "Sector 108",
    "Sector 110", "Sector 128", "Sector 135", "Sector 137", "Sector 143", "Sector 144", "Sector 150", 
    "Sector 151", "Sector 168",
    "Noida Extension", "Greater Noida West", "Gaur City"
]

def slugify(text):
    return text.lower().replace(" ", "-")

def generate_subpages(service_type, template_file, locations):
    with open(template_file, 'r', encoding='utf-8') as f:
        template_content = f.read()

    links_html = []
    
    # Logic to insert columns - getting ready for 4 columns
    total_locs = len(locations)
    per_col = (total_locs + 3) // 4
    
    columns = [[], [], [], []]

    for i, location in enumerate(locations):
        full_location_name = f"{location} Noida"
        if "Noida" in location: # Avoid "Noida Extension Noida"
             full_location_name = location
        
        slug = slugify(full_location_name)
        filename = f"{service_type}-transport-{slug}.php"
        
        # Determine title service name
        service_name_cap = "Bike" if service_type == "bike" else "Car"
        
        # Replace content
        new_content = template_content.replace(f"{service_name_cap} Transport in Noida", f"{service_name_cap} Transport in {full_location_name}")
        new_content = new_content.replace(f"{service_type} transport service in Noida", f"{service_type} transport service in {full_location_name}")
        
        # Meta tag updates - simple search and replace might be risky if we don't match exactly.
        # But since we used "Noida" in the template, we can proceed with care.
        # We need to replace "Noida" with "full_location_name" in specific contexts to avoid replacing included file paths etc.
        # However, the template is specifically 'bike-transport-noida.php'.
        
        # A safer way: replace the specific Title and Description strings we know exist.
        
        # Title
        search_title = f"<title>{service_name_cap} Transport in Noida | Safe"
        replace_title = f"<title>{service_name_cap} Transport in {full_location_name} | Safe"
        new_content = new_content.replace(search_title, replace_title)
        
        # Description
        search_desc = f"transport service in Noida. Safe"
        replace_desc = f"transport service in {full_location_name}. Safe"
        new_content = new_content.replace(search_desc, replace_desc)
        
        # Keywords
        search_kw = f"{service_type} transport noida, {service_type} shifting noida"
        replace_kw = f"{service_type} transport {full_location_name.lower()}, {service_type} shifting {full_location_name.lower()}"
        new_content = new_content.replace(search_kw, replace_kw)
        
        # H1
        # H1 replacement
        search_h1_span = """<span
                        style="background: linear-gradient(to right, var(--color-primary), var(--color-secondary)); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;">Noida</span>"""
        replace_h1_span = f"""<span
                        style="background: linear-gradient(to right, var(--color-primary), var(--color-secondary)); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;">{full_location_name}</span>"""
        new_content = new_content.replace(search_h1_span, replace_h1_span)

        # Breadcrumbs or text content could also be updated
        new_content = new_content.replace("Home </a>&nbsp; / &nbsp; Noida", f"Home </a>&nbsp; / &nbsp; <a href=\"{service_type}-transport-noida.php\">Noida</a> &nbsp; / &nbsp; {full_location_name}")
        
        
        # Write the new file
        output_path = os.path.join(os.path.dirname(template_file), filename)
        with open(output_path, 'w', encoding='utf-8') as out_f:
            out_f.write(new_content)
            
        print(f"Created: {filename}")
        
        # Generate link HTML
        link_html = f"""                        <li
                            style="padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; align-items: flex-start; gap: 10px;">
                            <i class="fa-solid fa-circle-check"
                                style="color: var(--color-primary); font-size: 0.8rem; margin-top: 5px; flex-shrink: 0;"></i>
                            <a href="{filename.replace('.php', '')}"
                                style="color: var(--color-text-white); font-size: 1rem; text-decoration: none; transition: 0.3s;">{service_name_cap}
                                transport in {full_location_name}</a>
                        </li>"""
        columns[i // per_col].append(link_html)

    # Output the columns HTML to a file for easy copying
    with open(f"script/{service_type}_noida_links.html", "w", encoding='utf-8') as f:
         for col_idx, col in enumerate(columns):
             f.write(f"\n\n<!-- Column {col_idx + 1} -->\n")
             f.write('<ul style="list-style: none; padding: 0;">\n')
             f.write('\n'.join(col))
             f.write('\n</ul>')

if __name__ == "__main__":
    base_dir = "/Users/bp/Desktop/Shifter"
    
    # Generate Bike Pages
    print("Generating Bike Pages...")
    generate_subpages("bike", os.path.join(base_dir, "bike-transport-noida.php"), locations)
    
    # Generate Car Pages
    print("\nGenerating Car Pages...")
    generate_subpages("car", os.path.join(base_dir, "car-transport-noida.php"), locations)
