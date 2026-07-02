import re

with open('rekomendasi.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Auditory Bottom Section
target_auditory = """            <p style="margin-top: 20px;">Cari podcast atau audiobook edukasi:</p>
            <div class="game-buttons">
                <a href="https://www.google.com/search?q=podcast+edukasi+anak+SD" target="_blank">Cari di Google</a>
            </div>"""

replacement_auditory = """            <p style="margin-top: 20px; font-weight: bold; color: #4fc3f7;">Contoh Video Pembelajaran Auditori (Nussa & Lagu Anak):</p>
            <div style="display: flex; gap: 15px; margin-top: 15px; flex-wrap: wrap; justify-content: center;">
                <div style="position: relative; width: 100%; max-width: 320px; padding-bottom: 30%; height: 200px; overflow: hidden; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
                    <iframe src="https://www.youtube.com/embed/videoseries?list=PL4fGSI1pDJn6jWSL5j8D8KjB2d1X0P6Ue" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" allowfullscreen title="Lagu Edukasi"></iframe>
                </div>
            </div>
            <p style="margin-top: 20px;">Cari podcast atau video edukasi lainnya:</p>
            <div class="game-buttons">
                <a href="https://www.youtube.com/results?search_query=podcast+edukasi+cerita+anak" target="_blank">Cari di YouTube</a>
            </div>"""

if target_auditory in content:
    content = content.replace(target_auditory, replacement_auditory)


# Replace Visual Bottom Section
# Looking at the line wrap in the source, we should use regex to match it reliably
target_visual = re.compile(r'<p style="margin-top: 20px;">Cari video lain di YouTube:</p>\s*<div class="game-buttons">\s*<a href="https://www\.youtube\.com/results\?search_query=video\+edukasi\+visual\+SD" target="_blank">Cari di\s*YouTube</a>\s*</div>', re.DOTALL)

replacement_visual = """            <p style="margin-top: 20px; font-weight: bold; color: #4fc3f7;">Contoh Video Pembelajaran Visual (Animasi & Eksplorasi):</p>
            <div style="display: flex; gap: 15px; margin-top: 15px; flex-wrap: wrap; justify-content: center;">
                <div style="position: relative; width: 100%; max-width: 320px; padding-bottom: 30%; height: 200px; overflow: hidden; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
                    <iframe src="https://www.youtube.com/embed/pWepfJ-8XU0" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" allowfullscreen title="Animasi Edukasi Kok Bisa"></iframe>
                </div>
            </div>
            <p style="margin-top: 20px;">Cari video edukasi visual lainnya:</p>
            <div class="game-buttons">
                <a href="https://www.youtube.com/results?search_query=video+edukasi+animasi+anak+SD" target="_blank">Cari di YouTube</a>
            </div>"""

content = target_visual.sub(replacement_visual, content)


# Replace Kinesthetic Bottom Section
target_kinesthetic = """            <p style="margin-top: 20px;">Cari game lain di Google:</p>
            <div class="game-buttons">
                <a href="https://www.google.com/search?q=game+edukasi+kinestetik+SD" target="_blank">Cari di Google</a>
            </div>"""

replacement_kinesthetic = """            <p style="margin-top: 20px; font-weight: bold; color: #4fc3f7;">Contoh Video Pembelajaran Kinestetik (Senam & Eksperimen):</p>
            <div style="display: flex; gap: 15px; margin-top: 15px; flex-wrap: wrap; justify-content: center;">
                <div style="position: relative; width: 100%; max-width: 320px; padding-bottom: 30%; height: 200px; overflow: hidden; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
                    <iframe src="https://www.youtube.com/embed/8-9m2iB0iM4" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" allowfullscreen title="Senam Anak dan Eksperimen"></iframe>
                </div>
            </div>
            <p style="margin-top: 20px;">Cari video aktivitas & game edukasi lainnya:</p>
            <div class="game-buttons">
                <a href="https://www.youtube.com/results?search_query=senam+anak+SD+atau+eksperimen+sains" target="_blank">Cari di YouTube</a>
            </div>"""

if target_kinesthetic in content:
    content = content.replace(target_kinesthetic, replacement_kinesthetic)

with open('rekomendasi.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated rekomendasi.html to embed YouTube videos at the bottom of each learning style section.")
