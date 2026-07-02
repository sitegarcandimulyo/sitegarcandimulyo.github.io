import re

with open('larikelas6.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the style block and add links (remove animated background styles)
# We will just remove the animation and circle styles from the inline block.
style_anim_pattern = r'/\* --- ANIMASI LATAR BELAKANG \(Dashboard Style\) ---\s*\*/.*?@keyframes float {.*?\s*100% {\s*transform: translateY\(-120vh\) rotate\(360deg\);\s*opacity: 0;\s*border-radius: 50%;\s*}\s*}'
content = re.sub(style_anim_pattern, '', content, flags=re.DOTALL)

# Remove the animated background HTML divs
anim_html_pattern = r'<div class="animated-background">.*?</div>\s*</div>' # Wait, it might just be <div class="animated-background">...</div>
# Let's use a simpler pattern for the HTML
content = re.sub(r'<div class="animated-background">[\s\S]*?(<div id="setup-screen"|<div id="game-container")', r'\1', content)

# Adjust body style override if any
body_style_pattern = r'body\s*\{\s*/\* Overriding style\.css for game viewport \*/\s*height: 100vh;\s*width: 100vw;\s*overflow: hidden;\s*display: flex;\s*flex-direction: column;\s*position: relative;\s*\}'
content = re.sub(body_style_pattern, 'body { height: 100vh; width: 100vw; overflow: hidden; display: flex; flex-direction: column; position: relative; background-color: var(--bg-color); color: var(--text-main); }', content)

# Change setup container to match dark theme
content = content.replace('background: rgba(255, 255, 255, 0.95);', 'background: var(--card-bg); border: 1px solid rgba(255,255,255,0.05); color: var(--text-main);')
content = content.replace('color: #34495e;', 'color: #ffffff;') # titles
content = content.replace('color: #2c3e50;', 'color: #ffffff;') # text-color var
content = content.replace('--text-color: #2c3e50;', '--text-color: #ffffff;')

with open('larikelas6.html', 'w', encoding='utf-8') as f:
    f.write(content)
