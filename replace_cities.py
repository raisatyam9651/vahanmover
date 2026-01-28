import re

# Read the file
with open('bike-transport-andhra-pradesh.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the AP cities in order
cities = [
    "Anakapalli", "Anantapur", "Alluri Sitarama Raju", "Annamayya", "Bapatla", "Chittoor", "Dr. B. R. Ambedkar Konaseema",
    "East Godavari", "Eluru", "Guntur", "Kakinada", "Krishna", "Kurnool", "Nandyal",
    "Nellore", "NTR", "Palnadu", "Parvathipuram Manyam", "Prakasam", "Srikakulam", "Sri Sathya Sai",
    "Tirupati", "Visakhapatnam", "Vizianagaram", "West Godavari", "YSR Kadapa"
]

# Find the section between <!-- Column 1 --> and </div> before <!-- Footer -->
pattern = r'(<!-- Column 1 -->.*?)</div>\s*</div>\s*</div>\s*</section>\s*<!-- Footer -->'
match = re.search(pattern, content, re.DOTALL)

if match:
    # Create new city list HTML
    cities_html = []
    cities_per_column = 7
    
    for col in range(4):
        start_idx = col * cities_per_column
        end_idx = min(start_idx + cities_per_column, len(cities))
        col_cities = cities[start_idx:end_idx]
        
        ul_items = []
        for i, city in enumerate(col_cities):
            is_last = (i == len(col_cities) - 1)
            border_style = "" if is_last else " border-bottom: 1px solid rgba(255,255,255,0.05);"
            
            item = f'''                        <li style="padding: 10px 0;{border_style} display: flex; align-items: flex-start; gap: 10px;">
                            <i class="fa-solid fa-circle-check" style="color: var(--color-primary); font-size: 0.8rem; margin-top: 5px; flex-shrink: 0;"></i>
                            <span style="color: var(--color-text-white); font-size: 1rem;">Bike transport in {city}</span>
                        </li>'''
            ul_items.append(item)
        
        col_html = f'''
                    <!-- Column {col + 1} -->
                    <ul style="list-style: none; padding: 0;">
{chr(10).join(ul_items)}
                    </ul>'''
        cities_html.append(col_html)
    
    replacement = f'''<!-- Column 1 -->{chr(10).join(cities_html)}

                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->'''
    
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Write back
    with open('bike-transport-andhra-pradesh.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Successfully replaced states with Andhra Pradesh cities!")
else:
    print("Pattern not found!")
