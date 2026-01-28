import os
import re

# Change to the parent directory
os.chdir('..')

# Google verification meta tag
verification_tag = '    <meta name="google-site-verification" content="xjeLREcMez2kegDf2QsMgGLabvzbJVgrIwn4XZR5R-c" />'

print("="*80)
print("Adding Google Search Console Verification Meta Tag")
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
files_already_have_tag = 0
files_updated = 0
files_skipped = 0

# Process each file
for file_path in sorted(all_files):
    try:
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file already has the verification tag
        if 'google-site-verification' in content and 'xjeLREcMez2kegDf2QsMgGLabvzbJVgrIwn4XZR5R-c' in content:
            files_already_have_tag += 1
            continue
        
        # Check if file has a <head> section
        if '<head>' not in content:
            files_skipped += 1
            continue
        
        # Find the position after <head> tag
        # Insert after the viewport meta tag if it exists, otherwise after <head>
        if '<meta name="viewport"' in content:
            # Insert after viewport meta tag
            pattern = r'(<meta name="viewport"[^>]*>)'
            replacement = r'\1\n' + verification_tag
            new_content = re.sub(pattern, replacement, content, count=1)
        else:
            # Insert right after <head>
            pattern = r'(<head>)'
            replacement = r'\1\n' + verification_tag
            new_content = re.sub(pattern, replacement, content, count=1)
        
        # Write back if changes were made
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            files_updated += 1
            
    except Exception as e:
        print(f"⚠️  Error processing {file_path}: {e}")

# Print summary
print("="*80)
print("GOOGLE VERIFICATION TAG ADDITION COMPLETE")
print("="*80)
print(f"Files processed: {len(all_files)}")
print(f"Files already had tag: {files_already_have_tag}")
print(f"Files updated: {files_updated}")
print(f"Files skipped (no <head>): {files_skipped}")
print("="*80)
print()

if files_updated > 0:
    print(f"✅ Successfully added Google verification tag to {files_updated} files!")
else:
    print("✅ All files already have the Google verification tag!")
