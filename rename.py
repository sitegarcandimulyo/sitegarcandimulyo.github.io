import os

# List of files to update based on grep results
files = [
    'index.html',
    'larikelas6.html',
    'log.html',
    'rekomendasi.html',
    'sumber.html'
]

for file in files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Perform replacements
        content = content.replace('TEGAS OPTIMALAI', 'SI TEGAR AI')
        content = content.replace('Tegas Optimal Ai', 'Si Tegar AI')
        content = content.replace('TEGAS OPTIMAL', 'SI TEGAR')
        content = content.replace('Tegas Optimal', 'Si Tegar')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Renamed 'Tegas Optimal' to 'Si Tegar' across HTML files.")
