import re

with open('sumber.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = """                <ul>
                    <li>Gunakan spidol dan stabilo warna-warni untuk menandai kalimat penting di buku.</li>
                    <li>Buatlah peta pikiran (mind map) yang penuh dengan gambar dan warna.</li>
                    <li>Tonton video animasi atau dokumenter edukasi agar pelajaran mudah diingat.</li>
                    <li>Tempelkan poster-poster gambar edukasi di dinding kamarmu.</li>
                    <li>Buat flashcard (kartu pintar) dengan gambar dan tulisan berwarna cerah.</li>
                </ul>"""

replacement = """                <ul>
                    <li>Buatlah mind mapping untuk setiap topik baru yang kamu pelajari</li>
                    <li>Gunakan highlighter warna-warni untuk menandai poin penting</li>
                    <li>Tempel poster atau infografis di dinding kamarmu</li>
                    <li>Rekam penjelasan guru dalam bentuk sketsa atau diagram</li>
                    <li>Buat flashcard dengan gambar dan warna menarik</li>
                </ul>"""

if target in content:
    content = content.replace(target, replacement)
    with open('sumber.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Replaced visual learning tips successfully.")
else:
    print("Could not find the target string.")
