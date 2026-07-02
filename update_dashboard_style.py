import re

with open('larikelas6.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = 'class="dashboard-header" style="text-align: center; background: rgba(26, 32, 44, 0.95); padding: 40px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 1px solid rgba(255, 255, 255, 0.1);"'
replacement = 'class="dashboard-header" style="text-align: center; background: rgba(26, 32, 44, 0.95); padding: 50px 40px; width: 480px; max-width: 95%; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 1px solid rgba(255, 255, 255, 0.1);"'

content = content.replace(target, replacement)

with open('larikelas6.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Styles updated!")
