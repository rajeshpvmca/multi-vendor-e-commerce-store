import os
import glob

root_dir = r'e:\Stackly\Multi-Vendor E-Commerce Store'

# Root HTML files
root_files = glob.glob(os.path.join(root_dir, '*.html'))
for f in root_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    if 'href=\"#\"' in content:
        content = content.replace('href=\"#\"', 'href=\"404.html\"')
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)

# Dashboard HTML files
dash_dir = os.path.join(root_dir, 'dashboard')
dash_files = glob.glob(os.path.join(dash_dir, '*.html'))
for f in dash_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    if 'href=\"#\"' in content:
        content = content.replace('href=\"#\"', 'href=\"../404.html\"')
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
print('Replacement complete.')
