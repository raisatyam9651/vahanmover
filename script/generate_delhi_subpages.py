import os
import shutil

# List of locations
locations = [
    "Connaught Place", "Karol Bagh", "South Extension", "Greater Kailash", 
    "Lajpat Nagar", "Defence Colony", "Hauz Khas", "Saket", "Green Park", 
    "Vasant Kunj", "Vasant Vihar", "Malviya Nagar", "Dwarka", "Janakpuri", 
    "Rajouri Garden", "Punjabi Bagh", "Paschim Vihar", "Rohini", "Pitampura", 
    "Ashok Vihar", "Civil Lines", "Preet Vihar", "Laxmi Nagar", "Mayur Vihar", 
    "Anand Vihar", "Nehru Place", "Okhla"
]

# Helper to create slug
def create_slug(name):
    return name.lower().replace(" ", "-")

# Template files
bike_template_path = "bike-transport-delhi.php"
car_template_path = "car-transport-delhi.php"

# Ensure templates exist
if not os.path.exists(bike_template_path) or not os.path.exists(car_template_path):
    print("Error: Template files not found.")
    exit(1)

with open(bike_template_path, 'r') as f:
    bike_content = f.read()

with open(car_template_path, 'r') as f:
    car_content = f.read()

generated_files = []

for loc in locations:
    slug = create_slug(loc)
    loc_display = f"{loc}, Delhi"
    
    # ---------------------------
    # Generate Bike Page
    # ---------------------------
    new_bike_content = bike_content.replace("Delhi", loc_display)
    # Fix double "Delhi, Delhi" if any, though unlikely with simple find/replace on names, 
    # but check title logic. 
    # Actually, simpler replace: replace "Transport in Delhi" with "Transport in [Loc]" ?
    # The prompt strategy was: duplicate bike-transport-delhi.php and adapt.
    # bike-transport-delhi.php has "Bike Transport in Delhi".
    # If we replace "Delhi" with "Connaught Place, Delhi", we get "Bike Transport in Connaught Place, Delhi".
    # This seems correct and desirable for SEO.
    
    # However, we must be careful with partial matches or internal links.
    # E.g. "To and from Delhi" -> "To and from Connaught Place, Delhi" (OK)
    # "Bike transport Delhi" (meta keywords) -> "Bike transport Connaught Place, Delhi" (OK)
    
    # Clean up potentially awkward phrasing if needed, but simple replace usually works well for these local pages.
    
    bike_filename = f"bike-transport-{slug}.php"
    with open(bike_filename, 'w') as f:
        f.write(new_bike_content)
    generated_files.append(bike_filename)
    print(f"Generated: {bike_filename}")

    # ---------------------------
    # Generate Car Page
    # ---------------------------
    new_car_content = car_content.replace("Delhi", loc_display)
    
    car_filename = f"car-transport-{slug}.php"
    with open(car_filename, 'w') as f:
        f.write(new_car_content)
    generated_files.append(car_filename)
    print(f"Generated: {car_filename}")

print(f"\nSuccessfully created {len(generated_files)} pages.")
