import os
import re

def restore_districts():
    files = [f for f in os.listdir('.') if f.startswith('bike-transport-') and f.endswith('.php') and f != 'bike-transport-service.php']
    
    for bike_file in files:
        state_suffix = bike_file.replace('bike-transport-', '')
        car_file = f'car-transport-{state_suffix}'
        
        if not os.path.exists(car_file):
            print(f"Skipping {bike_file} as {car_file} does not exist.")
            continue
            
        print(f"Processing {state_suffix}...")
        
        # Read bike file to get the section
        with open(bike_file, 'r', encoding='utf-8') as f:
            bike_content = f.read()
            
        # Extract the "Bike Transport By City" section
        # Pattern: <!-- State-wise Bike Transport Section --> ... </section>
        # Note: The comment might vary slightly, so we look for the unique H2 "Bike Transport By City" or similar context.
        # In bike-transport-andhra-pradesh.php it was:
        # <!-- State-wise Bike Transport Section -->
        # <section ...>
        # ... <h2>Bike Transport <span>By City</span></h2> ...
        # ... </section>
        
        section_pattern = re.compile(r'(<!-- State-wise Bike Transport Section -->.*?<section.*?>.*?</h2>.*?<div class="glass-card".*?</div>\s*?</div>\s*?</section>)', re.DOTALL)
        match = section_pattern.search(bike_content)
        
        if not match:
            print(f"  Could not find district section in {bike_file}")
            # Try looser pattern if the comment is missing or different
            section_pattern_looser = re.compile(r'(<section.*?>.*?Bike Transport <span.*?>By City</span>.*?</h2>.*?</section>)', re.DOTALL)
            match = section_pattern_looser.search(bike_content)
            
        if match:
            district_section = match.group(1)
            
            # Convert Bike -> Car
            # We want to replace "Bike" with "Car" but carefully.
            # "Bike Transport By City" -> "Car Transport By City"
            # "Bike transport in Anakapalli" -> "Car transport in Anakapalli"
            # "bike transport service" -> "car transport service" (in paragraph)
            
            # Simple replacements
            new_section = district_section.replace('Bike Transport', 'Car Transport')
            new_section = new_section.replace('Bike transport', 'Car transport')
            new_section = new_section.replace('bike transport', 'car transport')
            new_section = new_section.replace('bike shifting', 'car shifting')
            new_section = new_section.replace('Bike Shifting', 'Car Shifting')
            
            # The icons might be bike specific? 
            # <i class="fa-solid fa-circle-check" ...> is generic check, which is fine.
            # If there are motorcycle icons, we might want to change them.
            # In the sample: <i class="fa-solid fa-circle-check"
            # So icons are fine.
            
            # Update the comment too if it was captured
            new_section = new_section.replace('<!-- State-wise Bike Transport Section -->', '<!-- Car Transport By City Section -->')

            # Now insert into car file
            with open(car_file, 'r', encoding='utf-8') as f:
                car_content = f.read()
            
            # Find the "Car Transport By City" section in car file to replace
            # It was inserted as:
            # <!-- Car Transport By City Section -->
            # <section ...> ... </section>
            
            car_section_pattern = re.compile(r'(<!-- Car Transport By City Section -->.*?<section.*?>.*?</section>)', re.DOTALL)
            
            if car_section_pattern.search(car_content):
                new_car_content = car_section_pattern.sub(new_section, car_content)
                
                with open(car_file, 'w', encoding='utf-8') as f:
                    f.write(new_car_content)
                print(f"  Updated {car_file}")
            else:
                print(f"  Could not find generic section in {car_file} to replace.")
        else:
            print(f"  No suitable section found in {bike_file}")

if __name__ == "__main__":
    restore_districts()
