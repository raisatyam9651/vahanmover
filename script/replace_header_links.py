import os
import re

# Change to the parent directory
os.chdir('..')

print("="*80)
print("Replacing CSS/Font Awesome Links with header-link.php Include")
print("="*80)
print()

# Get all PHP files (excluding html_backup, script, and includes directories)
all_files = []
for root, dirs, files in os.walk('.'):
    # Skip excluded directories
    dirs[:] = [d for d in dirs if d not in ['html_backup', 'script', '.git', '.venv', '__pycache__', 'includes']]
    
    for file in files:
        if file.endswith('.php'):
            file_path = os.path.join(root, file)
            all_files.append(file_path)

print(f"Found {len(all_files)} PHP files to process")
print()

# Track statistics
files_updated = 0
files_without_links = 0

# Process each file
for file_path in sorted(all_files):
    try:
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file has the CSS and Font Awesome links
        if 'style.css' not in content or 'font-awesome' not in content:
            files_without_links += 1
            continue
        
        # Pattern to match the CSS and Font Awesome links (with optional whitespace and comments)
        pattern = r'\s*<link rel="stylesheet" href="style\.css">\s*\n?\s*<!-- Font Awesome for Icons -->\s*\n?\s*<link rel="stylesheet" href="https://cdnjs\.cloudflare\.com/ajax/libs/font-awesome/[^"]+\.css">\s*\n?'
        
        # Replace with PHP include
        replacement = '    <?php include \'includes/header-link.php\'; ?>\n'
        new_content = re.sub(pattern, replacement, content)
        
        # Write back if changes were made
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            files_updated += 1
            
    except Exception as e:
        print(f"⚠️  Error processing {file_path}: {e}")

# Print summary
print("="*80)
print("HEADER LINKS REPLACEMENT COMPLETE")
print("="*80)
print(f"Files processed: {len(all_files)}")
print(f"Files updated: {files_updated}")
print(f"Files without links: {files_without_links}")
print("="*80)
print()

if files_updated > 0:
    print(f"✅ Successfully replaced header links with include in {files_updated} files!")
else:
    print("⚠️  No files were updated. Links may already be replaced or pattern didn't match.")
