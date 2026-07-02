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
                <p>Aplikasi pembelajaran interaktif yang kaya akan panduan suara dan lagu.</p>
                <div class="source-links">
                    <a href="https://www.duolingo.com/" target="_blank"><i class="fas fa-volume-up"></i> Duolingo (Bahasa & Suara)</a>
                    <a href="https://quizizz.com/" target="_blank"><i class="fas fa-gamepad"></i> Quizizz (Kuis Interaktif Bersuara)</a>
                    <a href="https://lingokids.com/" target="_blank"><i class="fas fa-music"></i> Lingokids (Game Edukasi Musikal)</a>
                </div>
            </div>

            <div class="reco-item">
                <h4>DIY Project Platforms</h4>
                <p>Platform untuk proyek pembelajaran hands-on khusus mengeksplorasi bunyi.</p>
                <div class="source-links">
                    <a href="https://musiclab.chromeexperiments.com/" target="_blank"><i class="fas fa-guitar"></i> Chrome Music Lab</a>
                    <a href="https://www.instructables.com/craft/" target="_blank"><i class="fas fa-tools"></i> Instructables (Proyek Alat Musik)</a>
                    <a href="https://www.sciencebuddies.org/" target="_blank"><i class="fas fa-flask"></i> Science Buddies (Eksperimen Suara)</a>
                </div>
            </div>

            <div class="reco-item">
                <h4>Virtual Labs</h4>
                <p>Laboratorium virtual untuk eksperimen yang dilengkapi panduan audio.</p>
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
                <p>Aplikasi pembelajaran interaktif yang penuh warna dan kreasi visual.</p>
                <div class="source-links">
                    <a href="https://www.canva.com/id_id/pendidikan/" target="_blank"><i class="fas fa-palette"></i> Canva for Education</a>
                    <a href="https://kahoot.com/" target="_blank"><i class="fas fa-trophy"></i> Kahoot! (Kuis Visual)</a>
                    <a href="https://www.blooket.com/" target="_blank"><i class="fas fa-ghost"></i> Blooket (Game Edukasi Grafis)</a>
                </div>
            </div>

            <div class="reco-item">
                <h4>DIY Project Platforms</h4>
                <p>Platform untuk proyek pembelajaran hands-on yang melatih kreativitas desain.</p>
                <div class="source-links">
                    <a href="https://diy.org/" target="_blank"><i class="fas fa-paint-brush"></i> DIY.org (Kerajinan Kreatif)</a>
                    <a href="https://www.artforkidshub.com/" target="_blank"><i class="fas fa-pencil-alt"></i> Art for Kids Hub (Tutorial Menggambar)</a>
                    <a href="https://www.origamiway.com/" target="_blank"><i class="fas fa-paper-plane"></i> Origami Way (Melipat Kertas Visual)</a>
                </div>
            </div>

            <div class="reco-item">
                <h4>Virtual Labs</h4>
                <p>Laboratorium virtual untuk eksperimen dengan gambar nyata yang menakjubkan.</p>
                <div class="source-links">
                    <a href="https://earth.google.com/" target="_blank"><i class="fas fa-globe-americas"></i> Google Earth (Eksplorasi Peta)</a>
                    <a href="https://stellarium-web.org/" target="_blank"><i class="fas fa-star"></i> Stellarium Web (Planetarium)</a>
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
                <p>Aplikasi pembelajaran interaktif yang melatih ketangkasan dan kecepatan tangan.</p>
                <div class="source-links">
                    <a href="https://wordwall.net/id" target="_blank"><i class="fas fa-hand-pointer"></i> Wordwall (Game Geser & Tarik)</a>
                    <a href="https://scratch.mit.edu/" target="_blank"><i class="fas fa-code"></i> Scratch (Merakit Blok Animasi)</a>
                    <a href="https://education.minecraft.net/" target="_blank"><i class="fas fa-cubes"></i> Minecraft Education (Bangun Balok)</a>
                </div>
            </div>

            <div class="reco-item">
                <h4>DIY Project Platforms</h4>
                <p>Platform untuk proyek pembelajaran hands-on di mana kamu bisa merakit sesuatu dengan tanganmu sendiri.</p>
                <div class="source-links">
                    <a href="https://www.instructables.com/craft/" target="_blank"><i class="fas fa-hammer"></i> Instructables (Proyek Merakit Mainan)</a>
                    <a href="https://www.sciencebuddies.org/" target="_blank"><i class="fas fa-rocket"></i> Science Buddies (Eksperimen Fisik)</a>
                    <a href="https://makerkids.com/" target="_blank"><i class="fas fa-robot"></i> Maker Kids (Proyek Robotika Dasar)</a>
                </div>
            </div>

            <div class="reco-item">
                <h4>Virtual Labs</h4>
                <p>Laboratorium virtual untuk eksperimen yang bisa kamu atur dan ubah bentuknya secara langsung.</p>
                <div class="source-links">
                    <a href="https://phet.colorado.edu/" target="_blank"><i class="fas fa-flask"></i> PhET (Simulasi Interaktif Penuh)</a>
                    <a href="https://chemcollective.org/" target="_blank"><i class="fas fa-vial"></i> ChemCollective (Eksperimen Campur Warna)</a>
                    <a href="https://www.hhmi.org/biointeractive/virtual-biology-lab" target="_blank"><i class="fas fa-leaf"></i> Virtual Biology Lab</a>
                </div>
            </div>
        </div>"""

content = re.sub(r'<div id="kinesthetic-source" class="source-section">.*?</div>\s*<p>Informasi mengenai gaya belajar ini', kinesthetic_replacement + '\n\n        <p>Informasi mengenai gaya belajar ini', content, flags=re.DOTALL)

with open('sumber.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated sumber.html to strictly use requested formatting and specific 5 points and categories.")
