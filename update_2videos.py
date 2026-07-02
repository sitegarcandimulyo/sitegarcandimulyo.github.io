import re

with open('rekomendasi.html', 'r', encoding='utf-8') as f:
    content = f.read()

def replace_videos(html_content, section_keyword, video_id1, video_id2, title1, title2):
    # Regex to find the whole video block we inserted last time
    # We look for the <p> containing "Contoh Video Pembelajaran ..." 
    # up to the <div class="game-buttons"> block
    
    # Using a generic regex that captures the section based on keyword
    pattern = re.compile(rf'<p style="margin-top: 20px; font-weight: bold; color: #4fc3f7;">Contoh Video Pembelajaran {section_keyword}.*?<div class="game-buttons">\s*<a href="[^"]+".*?</a>\s*</div>', re.DOTALL)
    
    # We reconstruct the entire bottom section for that learning style
    replacement = f"""<p style="margin-top: 20px; font-weight: bold; color: #4fc3f7;">Contoh Video Pembelajaran {section_keyword}:</p>
            <div style="display: flex; gap: 20px; margin-top: 15px; flex-wrap: wrap; justify-content: center;">
                <!-- Video 1 -->
                <div style="position: relative; width: 45%; min-width: 280px; max-width: 350px; aspect-ratio: 16/9; overflow: hidden; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
                    <iframe src="https://www.youtube.com/embed/{video_id1}" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" allowfullscreen title="{title1}"></iframe>
                </div>
                <!-- Video 2 -->
                <div style="position: relative; width: 45%; min-width: 280px; max-width: 350px; aspect-ratio: 16/9; overflow: hidden; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
                    <iframe src="https://www.youtube.com/embed/{video_id2}" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" allowfullscreen title="{title2}"></iframe>
                </div>
            </div>
            <p style="margin-top: 20px;">Cari video edukasi {section_keyword.split()[0].lower()} lainnya:</p>
            <div class="game-buttons">
                <a href="https://www.youtube.com/results?search_query=video+edukasi+{section_keyword.split()[0].lower()}+anak+SD" target="_blank">Cari di YouTube</a>
            </div>"""
    
    return pattern.sub(replacement, html_content)


content = replace_videos(content, "Auditori (Nussa & Lagu Anak)", "videoseries?list=PL4fGSI1pDJn6jWSL5j8D8KjB2d1X0P6Ue", "7VIGYI8d0l0", "Lagu Edukasi Anak", "Nussa Official")
content = replace_videos(content, "Visual (Animasi & Eksplorasi)", "pWepfJ-8XU0", "8O-8X6H6i4U", "Animasi Edukasi Kok Bisa", "Edukasi Sains Visual")
content = replace_videos(content, "Kinestetik (Senam & Eksperimen)", "8-9m2iB0iM4", "j4mG5O-uG4A", "Senam Anak", "Eksperimen Sains Anak")

with open('rekomendasi.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated rekomendasi.html to display 2 side-by-side YouTube videos for each learning style.")
