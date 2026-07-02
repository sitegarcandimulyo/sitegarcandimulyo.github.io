import re

with open('rekomendasi.html', 'r', encoding='utf-8') as f:
    content = f.read()

def revert_videos(html_content, section_keyword, video_id1, title1):
    # Match the 2-video block
    pattern = re.compile(rf'<p style="margin-top: 20px; font-weight: bold; color: #4fc3f7;">Contoh Video Pembelajaran {section_keyword}:</p>.*?<div class="game-buttons">\s*<a href="[^"]+".*?</a>\s*</div>', re.DOTALL)
    
    # 1-video layout (which worked correctly)
    replacement = f"""<p style="margin-top: 20px; font-weight: bold; color: #4fc3f7;">Contoh Video Pembelajaran {section_keyword}:</p>
            <div style="display: flex; gap: 15px; margin-top: 15px; flex-wrap: wrap; justify-content: center;">
                <div style="position: relative; width: 100%; max-width: 320px; padding-bottom: 30%; height: 200px; overflow: hidden; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
                    <iframe src="https://www.youtube.com/embed/{video_id1}" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" allowfullscreen title="{title1}"></iframe>
                </div>
            </div>
            <p style="margin-top: 20px;">Cari video edukasi {section_keyword.split()[0].lower()} lainnya:</p>
            <div class="game-buttons">
                <a href="https://www.youtube.com/results?search_query=video+edukasi+{section_keyword.split()[0].lower()}+anak+SD" target="_blank">Cari di YouTube</a>
            </div>"""
    
    return pattern.sub(replacement, html_content)


content = revert_videos(content, "Auditori", "videoseries?list=PL4fGSI1pDJn6jWSL5j8D8KjB2d1X0P6Ue", "Lagu Edukasi")
content = revert_videos(content, "Visual", "pWepfJ-8XU0", "Animasi Edukasi Kok Bisa")
content = revert_videos(content, "Kinestetik", "8-9m2iB0iM4", "Senam Anak dan Eksperimen")

with open('rekomendasi.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Reverted rekomendasi.html to the 1-video layout.")
