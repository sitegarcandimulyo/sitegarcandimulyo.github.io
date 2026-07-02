import re

with open('larikelas6.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update main dashboard container
content = content.replace(
    'background: rgba(255,255,255,0.95); padding: 40px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.5);',
    'background: rgba(26, 32, 44, 0.95); padding: 40px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 1px solid rgba(255, 255, 255, 0.1);'
)

# Update texts in main dashboard
content = content.replace(
    'color: #2c3e50; font-weight: 800; margin-top: 15px; font-size: 2.5rem;',
    'color: #ffffff; font-weight: 800; margin-top: 15px; font-size: 2.5rem; text-shadow: 0 0 10px rgba(255,255,255,0.3);'
)
content = content.replace(
    'color: #7f8c8d; font-size: 1.2rem;',
    'color: #94a3b8; font-size: 1.2rem;'
)

# Update mode buttons
content = content.replace(
    'transition: all 0.3s; background: white;',
    'transition: all 0.3s; background: rgba(255, 255, 255, 0.05);'
)
content = content.replace(
    '<span class="mode-text fs-5 fw-bold text-dark">',
    '<span class="mode-text fs-5 fw-bold text-white">'
)

# Fix inputs for registration
old_input_css = """            input,
            select {
                padding: 15px;
                font-size: 1.5rem;
                border-radius: 8px;
            }"""
new_input_css = """            input,
            select {
                padding: 15px;
                font-size: 1.5rem;
                border-radius: 8px;
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.2);
                color: #ffffff;
            }
            input::placeholder, select::placeholder {
                color: rgba(255, 255, 255, 0.5);
            }"""
content = content.replace(old_input_css, new_input_css)

with open('larikelas6.html', 'w', encoding='utf-8') as f:
    f.write(content)
