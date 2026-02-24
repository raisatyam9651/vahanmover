import os
import re

districts = ['Agra', 'Aligarh', 'Ambedkar Nagar', 'Amethi', 'Amroha', 'Auraiya', 'Ayodhya', 'Azamgarh', 'Baghpat', 'Bahraich', 'Ballia', 'Balrampur', 'Banda', 'Barabanki', 'Bareilly', 'Basti', 'Bhadohi', 'Bijnor', 'Budaun', 'Bulandshahr', 'Chandauli', 'Chitrakoot', 'Deoria', 'Etah', 'Etawah', 'Farrukhabad', 'Fatehpur', 'Firozabad', 'Gautam Buddha Nagar', 'Ghaziabad', 'Ghazipur', 'Gonda', 'Gorakhpur', 'Hamirpur', 'Hapur', 'Hardoi', 'Hathras', 'Jalaun', 'Jaunpur', 'Jhansi', 'Kannauj', 'Kanpur Dehat', 'Kanpur Nagar', 'Kasganj', 'Kaushambi', 'Kushinagar', 'Lakhimpur Kheri', 'Lalitpur', 'Lucknow', 'Maharajganj', 'Mahoba', 'Mainpuri', 'Mathura', 'Mau', 'Meerut', 'Mirzapur', 'Moradabad', 'Muzaffarnagar', 'Pilibhit', 'Pratapgarh', 'Prayagraj', 'Raebareli', 'Rampur', 'Saharanpur', 'Sambhal', 'Sant Kabir Nagar', 'Shahjahanpur', 'Shamli', 'Shravasti', 'Siddharthnagar', 'Sitapur', 'Sonbhadra', 'Sultanpur', 'Unnao', 'Varanasi']

states = {
    "Andhra Pradesh": ("15.9129", "79.7400"),
    "Arunachal Pradesh": ("28.2180", "94.7278"),
    "Assam": ("26.2006", "92.9376"),
    "Bihar": ("25.0961", "85.3131"),
    "Chhattisgarh": ("21.2787", "81.8661"),
    "Goa": ("15.2993", "74.1240"),
    "Gujarat": ("22.2587", "71.1924"),
    "Haryana": ("29.0588", "76.0856"),
    "Himachal Pradesh": ("31.1048", "77.1665"),
    "Jharkhand": ("23.6102", "85.2799"),
    "Karnataka": ("15.3173", "75.7139"),
    "Kerala": ("10.8505", "76.2711"),
    "Madhya Pradesh": ("22.9734", "78.6569"),
    "Maharashtra": ("19.7515", "75.7139"),
    "Manipur": ("24.6637", "93.9063"),
    "Meghalaya": ("25.4670", "91.3662"),
    "Mizoram": ("23.1645", "92.9376"),
    "Nagaland": ("26.1584", "94.5624"),
    "Odisha": ("20.9517", "85.0985"),
    "Punjab": ("31.1471", "75.3412"),
    "Rajasthan": ("27.0238", "74.2179"),
    "Sikkim": ("27.5330", "88.5122"),
    "Tamil Nadu": ("11.1271", "78.6569"),
    "Telangana": ("18.1124", "79.0193"),
    "Tripura": ("23.9408", "91.9882"),
    "Uttar Pradesh": ("26.8467", "80.9462"),
    "Uttarakhand": ("30.0668", "79.0193"),
    "West Bengal": ("22.9868", "87.8550"),
    "Andaman and Nicobar Islands": ("11.7401", "92.6586"),
    "Chandigarh": ("30.7333", "76.7794"),
    "Dadra and Nagar Haveli and Daman and Diu": ("20.1809", "73.0169"),
    "Delhi": ("28.7041", "77.1025"),
    "Jammu and Kashmir": ("33.7782", "76.5762"),
    "Ladakh": ("34.1526", "77.5771"),
    "Lakshadweep": ("10.5667", "72.6417"),
    "Puducherry": ("11.9416", "79.8083")
}

def to_slug(name):
    return name.lower().replace(" ", "-").replace("&", "and")

def create_links_section(service_type, district):
    # Create HTML block for internal links
    links_html = f'''
    <!-- State Links Section -->
    <section style="padding: 40px 0; background: rgba(255,255,255,0.02); margin-top: 40px;">
        <div class="container">
            <h3 style="font-size: 2rem; margin-bottom: 20px; font-weight: 700; text-align: center;">Other <span style="color: var(--color-primary);">Locations We Serve</span></h3>
            <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 15px;">
'''
    district_slug = to_slug(district)
    for state in sorted(states.keys()):
        slug = to_slug(state)
        url = f"{service_type}-transport-{district_slug}-to-{slug}"
        # using absolute path basically matching the structure
        links_html += f'                <a href="{url}" style="padding: 10px 20px; background: rgba(6, 182, 212, 0.1); border: 1px solid rgba(6, 182, 212, 0.3); border-radius: 30px; color: var(--color-text-white); text-decoration: none; font-size: 0.95rem; transition: background 0.3s;">{district} to {state}</a>\n'
    
    links_html += '''            </div>
        </div>
    </section>
'''
    return links_html

def process_file_for_district(template_path, service_type, district):
    
    district_slug = to_slug(district)

    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()

    links_section = create_links_section(service_type, district)

    for state, (lat, lng) in states.items():
        slug = to_slug(state)
        new_filename = f"{service_type}-transport-{district_slug}-to-{slug}.php"
        
        # We only generate for states that aren't the same. E.g we can generate UP to UP but we already generate others.
        c = content

        # Titles and Meta
        c = c.replace(f"Bike Transport in Gorakhpur", f"Bike Transport from {district} to {state}")
        c = c.replace(f"Car Transport in Gorakhpur", f"Car Transport from {district} to {state}")
        
        c = c.replace(f"Gorakhpur |", f"{district} to {state} |")
        c = c.replace(f"bike transport service in Gorakhpur", f"bike transport service from {district} to {state}")
        c = c.replace(f"car transport service in Gorakhpur", f"car transport service from {district} to {state}")
        c = c.replace(f"bike shifting gorakhpur", f"bike shifting {district} to {state}")
        c = c.replace(f"car shifting gorakhpur", f"car shifting {district} to {state}")
        c = c.replace(f"bike transport gorakhpur", f"bike transport {district} to {state}")
        c = c.replace(f"car transport gorakhpur", f"car transport {district} to {state}")
        c = c.replace(f"motorcycle transport gorakhpur", f"motorcycle transport {district} to {state}")
        c = c.replace(f"vehicle transport gorakhpur", f"vehicle transport {district} to {state}")
        c = c.replace(f"car carrier gorakhpur", f"car carrier {district} to {state}")
        c = c.replace(f"car relocation gorakhpur", f"car relocation {district} to {state}")
        c = c.replace(f"bike relocation gorakhpur", f"bike relocation {district} to {state}")
        c = c.replace(f"bike courier service gorakhpur", f"bike courier service {district} to {state}")

        c = c.replace(f"to and from Gorakhpur to anywhere in India", f"from {district} to {state} safely")
        
        # Geo tags
        c = re.sub(r'content="Gorakhpur"', f'content="{state}"', c)
        c = re.sub(r'content="26\.755;83\.373889"', f'content="{lat};{lng}"', c)
        c = re.sub(r'content="26\.755,\s*83\.373889"', f'content="{lat}, {lng}"', c)
        
        # Schema
        c = c.replace(f'"name": "Vahan Mover - Gorakhpur"', f'"name": "Vahan Mover - {district} to {state}"')
        c = c.replace(f"{service_type}-transport-gorakhpur.php", f"{service_type}-transport-{district_slug}-to-{slug}.php")
        c = c.replace(f'"addressLocality": "Gorakhpur"', f'"addressLocality": "{state}"')
        c = re.sub(r'"latitude":\s*"26\.755"', f'"latitude": "{lat}"', c)
        c = re.sub(r'"longitude":\s*"83\.373889"', f'"longitude": "{lng}"', c)
        
        # In Gorakhpur references
        c = c.replace("in Gorakhpur?", f"from {district} to {state}?")
        c = c.replace("from Gorakhpur?", f"from {district} to {state}?")
        c = c.replace("in Gorakhpur.", f"from {district} to {state}.")
        
        # Handling the "home in Gorakhpur" text specifically to be "home in {district}"
        c = c.replace("home in Gorakhpur", f"home in {district}")
        
        # AddressLocality override - ensure it remains State as the destination is State for search purposes (or keep District as source depending on SEO strategy but mostly destination is fine)
        # Actually Schema address relates to destination location if Area Served is origin. So:
        # addressLocality -> state. But if it got replaced with State, keep it.
        c = c.replace(f"addressLocality\": \"{district}\"", f"addressLocality\": \"{state}\"")
        
        # For area served
        c = c.replace(f'"name": "Gorakhpur"', f'"name": "{district}"')

        c = c.replace(">Gorakhpur</span>", f">{district} to {state}</span>")
        c = c.replace("Gorakhpur</strong>", f"{district} to {state}</strong>")
        
        # Google Maps
        c = re.sub(r'q=Gorakhpur,India', f'q={state},India', c)
        c = re.sub(r'q=Gorakhpur', f'q={state}', c)

        # Base case cleanup if leftover
        c = c.replace("Gorakhpur to", f"{district} to")
        c = c.replace("Gorakhpur", f"{district}")

        # Inject links before footer
        c = c.replace("<?php include 'includes/footer.php'; ?>", f"{links_section}\n    <?php include 'includes/footer.php'; ?>")

        with open(new_filename, 'w', encoding='utf-8') as f:
            f.write(c)
            
    print(f"Created all pages for {district} ({service_type} transport)")

if __name__ == "__main__":
    import os
    # We already created gorakhpur, but we can recreate or skip
    for district in districts:
        if district == 'Gorakhpur':
            continue
        process_file_for_district("bike-transport-gorakhpur.php", "bike", district)
        process_file_for_district("car-transport-gorakhpur.php", "car", district)
