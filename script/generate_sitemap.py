import os
from datetime import datetime

# Change to the parent directory
os.chdir('..')

print("="*80)
print("Generating sitemap.xml")
print("="*80)
print()

# Get all PHP files
all_php_files = []
for root, dirs, files in os.walk('.'):
    # Skip excluded directories
    dirs[:] = [d for d in dirs if d not in ['html_backup', 'script', '.git', '.venv', '__pycache__', 'includes']]
    
    for file in files:
        if file.endswith('.php'):
            # Get relative path from root
            file_path = os.path.join(root, file)
            # Remove leading './'
            file_path = file_path[2:] if file_path.startswith('./') else file_path
            all_php_files.append(file_path)

print(f"Found {len(all_php_files)} PHP files")

# Sort files for consistent output
all_php_files.sort()

# Get current date for lastmod
current_date = datetime.now().strftime('%Y-%m-%d')

# Create sitemap XML
sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

# Add each PHP file as a URL
for php_file in all_php_files:
    # Determine priority based on file type
    if php_file == 'index.php':
        priority = '1.0'
        changefreq = 'daily'
    elif php_file == 'contact.php':
        priority = '0.9'
        changefreq = 'monthly'
    elif php_file in ['bike-transport-service.php', 'car-transport-service.php']:
        priority = '0.9'
        changefreq = 'weekly'
    elif 'transport-service' in php_file:
        priority = '0.8'
        changefreq = 'weekly'
    else:
        # State and district pages
        priority = '0.7'
        changefreq = 'monthly'
    
    sitemap_content += f'  <url>\n'
    sitemap_content += f'    <loc>https://vahanmover.com/{php_file}</loc>\n'
    sitemap_content += f'    <lastmod>{current_date}</lastmod>\n'
    sitemap_content += f'    <changefreq>{changefreq}</changefreq>\n'
    sitemap_content += f'    <priority>{priority}</priority>\n'
    sitemap_content += f'  </url>\n'

sitemap_content += '</urlset>'

# Write sitemap.xml
with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap_content)

print(f"✅ Created sitemap.xml with {len(all_php_files)} URLs")
print()
print("="*80)
print("Sitemap generation complete!")
print("="*80)
