import os
import re
import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

files_to_process = ['index.html', 'shop.html', 'categories.html', 'css/style.css']
image_dir = 'assets/images'
os.makedirs(image_dir, exist_ok=True)

url_pattern = re.compile(r'(https?://(?:images\.unsplash\.com|lh3\.googleusercontent\.com)[^\s"\'\)]+)')

url_to_filename = {}
counter = 1

req_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

for filepath in files_to_process:
    if not os.path.exists(filepath):
        continue
    print(f"Processing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    urls = url_pattern.findall(content)
    unique_urls = list(set(urls))
    
    for url in unique_urls:
        if url not in url_to_filename:
            filename = f"img_{counter:03d}.jpg"
            local_path = os.path.join(image_dir, filename)
            url_to_filename[url] = f"assets/images/{filename}"
            counter += 1
            
            print(f"Downloading {filename}...")
            try:
                req = urllib.request.Request(url, headers=req_headers)
                with urllib.request.urlopen(req, context=ctx) as response, open(local_path, 'wb') as out_file:
                    out_file.write(response.read())
            except Exception as e:
                print(f"Failed to download {url}: {e}")

    # Replace URLs in content
    for url, local_path in url_to_filename.items():
        if filepath.startswith('css'):
            css_local_path = f"../{local_path}"
            content = content.replace(url, css_local_path)
        else:
            content = content.replace(url, local_path)
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done downloading and updating files.")
