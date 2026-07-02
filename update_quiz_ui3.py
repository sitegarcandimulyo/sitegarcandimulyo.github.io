import re

def update_ui(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update HTML
    old_html_p1 = """            <div class="player-zone zone-p1" id="zone-p1">
                <div class="player-header">
                    <div id="disp-p1-name" class="p-name">P1</div>
                    <div class="question-box" id="q-box-p1">Memuat...</div>
                    <div class="p-stats"><span id="score-p1">0</span> | <span id="q-count-p1">1/20</span></div>
                </div>
                <div class="options-grid" id="opts-p1"></div>
            </div>"""
    
    new_html_p1 = """            <div class="player-zone zone-p1" id="zone-p1">
                <div class="player-header">
                    <div id="disp-p1-name" class="p-name">P1</div>
                    <div class="p-stats"><span id="score-p1" style="display:none;">0</span><span id="q-count-p1">1/20</span></div>
                </div>
                <div class="question-box" id="q-box-p1">Memuat...</div>
                <div class="options-grid" id="opts-p1"></div>
            </div>"""

    old_html_p2 = """            <div class="player-zone zone-p2" id="zone-p2">
                <div class="player-header">
                    <div id="disp-p2-name" class="p-name">P2</div>
                    <div class="question-box" id="q-box-p2">Memuat...</div>
                    <div class="p-stats"><span id="score-p2">0</span> | <span id="q-count-p2">1/20</span></div>
                </div>
                <div class="options-grid" id="opts-p2"></div>
            </div>"""

    new_html_p2 = """            <div class="player-zone zone-p2" id="zone-p2">
                <div class="player-header">
                    <div id="disp-p2-name" class="p-name">P2</div>
                    <div class="p-stats"><span id="score-p2" style="display:none;">0</span><span id="q-count-p2">1/20</span></div>
                </div>
                <div class="question-box" id="q-box-p2">Memuat...</div>
                <div class="options-grid" id="opts-p2"></div>
            </div>"""

    content = content.replace(old_html_p1, new_html_p1)
    content = content.replace(old_html_p2, new_html_p2)

    # 2. Update CSS
    css_pattern = re.compile(r'\.player-zone \{.*?(?=\.option-btn\.selected-answer \{)', re.DOTALL)
    
    new_css = """        .player-zone {
            padding: 0;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            position: relative;
            overflow-y: hidden;
            border: 2px solid #1a202c;
            background: #fff;
            border-radius: 4px;
            gap: 0;
        }

        .player-zone.hidden {
            display: none;
        }

        .zone-p1, .zone-p2 {
            background-color: #fff;
            border-color: #1a202c;
        }

        .player-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #ffe6e6;
            padding: 4px 10px;
            min-height: 25px;
            border-bottom: 2px solid #1a202c;
            color: #d32f2f;
            font-weight: bold;
        }

        .p-name {
            text-transform: uppercase;
            width: auto;
            text-align: left;
            font-size: 11px;
            color: #d32f2f;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .p-stats {
            width: auto;
            text-align: right;
            font-size: 11px;
            color: #d32f2f;
        }

        .question-box {
            flex-grow: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            font-size: 15px;
            font-weight: 800;
            color: #fff;
            background: #0f172a;
            padding: 15px 10px;
            margin: 0;
            white-space: normal;
            border-bottom: 2px solid #1a202c;
        }

        .options-grid {
            display: flex;
            flex-direction: column;
            gap: 0;
        }

        .option-btn {
            padding: 14px 12px;
            border: none;
            border-bottom: 1px solid #e2e8f0;
            border-radius: 0 !important;
            background: white;
            color: #333;
            font-size: 13px;
            font-weight: 500;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            min-height: 38px;
            width: 100%;
            line-height: 1.2;
            word-wrap: break-word;
            white-space: normal;
            transition: background 0.2s;
        }

        .option-btn:last-child {
            border-bottom: none;
        }
        
        .option-btn.disabled {
            pointer-events: none;
            opacity: 0.7;
        }

        .option-btn:active {
            background-color: #f1f5f9;
        }

        """
    
    if css_pattern.search(content):
        content = css_pattern.sub(new_css, content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated CSS and HTML layout for quiz area.")
    else:
        print("CSS pattern not found!")

update_ui('larikelas6.html')
