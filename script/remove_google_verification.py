import os
import re

# Change to the parent directory
os.chdir('..')

print("="*80)
print("Removing Google Search Console Verification Meta Tag")
print("="*80)
print()

# Get all PHP files (excluding html_backup and script directories)
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
files_without_tag = 0

# Process each file
for file_path in sorted(all_files):
    try:
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file has the verification tag
        if 'google-site-verification' not in content or 'xjeLREcMez2kegDf2QsMgGLabvzbJVgrIwn4XZR5R-c' not in content:
            files_without_tag += 1
            continue
        
        # Remove the verification meta tag line
        # Match the entire line including whitespace
        pattern = r'\s*<meta name="google-site-verification" content="xjeLREcMez2kegDf2QsMgGLabvzbJVgrIwn4XZR5R-c" />\n?'
        new_content = re.sub(pattern, '', content)
        
        # Write back if changes were made
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            files_updated += 1
            
    except Exception as e:
        print(f"⚠️  Error processing {file_path}: {e}")

# Print summary
print("="*80)
print("GOOGLE VERIFICATION TAG REMOVAL COMPLETE")
print("="*80)
print(f"Files processed: {len(all_files)}")
print(f"Files updated (tag removed): {files_updated}")
print(f"Files without tag: {files_without_tag}")
print("="*80)
print()

if files_updated > 0:
    print(f"✅ Successfully removed Google verification tag from {files_updated} files!")
else:
    print("✅ No files had the Google verification tag!")
