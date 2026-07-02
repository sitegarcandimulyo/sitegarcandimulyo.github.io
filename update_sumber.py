import re

with open('sumber.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Auditory Section
auditory_replacement = """        <div id="auditory-source" class="source-section">
            <h2>Selamat Datang di Dunia Auditori! 🎧</h2>
            <p class="intro-text">Wah, telingamu sangat peka seperti pahlawan super! Setiap suara dan nada adalah kunci ajaibmu untuk belajar banyak hal baru.</p>
            
            <h3>Deskripsi Gaya Belajar Auditori</h3>
            <p>Kamu adalah sang <strong>Pendengar Hebat</strong>! Anak dengan gaya belajar Auditori paling mudah memahami pelajaran dengan cara mendengarkan. Kamu mungkin sangat suka mendengarkan dongeng, bernyanyi, menghafal lewat lagu, atau mengobrol bersama teman dan guru. Suara yang kamu dengar akan menempel kuat di ingatanmu!</p>

            <div class="tips-section" style="background-color: #fff3e0; border-left: 5px solid #ff9800; padding: 15px; border-radius: 8px; margin-bottom: 20px;">
                <h4 style="color: #e65100;">🌟 Kata-Kata Semangat Untukmu!</h4>
                <p style="font-style: italic; color: #424242;">"Teruslah bernyanyi, bercerita, dan mendengarkan hal-hal hebat. Jadikan suaramu sebagai kekuatanmu untuk meraih mimpi. Semangat belajarnya, jagoan!"</p>
            </div>

            <div class="tips-section">
                <h4>Cara Belajar Paling Seru:</h4>
                <ul>
                    <li>Minta ayah, ibu, atau gurumu untuk membacakan buku pelajaran seperti sedang bercerita.</li>
                    <li>Ubah hafalan rumus atau nama-nama penting menjadi lagu yang asyik.</li>
                    <li>Sering-seringlah mengobrol dan berdiskusi tentang apa yang baru saja kamu pelajari.</li>
                    <li>Rekam suaramu saat membaca buku, lalu dengarkan lagi sebelum tidur.</li>
                </ul>
            </div>

            <div class="reco-item">
                <h4>1. Dongeng & Cerita Anak Bersuara</h4>
                <p>Kumpulan cerita dan dongeng seru yang bisa kamu dengarkan.</p>
                <div class="source-links">
                    <a href="https://open.spotify.com/genre/kids-family" target="_blank"><i class="fab fa-spotify"></i> Spotify Kids Cerita Anak</a>
                    <a href="https://reader.letsreadasia.org/" target="_blank"><i class="fas fa-book-reader"></i> Let's Read Asia (Buku Bersuara)</a>
                </div>
            </div>

            <div class="reco-item">
                <h4>2. Video & Lagu Edukasi Anak</h4>
                <p>Belajar membaca, berhitung, dan sains melalui nyanyian dan nada.</p>
                <div class="source-links">
                    <a href="https://www.youtube.com/c/LaguAnakIndonesiaBalita" target="_blank"><i class="fab fa-youtube"></i> Lagu Anak Indonesia Edukasi</a>
                    <a href="https://www.youtube.com/c/NussaOfficial" target="_blank"><i class="fab fa-youtube"></i> Nussa (Cerita & Lagu)</a>
                </div>
            </div>
        </div>"""

content = re.sub(r'<div id="auditory-source" class="source-section">.*?</div>\s*<div id="visual-source"', auditory_replacement + '\n\n        <div id="visual-source"', content, flags=re.DOTALL)


# Replace Visual Section
visual_replacement = """        <div id="visual-source" class="source-section">
            <h2>Selamat Datang di Dunia Visual! 🎨</h2>
            <p class="intro-text">Hebat sekali! Matamu bisa menangkap warna dan gambar bagaikan kamera canggih! Dunia ini penuh dengan warna untukmu.</p>
            
            <h3>Deskripsi Gaya Belajar Visual</h3>
            <p>Kamu adalah sang <strong>Pengamat Cerdas</strong>! Anak dengan gaya belajar Visual sangat mudah mengingat apa yang mereka lihat. Kamu menyukai gambar, warna-warni, poster, grafik, dan video animasi. Saat kamu melihat sesuatu yang indah dan rapi, otakmu akan merekamnya dengan sangat cepat!</p>

            <div class="tips-section" style="background-color: #e3f2fd; border-left: 5px solid #2196f3; padding: 15px; border-radius: 8px; margin-bottom: 20px;">
                <h4 style="color: #0d47a1;">🌟 Kata-Kata Semangat Untukmu!</h4>
                <p style="font-style: italic; color: #424242;">"Ayo warnai dunia belajarmu dengan kreativitas tanpa batas! Jangan takut untuk mencoret-coret dan menggambar masa depanmu. Tetap semangat, sang pelukis hebat!"</p>
            </div>

            <div class="tips-section">
                <h4>Cara Belajar Paling Seru:</h4>
                <ul>
                    <li>Gunakan spidol atau pensil warna-warni untuk menandai tulisan penting di bukumu.</li>
                    <li>Gambarkan pelajaran yang sulit menjadi komik atau peta pikiran (mind map).</li>
                    <li>Tempelkan poster-poster gambar edukasi di dinding kamarmu.</li>
                    <li>Tonton video animasi pendidikan agar pelajaran terasa seperti menonton kartun.</li>
                </ul>
            </div>

            <div class="reco-item">
                <h4>1. Animasi Sains & Pengetahuan Anak</h4>
                <p>Penjelasan ilmu pengetahuan lewat gambar animasi yang sangat seru.</p>
                <div class="source-links">
                    <a href="https://www.youtube.com/c/KokBisa" target="_blank"><i class="fab fa-youtube"></i> Kok Bisa? (Animasi Sains)</a>
                    <a href="https://www.youtube.com/c/HujanTandaTanya" target="_blank"><i class="fab fa-youtube"></i> Hujan Tanda Tanya</a>
                </div>
            </div>

            <div class="reco-item">
                <h4>2. Platform Menggambar & Visual Anak</h4>
                <p>Aplikasi dan web seru untuk membuat karya visual dan peta pikiran.</p>
                <div class="source-links">
                    <a href="https://www.canva.com/id_id/pendidikan/" target="_blank"><i class="fas fa-palette"></i> Canva untuk Anak</a>
                    <a href="https://quickdraw.withgoogle.com/" target="_blank"><i class="fas fa-pencil-alt"></i> Quick, Draw! (Game Tebak Gambar)</a>
                </div>
            </div>
        </div>"""

content = re.sub(r'<div id="visual-source" class="source-section">.*?</div>\s*<div id="kinesthetic-source"', visual_replacement + '\n\n        <div id="kinesthetic-source"', content, flags=re.DOTALL)


# Replace Kinesthetic Section
kinesthetic_replacement = """        <div id="kinesthetic-source" class="source-section">
            <h2>Selamat Datang di Dunia Kinestetik! 🏃‍♂️</h2>
            <p class="intro-text">Wow, energimu sungguh luar biasa seperti atlet juara! Seluruh tubuhmu siap membawamu belajar lewat petualangan seru.</p>
            
            <h3>Deskripsi Gaya Belajar Kinestetik</h3>
            <p>Kamu adalah sang <strong>Penjelajah Aktif</strong>! Anak dengan gaya belajar Kinestetik tidak suka hanya duduk diam. Kamu belajar paling baik saat tangan dan tubuhmu bergerak. Menyentuh benda, berlarian, merakit mainan, dan melakukan eksperimen langsung adalah cara paling ampuh buatmu untuk pintar!</p>

            <div class="tips-section" style="background-color: #fce4ec; border-left: 5px solid #e91e63; padding: 15px; border-radius: 8px; margin-bottom: 20px;">
                <h4 style="color: #880e4f;">🌟 Kata-Kata Semangat Untukmu!</h4>
                <p style="font-style: italic; color: #424242;">"Dunia ini adalah tempat bermain dan laboratorium raksasamu! Jangan pernah lelah bergerak, mencoba, dan berkreasi. Maju terus, sang penjelajah hebat!"</p>
            </div>

            <div class="tips-section">
                <h4>Cara Belajar Paling Seru:</h4>
                <ul>
                    <li>Belajarlah sambil berjalan-jalan di sekitar ruangan atau sambil memantulkan bola.</li>
                    <li>Gunakan balok mainan, plastisin, atau benda-benda nyata saat belajar menghitung.</li>
                    <li>Beristirahatlah sebentar setiap 15 menit untuk meregangkan badan atau melompat.</li>
                    <li>Minta guru atau orang tua mengajakmu melakukan eksperimen langsung (misal: mencampur warna air).</li>
                </ul>
            </div>

            <div class="reco-item">
                <h4>1. Bermain Sambil Belajar (Game Aktif)</h4>
                <p>Website permainan edukatif interaktif yang membuatmu harus mengklik, menarik, dan berpikir cepat.</p>
                <div class="source-links">
                    <a href="https://wordwall.net/id" target="_blank"><i class="fas fa-gamepad"></i> Wordwall (Game Kuis Interaktif)</a>
                    <a href="https://phet.colorado.edu/in/simulations/filter?subjects=math,physics,chemistry,biology&levels=elementary-school" target="_blank"><i class="fas fa-flask"></i> PhET Simulasi Interaktif</a>
                </div>
            </div>

            <div class="reco-item">
                <h4>2. Aktivitas Gerak & Senam Otak Anak</h4>
                <p>Panduan gerak agar badan sehat dan otak cerdas saat istirahat belajar.</p>
                <div class="source-links">
                    <a href="https://www.youtube.com/results?search_query=senam+anak+sd+ceria" target="_blank"><i class="fab fa-youtube"></i> Senam Pagi Ceria Anak SD</a>
                    <a href="https://www.youtube.com/results?search_query=eksperimen+sains+anak+sd" target="_blank"><i class="fab fa-youtube"></i> Eksperimen Sains Anak</a>
                </div>
            </div>
        </div>"""

content = re.sub(r'<div id="kinesthetic-source" class="source-section">.*?</div>\s*<p>Informasi mengenai gaya belajar ini', kinesthetic_replacement + '\n\n        <p>Informasi mengenai gaya belajar ini', content, flags=re.DOTALL)

with open('sumber.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated sumber.html with detailed learning style descriptions, encouragement, and links tailored for elementary students.")
