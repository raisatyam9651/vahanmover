import os
import re

# Change to the parent directory
os.chdir('..')

print("="*80)
print("Formatting header-link.php Include Statements")
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
files_already_formatted = 0

# Process each file
for file_path in sorted(all_files):
    try:
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file has the include statement
        if "includes/header-link.php" not in content:
            continue
        
        # Pattern to match the include on the same line as other content
        # This matches when the include is at the end of a line with other content
        pattern = r'([^>\n]+>)\s*(<\?php include \'includes/header-link\.php\'; \?>)'
        
        # Check if pattern exists (include is on same line as other content)
        if re.search(pattern, content):
            # Replace with properly formatted version (include on new line)
            new_content = re.sub(pattern, r'\1\n    \n    \2', content)
            
            # Write back if changes were made
            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                files_updated += 1
        else:
            files_already_formatted += 1
            
    except Exception as e:
        print(f"⚠️  Error processing {file_path}: {e}")

# Print summary
print("="*80)
print("HEADER INCLUDE FORMATTING COMPLETE")
print("="*80)
print(f"Files processed: {len(all_files)}")
print(f"Files updated: {files_updated}")
print(f"Files already formatted: {files_already_formatted}")
print("="*80)
print()

if files_updated > 0:
    print(f"✅ Successfully formatted {files_updated} files!")
else:
    print("✅ All files already have properly formatted includes!")
