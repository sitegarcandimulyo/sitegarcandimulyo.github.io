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
                    <li>Minta orang tua atau guru membacakan materi pelajaran seperti sedang bercerita.</li>
                    <li>Ubah hafalan yang sulit menjadi lirik lagu atau nyanyian yang asyik.</li>
                    <li>Rekam suaramu saat membaca buku, lalu dengarkan lagi sebelum tidur.</li>
                    <li>Ajak teman-teman berdiskusi atau melakukan tanya jawab secara langsung.</li>
                    <li>Gunakan tepukan tangan atau ketukan meja untuk menghafal ejaan dan angka.</li>
                </ul>
            </div>

            <div class="reco-item">
                <h4>Interactive Learning Apps</h4>
                <p>Aplikasi pembelajaran interaktif (Termasuk video & lagu edukasi anak).</p>
                <div class="source-links">
                    <a href="https://www.youtube.com/c/NussaOfficial" target="_blank"><i class="fas fa-play-circle"></i> Nussa (Cerita & Lagu Anak)</a>
                    <a href="https://www.youtube.com/c/LaguAnakIndonesiaBalita" target="_blank"><i class="fas fa-music"></i> Lagu Anak Indonesia Edukasi</a>
                    <a href="https://quizizz.com/" target="_blank"><i class="fas fa-gamepad"></i> Quizizz (Kuis Bersuara)</a>
                </div>
            </div>

            <div class="reco-item">
                <h4>DIY Project Platforms</h4>
                <p>Platform untuk proyek pembelajaran hands-on dan mendengarkan cerita.</p>
                <div class="source-links">
                    <a href="https://reader.letsreadasia.org/" target="_blank"><i class="fas fa-book-reader"></i> Let's Read Asia (Buku Bersuara)</a>
                    <a href="https://open.spotify.com/genre/kids-family" target="_blank"><i class="fab fa-spotify"></i> Podcast Cerita Anak (Spotify)</a>
                    <a href="https://musiclab.chromeexperiments.com/" target="_blank"><i class="fas fa-guitar"></i> Chrome Music Lab</a>
                </div>
            </div>

            <div class="reco-item">
                <h4>Virtual Labs</h4>
                <p>Laboratorium virtual untuk eksperimen (Fokus pada suara dan pendengaran).</p>
                <div class="source-links">
                    <a href="https://phet.colorado.edu/in/simulations/filter?subjects=sound" target="_blank"><i class="fas fa-wave-square"></i> PhET (Simulasi Gelombang & Suara)</a>
                    <a href="https://www.labster.com/" target="_blank"><i class="fas fa-microscope"></i> Labster (Virtual Lab Interaktif)</a>
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
                    <li>Gunakan spidol dan stabilo warna-warni untuk menandai kalimat penting di buku.</li>
                    <li>Buatlah peta pikiran (mind map) yang penuh dengan gambar dan warna.</li>
                    <li>Tonton video animasi atau dokumenter edukasi agar pelajaran mudah diingat.</li>
                    <li>Tempelkan poster-poster gambar edukasi di dinding kamarmu.</li>
                    <li>Buat flashcard (kartu pintar) dengan gambar dan tulisan berwarna cerah.</li>
                </ul>
            </div>

            <div class="reco-item">
                <h4>Interactive Learning Apps</h4>
                <p>Aplikasi pembelajaran interaktif (Termasuk akses gambar & game visual).</p>
                <div class="source-links">
                    <a href="https://quickdraw.withgoogle.com/" target="_blank"><i class="fas fa-pencil-alt"></i> Quick, Draw! (Game Tebak Gambar)</a>
                    <a href="https://www.canva.com/id_id/pendidikan/" target="_blank"><i class="fas fa-palette"></i> Canva untuk Anak</a>
                    <a href="https://reader.letsreadasia.org/" target="_blank"><i class="fas fa-book-open"></i> Let's Read Asia (Buku Cerita Bergambar)</a>
                </div>
            </div>

            <div class="reco-item">
                <h4>DIY Project Platforms</h4>
                <p>Platform untuk proyek pembelajaran hands-on (Fokus pada animasi dan warna).</p>
                <div class="source-links">
                    <a href="https://www.youtube.com/c/KokBisa" target="_blank"><i class="fab fa-youtube"></i> Kok Bisa? (Video Edukasi Animasi)</a>
                    <a href="https://www.youtube.com/c/HujanTandaTanya" target="_blank"><i class="fab fa-youtube"></i> Hujan Tanda Tanya (Sains Visual)</a>
                    <a href="https://www.artforkidshub.com/" target="_blank"><i class="fas fa-paint-brush"></i> Art for Kids Hub (Tutorial Gambar)</a>
                </div>
            </div>

            <div class="reco-item">
                <h4>Virtual Labs</h4>
                <p>Laboratorium virtual untuk eksperimen berbasis grafis dan pemetaan.</p>
                <div class="source-links">
                    <a href="https://earth.google.com/" target="_blank"><i class="fas fa-globe-americas"></i> Google Earth (Eksplorasi Peta)</a>
                    <a href="https://phet.colorado.edu/" target="_blank"><i class="fas fa-shapes"></i> PhET (Simulasi Geometri & Optik)</a>
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
                    <li>Gunakan balok mainan, plastisin, atau stik es krim saat belajar berhitung.</li>
                    <li>Lakukan eksperimen nyata dan sentuh langsung benda yang sedang dipelajari.</li>
                    <li>Beristirahatlah sebentar setiap 15-20 menit untuk melompat atau meregangkan badan.</li>
                    <li>Bermain peran (role-play) dengan teman untuk mempraktikkan materi pelajaran.</li>
                </ul>
            </div>

            <div class="reco-item">
                <h4>Interactive Learning Apps</h4>
                <p>Aplikasi pembelajaran interaktif yang harus disentuh, ditarik, dan digeser.</p>
                <div class="source-links">
                    <a href="https://wordwall.net/id" target="_blank"><i class="fas fa-hand-pointer"></i> Wordwall (Kuis Aktif Geser & Tarik)</a>
                    <a href="https://kahoot.com/" target="_blank"><i class="fas fa-gamepad"></i> Kahoot! (Kuis Kompetisi Aktif)</a>
                    <a href="https://education.minecraft.net/" target="_blank"><i class="fas fa-cubes"></i> Minecraft Education (Bangun Balok)</a>
                </div>
            </div>

            <div class="reco-item">
                <h4>DIY Project Platforms</h4>
                <p>Platform untuk proyek pembelajaran hands-on (Senam dan Eksperimen Nyata).</p>
                <div class="source-links">
                    <a href="https://www.youtube.com/results?search_query=senam+anak+sd+ceria" target="_blank"><i class="fas fa-child"></i> Video Senam Anak SD Ceria</a>
                    <a href="https://www.youtube.com/results?search_query=eksperimen+sains+anak+sd" target="_blank"><i class="fas fa-rocket"></i> Video Eksperimen Sains Anak</a>
                    <a href="https://www.instructables.com/craft/" target="_blank"><i class="fas fa-hammer"></i> Instructables (Proyek Prakarya)</a>
                </div>
            </div>

            <div class="reco-item">
                <h4>Virtual Labs</h4>
                <p>Laboratorium virtual untuk eksperimen langsung di layarmu.</p>
                <div class="source-links">
                    <a href="https://phet.colorado.edu/" target="_blank"><i class="fas fa-flask"></i> PhET Simulasi Interaktif</a>
                    <a href="https://chemcollective.org/" target="_blank"><i class="fas fa-vial"></i> ChemCollective (Eksperimen Campur Warna)</a>
                </div>
            </div>
        </div>"""

content = re.sub(r'<div id="kinesthetic-source" class="source-section">.*?</div>\s*<p>Informasi mengenai gaya belajar ini', kinesthetic_replacement + '\n\n        <p>Informasi mengenai gaya belajar ini', content, flags=re.DOTALL)

with open('sumber.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated sumber.html to merge Indonesian learning apps into the requested formatting.")
