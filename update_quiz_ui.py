import re

with open('larikelas6.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace HTML for player-zones
old_html_p1 = '''            <!-- P1 -->
            <div class="player-zone zone-p1" id="zone-p1">
                <div class="player-header">
                    <div id="disp-p1-name" class="p-name">P1</div>
                    <div class="p-stats"><span id="score-p1">0</span> | <span id="q-count-p1">1/20</span></div>
                </div>
                <div class="question-box" id="q-box-p1">Memuat...</div>
                <div class="options-grid" id="opts-p1"></div>
            </div>'''
new_html_p1 = '''            <!-- P1 -->
            <div class="player-zone zone-p1" id="zone-p1">
                <div class="player-header">
                    <div id="disp-p1-name" class="p-name">P1</div>
                    <div class="question-box" id="q-box-p1">Memuat...</div>
                    <div class="p-stats"><span id="score-p1">0</span> | <span id="q-count-p1">1/20</span></div>
                </div>
                <div class="options-grid" id="opts-p1"></div>
            </div>'''
content = content.replace(old_html_p1, new_html_p1)

old_html_p2 = '''            <!-- P2 -->
            <div class="player-zone zone-p2" id="zone-p2">
                <div class="player-header">
                    <div id="disp-p2-name" class="p-name">P2</div>
                    <div class="p-stats"><span id="score-p2">0</span> | <span id="q-count-p2">1/20</span></div>
                </div>
                <div class="question-box" id="q-box-p2">Memuat...</div>
                <div class="options-grid" id="opts-p2"></div>
            </div>'''
new_html_p2 = '''            <!-- P2 -->
            <div class="player-zone zone-p2" id="zone-p2">
                <div class="player-header">
                    <div id="disp-p2-name" class="p-name">P2</div>
                    <div class="question-box" id="q-box-p2">Memuat...</div>
                    <div class="p-stats"><span id="score-p2">0</span> | <span id="q-count-p2">1/20</span></div>
                </div>
                <div class="options-grid" id="opts-p2"></div>
            </div>'''
content = content.replace(old_html_p2, new_html_p2)

# Replace CSS
# player-zone
content = re.sub(r'\.player-zone\s*\{[^}]*\}', 
'''.player-zone {
            padding: 4px;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            position: relative;
            overflow-y: hidden;
            border: 1px solid #bdbdbd;
            background: #f7dede;
            border-top: 3px solid #27ae60;
            border-radius: 4px;
            gap: 4px;
        }''', content, count=1)

content = re.sub(r'\.zone-p1\s*\{[^}]*\}\s*\.zone-p2\s*\{[^}]*\}',
'''.zone-p1, .zone-p2 {
            background-color: #f7dede;
            border-color: #bdbdbd;
            border-top-color: #27ae60;
        }''', content, count=1)

# player-header
content = re.sub(r'\.player-header\s*\{[^}]*\}',
'''.player-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: white;
            padding: 0 10px;
            height: 40px;
            border: 1px solid #bdbdbd;
            border-radius: 4px;
            color: #333;
            font-weight: bold;
        }''', content, count=1)

content = re.sub(r'\.p-name\s*\{[^}]*\}',
'''.p-name {
            text-transform: uppercase;
            width: 80px;
            text-align: left;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            font-size: 12px;
        }''', content, count=1)

content = re.sub(r'\.p-stats\s*\{[^}]*\}',
'''.p-stats {
            width: 80px;
            text-align: right;
            font-size: 12px;
        }''', content, count=1)

content = re.sub(r'\.question-box\s*\{[^}]*\}',
'''.question-box {
            flex-grow: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            font-size: 16px;
            font-weight: 700;
            color: #2c3e50;
            margin: 0 10px;
            white-space: normal;
        }''', content, count=1)

content = re.sub(r'\.options-grid\s*\{[^}]*\}',
'''.options-grid {
            display: flex;
            flex-direction: column;
            gap: 4px;
        }''', content, count=1)

content = re.sub(r'\.option-btn\s*\{[^}]*\}',
'''.option-btn {
            padding: 4px 12px;
            border: 1px solid #bdbdbd;
            border-radius: 4px !important;
            background: white;
            color: #333;
            font-size: 14px;
            font-weight: 700;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            min-height: 32px;
            width: 100%;
            line-height: 1.2;
            word-wrap: break-word;
            white-space: normal;
            transition: background 0.2s;
        }''', content, count=1)

# Remove option-btn:first-child and last-child borders since we're using gap now
content = re.sub(r'\.option-btn:first-child\s*\{[^}]*\}\s*\.option-btn:last-child\s*\{[^}]*\}', '', content, count=1)

with open('larikelas6.html', 'w', encoding='utf-8') as f:
    f.write(content)
