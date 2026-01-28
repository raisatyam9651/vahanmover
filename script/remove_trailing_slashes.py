import os
import re

# Change to the parent directory
os.chdir('..')

print("="*80)
print("Removing Trailing Slashes from Internal Links")
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

# Pattern to match href="*/" (but not root / and not in includes)
pattern = r'href="([^"]+)/"'

# Process each file
for file_path in sorted(all_files):
    try:
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace trailing slashes (but keep root / and includes/)
        def replace_func(match):
            url = match.group(1)
            # Keep root URL as is
            if url == '':
                return match.group(0)
            # Keep includes directory as is
            if url.startswith('includes/'):
                return match.group(0)
            # Keep external URLs (http, https, tel, mailto, #)
            if url.startswith(('http://', 'https://', 'tel:', 'mailto:', '#')):
                return match.group(0)
            # Remove trailing slash
            return f'href="{url}"'
        
        new_content = re.sub(pattern, replace_func, content)
        
        # Count changes
        if new_content != content:
            changes = len(re.findall(pattern, content)) - len(re.findall(r'href="([^"]+)/"', new_content))
            if changes > 0:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                files_updated += 1
                total_replacements += changes
                
    except Exception as e:
        print(f"⚠️  Error processing {file_path}: {e}")

# Print summary
print("="*80)
print("TRAILING SLASH REMOVAL COMPLETE")
print("="*80)
print(f"Files processed: {len(all_files)}")
print(f"Files updated: {files_updated}")
print(f"Total slashes removed: {total_replacements}")
print("="*80)
print()

if files_updated > 0:
    print(f"✅ Successfully removed trailing slashes from {total_replacements} links in {files_updated} files!")
    print()
    print("Examples of changes:")
    print('  href="contact/" → href="contact"')
    print('  href="bike-transport-service/" → href="bike-transport-service"')
else:
    print("✅ All links are already without trailing slashes!")
