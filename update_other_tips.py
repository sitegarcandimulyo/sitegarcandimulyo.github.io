import re

with open('sumber.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Auditory Tips
target_auditory = """                <ul>
                    <li>Minta orang tua atau guru membacakan materi pelajaran seperti sedang bercerita.</li>
                    <li>Ubah hafalan yang sulit menjadi lirik lagu atau nyanyian yang asyik.</li>
                    <li>Rekam suaramu saat membaca buku, lalu dengarkan lagi sebelum tidur.</li>
                    <li>Ajak teman-teman berdiskusi atau melakukan tanya jawab secara langsung.</li>
                    <li>Gunakan tepukan tangan atau ketukan meja untuk menghafal ejaan dan angka.</li>
                </ul>"""

replacement_auditory = """                <ul>
                    <li>Rekam suaramu saat membaca materi lalu dengarkan kembali sebelum tidur</li>
                    <li>Gunakan irama atau lagu asyik untuk menghafal rumus dan istilah penting</li>
                    <li>Ajak teman atau orang tua untuk berdiskusi tentang topik pelajaran baru</li>
                    <li>Bacalah buku pelajaran dengan suara lantang layaknya sedang bercerita</li>
                    <li>Buatlah kelompok belajar kecil untuk saling melakukan tanya jawab langsung</li>
                </ul>"""

if target_auditory in content:
    content = content.replace(target_auditory, replacement_auditory)
else:
    print("Auditory target not found!")

# Replace Kinesthetic Tips
target_kinesthetic = """                <ul>
                    <li>Belajarlah sambil berjalan-jalan di sekitar ruangan atau sambil memantulkan bola.</li>
                    <li>Gunakan balok mainan, plastisin, atau stik es krim saat belajar berhitung.</li>
                    <li>Lakukan eksperimen nyata dan sentuh langsung benda yang sedang dipelajari.</li>
                    <li>Beristirahatlah sebentar setiap 15-20 menit untuk melompat atau meregangkan badan.</li>
                    <li>Bermain peran (role-play) dengan teman untuk mempraktikkan materi pelajaran.</li>
                </ul>"""

replacement_kinesthetic = """                <ul>
                    <li>Lakukan eksperimen secara langsung untuk menguji teori yang sedang dibahas</li>
                    <li>Gunakan gerakan tubuh atau berjalan-jalan kecil saat sedang menghafal sesuatu</li>
                    <li>Ambil waktu istirahat sejenak di sela belajar untuk sekadar meregangkan badan</li>
                    <li>Buatlah model atau prakarya dari benda nyata terkait topik yang dipelajari</li>
                    <li>Mainkan peran (role-play) bersama teman untuk mengingat sejarah atau cerita</li>
                </ul>"""

if target_kinesthetic in content:
    content = content.replace(target_kinesthetic, replacement_kinesthetic)
else:
    print("Kinesthetic target not found!")

with open('sumber.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated Auditory and Kinesthetic learning tips to match the requested style.")
