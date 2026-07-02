import os
import glob
import re

html_files = glob.glob('*.html')
nav_item_template = '                    <li class="nav-item"><a class="nav-link" href="statistik.html"><i class="fas fa-chart-pie me-1"></i>Statistik</a></li>\n'

for f in html_files:
    if f == 'larikelas6.html' or f == '404.html': continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check if already added
    if 'href="statistik.html"' in content:
        print(f"Skipping {f}, already has statistik.html")
        continue

    pattern = r'([ \t]*<li class="nav-item"><a class="nav-link(?: active)?" href="log\.html".*?</li>\n)'
    new_content, count = re.subn(pattern, r'\g<1>' + nav_item_template, content)
    
    if count > 0:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated {f}")
    else:
        print(f"Could not find log.html nav-item in {f}")
