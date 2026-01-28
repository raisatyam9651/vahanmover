import os
import re

# Change to the parent directory
os.chdir('..')

print("="*80)
print("Updating Internal Links to Clean URLs")
print("="*80)
print()

# Get all PHP files (excluding html_backup, script, and includes directories)
all_files = []
for root, dirs, files in os.walk('.'):
    # Skip excluded directories
    dirs[:] = [d for d in dirs if d not in ['html_backup', 'script', '.git', '.venv', '__pycache__']]
    
    for file in files:
        if file.endswith('.php'):
            file_path = os.path.join(root, file)
            all_files.append(file_path)

print(f"Found {len(all_files)} PHP files to process")
print()

# Track statistics
files_updated = 0
total_replacements = 0

# Pattern to match href="*.php" (but not in includes)
pattern = r'href="([^"]*?)\.php"'

# Process each file
for file_path in sorted(all_files):
    try:
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Count matches before replacement
        matches = re.findall(pattern, content)
        
        # Filter out includes (we don't want to change those)
        valid_matches = [m for m in matches if not m.startswith('includes/')]
        
        if valid_matches:
            # Replace .php with / (clean URL)
            # But skip includes directory
            def replace_func(match):
                url = match.group(1)
                if url.startswith('includes/'):
                    return match.group(0)  # Don't change includes
                return f'href="{url}/"'
            
            new_content = re.sub(pattern, replace_func, content)
            
            # Write back if changes were made
            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                files_updated += 1
                total_replacements += len(valid_matches)
                
    except Exception as e:
        print(f"⚠️  Error processing {file_path}: {e}")

# Print summary
print("="*80)
print("LINK UPDATE COMPLETE")
print("="*80)
print(f"Files processed: {len(all_files)}")
print(f"Files updated: {files_updated}")
print(f"Total links updated: {total_replacements}")
print("="*80)
print()

if files_updated > 0:
    print(f"✅ Successfully updated {total_replacements} links in {files_updated} files!")
    print()
    print("Examples of changes:")
    print('  href="contact.php" → href="contact/"')
    print('  href="bike-transport-service.php" → href="bike-transport-service/"')
else:
    print("✅ All links are already in clean URL format!")
