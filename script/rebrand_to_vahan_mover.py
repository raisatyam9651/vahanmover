import os
import re

# Change to the parent directory
os.chdir('..')

print("="*80)
print("REBRANDING: Shifter → Vahan Mover")
print("="*80)
print()

# Define replacements
replacements = [
    ('SHIFTER', 'VAHAN MOVER'),
    ('Shifter Logistics', 'Vahan Mover Logistics'),
    ('Shifter', 'Vahan Mover'),
    ('shifter.com', 'vahanmover.com'),
]

# Get all PHP files (excluding html_backup and script directories)
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
total_files_changed = 0
total_replacements = 0
changes_by_file = {}

# Process each file
for file_path in sorted(all_files):
    try:
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        file_changes = 0
        
        # Apply all replacements
        for old, new in replacements:
            count = content.count(old)
            if count > 0:
                content = content.replace(old, new)
                file_changes += count
        
        # Write back if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            total_files_changed += 1
            total_replacements += file_changes
            changes_by_file[file_path] = file_changes
            
    except Exception as e:
        print(f"⚠️  Error processing {file_path}: {e}")

# Print summary
print("="*80)
print("REBRANDING COMPLETE")
print("="*80)
print(f"Files processed: {len(all_files)}")
print(f"Files changed: {total_files_changed}")
print(f"Total replacements: {total_replacements}")
print("="*80)
print()

# Show files with most changes
if changes_by_file:
    print("Top 10 files with most changes:")
    print("-"*80)
    sorted_changes = sorted(changes_by_file.items(), key=lambda x: x[1], reverse=True)[:10]
    for file_path, count in sorted_changes:
        print(f"  {count:3d} changes - {file_path}")
    print()

# Verify no "Shifter" remains in PHP files
print("Verifying rebranding...")
print("-"*80)
remaining_shifter = []
for file_path in all_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        if 'Shifter' in content or 'SHIFTER' in content or 'shifter' in content:
            # Count occurrences
            count = content.count('Shifter') + content.count('SHIFTER') + content.count('shifter')
            remaining_shifter.append((file_path, count))
    except:
        pass

if remaining_shifter:
    print(f"⚠️  WARNING: Found {len(remaining_shifter)} files still containing 'Shifter':")
    for file_path, count in remaining_shifter[:5]:
        print(f"  {file_path} ({count} occurrences)")
else:
    print("✅ SUCCESS: No 'Shifter' references found in PHP files!")

print()
print("="*80)
print("✓ Rebranding script completed successfully")
print("="*80)
