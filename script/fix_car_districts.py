import os
import re

# Change to the parent directory
os.chdir('..')

# Get all car district files (exclude state files)
state_files = [f for f in os.listdir('.') if f.startswith('car-transport-') and f.endswith('.php') and f != 'car-transport-service.php']

# Exclude state pages
exclude_states = [
    'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar', 'chhattisgarh',
    'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jharkhand',
    'karnataka', 'kerala', 'madhya-pradesh', 'maharashtra', 'manipur',
    'meghalaya', 'mizoram', 'nagaland', 'odisha', 'punjab',
    'rajasthan', 'sikkim', 'tamil-nadu', 'telangana', 'tripura',
    'uttar-pradesh', 'uttarakhand', 'west-bengal'
]

district_files = [f for f in state_files if not any(state in f for state in exclude_states)]

print(f"Found {len(district_files)} car district files to fix")

total_fixed = 0

for filename in sorted(district_files):
    # Read file
    with open(filename, "r", encoding='utf-8') as f:
        content = f.read()
    
    # Replace all bike-related content with car-related content
    replacements = [
        # Icons
        ('fa-motorcycle', 'fa-car'),
        
        # Text replacements (case-sensitive)
        ('Bike transport', 'Car transport'),
        ('bike transport', 'car transport'),
        ('Bike shifting', 'Car shifting'),
        ('bike shifting', 'car shifting'),
        ('Bike relocation', 'Car relocation'),
        ('bike relocation', 'car relocation'),
        ('Bike Transport', 'Car Transport'),
        ('Bike Shifting', 'Car Shifting'),
        ('Bike Inspection', 'Car Inspection'),
        ('bike inspection', 'car inspection'),
        
        # Two-wheeler to car/vehicle
        ('Two-Wheeler Transport', 'Vehicle Transport'),
        ('two-wheeler', 'car'),
        ('Two-wheeler', 'Car'),
        ('motorcycle transport', 'car transport'),
        ('Motorcycle transport', 'Car transport'),
        ('motorcycle', 'car'),
        ('Motorcycle', 'Car'),
        
        # Bike-specific terms
        ('Bikes Shifted', 'Cars Shifted'),
        ('bikes', 'cars'),
        ('Bikes', 'Cars'),
        ('bike', 'car'),
        ('Bike', 'Car'),
        
        # Service names
        ('bike parcel service', 'car transport service'),
        ('bike courier service', 'car transport service'),
        
        # Packing related
        ('Secure Packing', 'Safe Loading'),
        ('Professional Packing', 'Enclosed Carriers'),
        ('packing materials', 'enclosed carriers'),
        ('bubble wrap, foam, and protective covers', 'specialized car carriers'),
        
        # Loading related
        ('Professional Loading', 'Safe Loading'),
        ('specialized carriers designed for two-wheeler transport', 'specialized car carriers using hydraulic ramps'),
        
        # Service links
        ('bike-transport-service.php', 'car-transport-service.php'),
        
        # Stats
        ('15k+', '10k+'),
        
        # Box icon to truck icon for packing
        ('fa-box-open', 'fa-truck-ramp-box'),
    ]
    
    for old, new in replacements:
        content = content.replace(old, new)
    
    # Additional regex replacements for more complex patterns
    # Fix "bike RC" to "car RC"
    content = re.sub(r'\bbike RC\b', 'car RC', content, flags=re.IGNORECASE)
    
    # Fix any remaining "bike" references in context
    content = re.sub(r'your bike', 'your car', content, flags=re.IGNORECASE)
    content = re.sub(r'the bike', 'the car', content, flags=re.IGNORECASE)
    content = re.sub(r'a bike', 'a car', content, flags=re.IGNORECASE)
    
    # Write back
    with open(filename, "w", encoding='utf-8') as f:
        f.write(content)
    
    total_fixed += 1
    if total_fixed % 50 == 0:
        print(f"  Fixed {total_fixed} files...")

print(f"\n{'='*60}")
print(f"SUMMARY")
print(f"{'='*60}")
print(f"Total files fixed: {total_fixed}")
print(f"{'='*60}")
