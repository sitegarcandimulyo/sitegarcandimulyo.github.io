import re

files_to_check = ['rekomendasi.html', 'sumber.html', 'larikelas6.html']

for filepath in files_to_check:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Fix multiline strings in the javascript object declarations inside the Word download function
        # For example: platform: "Text\nText" -> platform: `Text\nText`
        # Since using regex for this is tricky, I will explicitly replace the known broken strings

        broken_visual = '''{ kategori: "Interactive Learning Apps", platform: "Quick Draw! (Game Tebak Gambar)
Canva untuk Anak
Let's Read Asia (Buku Cerita Bergambar)" },
                    { kategori: "DIY Project Platforms", platform: "Kok Bisa? (Video Edukasi Animasi)
Hujan Tanda Tanya (Sains Visual)
Art for Kids Hub" },
                    { kategori: "Virtual Labs", platform: "Google Earth (Eksplorasi Peta)
PhET (Simulasi Geometri & Optik)" }'''

        fixed_visual = '''{ kategori: "Interactive Learning Apps", platform: "Quick Draw! (Game Tebak Gambar)\\nCanva untuk Anak\\nLet's Read Asia (Buku Cerita Bergambar)" },
                    { kategori: "DIY Project Platforms", platform: "Kok Bisa? (Video Edukasi Animasi)\\nHujan Tanda Tanya (Sains Visual)\\nArt for Kids Hub" },
                    { kategori: "Virtual Labs", platform: "Google Earth (Eksplorasi Peta)\\nPhET (Simulasi Geometri & Optik)" }'''

        broken_auditory = '''{ kategori: "Interactive Learning Apps", platform: "Nussa (Cerita & Lagu Anak)
Lagu Anak Indonesia Edukasi
Quizizz (Kuis Bersuara)" },
                    { kategori: "DIY Project Platforms", platform: "Let's Read Asia (Buku Bersuara)
Podcast Cerita Anak (Spotify)
Chrome Music Lab" },
                    { kategori: "Virtual Labs", platform: "PhET (Simulasi Gelombang & Suara)
Labster (Virtual Lab Interaktif)" }'''

        fixed_auditory = '''{ kategori: "Interactive Learning Apps", platform: "Nussa (Cerita & Lagu Anak)\\nLagu Anak Indonesia Edukasi\\nQuizizz (Kuis Bersuara)" },
                    { kategori: "DIY Project Platforms", platform: "Let's Read Asia (Buku Bersuara)\\nPodcast Cerita Anak (Spotify)\\nChrome Music Lab" },
                    { kategori: "Virtual Labs", platform: "PhET (Simulasi Gelombang & Suara)\\nLabster (Virtual Lab Interaktif)" }'''

        broken_kines = '''{ kategori: "Interactive Learning Apps", platform: "Wordwall (Kuis Aktif Geser & Tarik)
Kahoot! (Kuis Kompetisi)
Minecraft Education" },
                    { kategori: "DIY Project Platforms", platform: "Video Senam Anak SD Ceria
Video Eksperimen Sains Anak
Instructables (Proyek Prakarya)" },
                    { kategori: "Virtual Labs", platform: "PhET Simulasi Interaktif
ChemCollective (Eksperimen Campur Warna)" }'''

        fixed_kines = '''{ kategori: "Interactive Learning Apps", platform: "Wordwall (Kuis Aktif Geser & Tarik)\\nKahoot! (Kuis Kompetisi)\\nMinecraft Education" },
                    { kategori: "DIY Project Platforms", platform: "Video Senam Anak SD Ceria\\nVideo Eksperimen Sains Anak\\nInstructables (Proyek Prakarya)" },
                    { kategori: "Virtual Labs", platform: "PhET Simulasi Interaktif\\nChemCollective (Eksperimen Campur Warna)" }'''

        if broken_visual in content:
            content = content.replace(broken_visual, fixed_visual)
        if broken_auditory in content:
            content = content.replace(broken_auditory, fixed_auditory)
        if broken_kines in content:
            content = content.replace(broken_kines, fixed_kines)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed JS multiline string syntax errors in {filepath}")
    except FileNotFoundError:
        pass
