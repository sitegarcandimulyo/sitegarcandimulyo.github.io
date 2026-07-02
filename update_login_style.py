import re

with open('larikelas6.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = """        .login-container {
            background: rgba(26, 32, 44, 0.9);
            backdrop-filter: blur(10px);
            padding: 30px 40px;
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
            width: 100%;
            max-width: 600px;
            display: flex;
            flex-direction: column;
            gap: 20px;
            max-height: 95vh;
            overflow-y: auto;
            text-align: center;
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: #ffffff;
        }"""

replacement = """        .login-container {
            background: rgba(26, 32, 44, 0.9);
            backdrop-filter: blur(10px);
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
            width: 720px;
            max-width: 95%;
            aspect-ratio: 16/9;
            display: flex;
            flex-direction: column;
            justify-content: center;
            gap: 20px;
            max-height: 95vh;
            overflow-y: auto;
            text-align: center;
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: #ffffff;
        }"""

content = content.replace(target, replacement)

with open('larikelas6.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated login-container styles.")
