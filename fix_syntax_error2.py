import re

files_to_check = ['rekomendasi.html', 'sumber.html']

for filepath in files_to_check:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Fix multiline strings by converting the " to ` for the platform field
        
        broken_visual = '''{ kategori: "Interactive Learning Apps", platform: "Quick Draw! (Game Tebak Gambar)
Canva untuk Anak
Let's Read Asia (Buku Cerita Bergambar)" },
                    { kategori: "DIY Project Platforms", platform: "Kok Bisa? (Video Edukasi Animasi)
Hujan Tanda Tanya (Sains Visual)
Art for Kids Hub" },
                    { kategori: "Virtual Labs", platform: "Google Earth (Eksplorasi Peta)
PhET (Simulasi Geometri & Optik)" }'''

        fixed_visual = '''{ kategori: "Interactive Learning Apps", platform: `Quick Draw! (Game Tebak Gambar)
Canva untuk Anak
Let's Read Asia (Buku Cerita Bergambar)` },
                    { kategori: "DIY Project Platforms", platform: `Kok Bisa? (Video Edukasi Animasi)
Hujan Tanda Tanya (Sains Visual)
Art for Kids Hub` },
                    { kategori: "Virtual Labs", platform: `Google Earth (Eksplorasi Peta)
PhET (Simulasi Geometri & Optik)` }'''

        broken_auditory = '''{ kategori: "Interactive Learning Apps", platform: "Nussa (Cerita & Lagu Anak)
Lagu Anak Indonesia Edukasi
Quizizz (Kuis Bersuara)" },
                    { kategori: "DIY Project Platforms", platform: "Let's Read Asia (Buku Bersuara)
Podcast Cerita Anak (Spotify)
Chrome Music Lab" },
                    { kategori: "Virtual Labs", platform: "PhET (Simulasi Gelombang & Suara)
Labster (Virtual Lab Interaktif)" }'''

        fixed_auditory = '''{ kategori: "Interactive Learning Apps", platform: `Nussa (Cerita & Lagu Anak)
Lagu Anak Indonesia Edukasi
Quizizz (Kuis Bersuara)` },
                    { kategori: "DIY Project Platforms", platform: `Let's Read Asia (Buku Bersuara)
Podcast Cerita Anak (Spotify)
Chrome Music Lab` },
                    { kategori: "Virtual Labs", platform: `PhET (Simulasi Gelombang & Suara)
Labster (Virtual Lab Interaktif)` }'''

        broken_kines = '''{ kategori: "Interactive Learning Apps", platform: "Wordwall (Kuis Aktif Geser & Tarik)
Kahoot! (Kuis Kompetisi)
Minecraft Education" },
                    { kategori: "DIY Project Platforms", platform: "Video Senam Anak SD Ceria
Video Eksperimen Sains Anak
Instructables (Proyek Prakarya)" },
                    { kategori: "Virtual Labs", platform: "PhET Simulasi Interaktif
ChemCollective (Eksperimen Campur Warna)" }'''

        fixed_kines = '''{ kategori: "Interactive Learning Apps", platform: `Wordwall (Kuis Aktif Geser & Tarik)
Kahoot! (Kuis Kompetisi)
Minecraft Education` },
                    { kategori: "DIY Project Platforms", platform: `Video Senam Anak SD Ceria
Video Eksperimen Sains Anak
Instructables (Proyek Prakarya)` },
                    { kategori: "Virtual Labs", platform: `PhET Simulasi Interaktif
ChemCollective (Eksperimen Campur Warna)` }'''

        content = content.replace(broken_visual, fixed_visual)
        content = content.replace(broken_auditory, fixed_auditory)
        content = content.replace(broken_kines, fixed_kines)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed JS multiline string syntax errors in {filepath} using backticks")
    except FileNotFoundError:
        pass
