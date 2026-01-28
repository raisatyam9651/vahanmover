import os
import re

# Change to the parent directory
os.chdir('..')

print("="*80)
print("Updating Contact Number to 6388717912")
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

# Replacements to make
replacements = [
    # formatted display (5-5 split)
    (r'98765 43210', '63887 17912'),
    # tel link format
    (r'\+919876543210', '+916388717912'),
    # raw number just in case
    (r'9876543210', '6388717912')
]

# Process each file
for file_path in sorted(all_files):
    try:
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        file_replacements = 0
        
        for old, new in replacements:
            # Use regex for replacement to ensure we catch all
            count = len(re.findall(old, content))
            if count > 0:
                content = re.sub(old, new, content)
                file_replacements += count
        
        # Write back if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            files_updated += 1
            total_replacements += file_replacements
            
            # Print specific updates for key files
            if 'footer.php' in file_path or 'contact.php' in file_path or 'index.php' in file_path:
                print(f"Updated {os.path.basename(file_path)}: {file_replacements} changes")
                
    except Exception as e:
        print(f"⚠️  Error processing {file_path}: {e}")

# Print summary
print("="*80)
print("CONTACT NUMBER UPDATE COMPLETE")
print("="*80)
print(f"Files processed: {len(all_files)}")
print(f"Files updated: {files_updated}")
print(f"Total replacements: {total_replacements}")
print("="*80)
print()

if files_updated > 0:
    print(f"✅ Successfully updated phone number across {files_updated} files!")
    print("New number: 6388717912")
else:
    print("⚠️ No phone numbers found to update!")
