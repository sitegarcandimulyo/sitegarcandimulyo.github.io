import re
import json

with open('larikelas6.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update TOTAL_STEPS
content = re.sub(r'var TOTAL_STEPS = \d+;', 'var TOTAL_STEPS = 15;', content)

# 15 selected questions
new_questions = """        var questions = [
            {
                q: "Ketika saya merakit mainan atau sesuatu, saya lebih suka...",
                a: [
                    { text: "Mengikuti gambar atau petunjuk tertulis.", type: 'V' },
                    { text: "Mendengarkan instruksi dari orang lain.", type: 'A' },
                    { text: "Langsung mencoba merakitnya sendiri.", type: 'K' }
                ]
            },
            {
                q: "Saat belajar pelajaran baru di kelas, saya paling ingat jika...",
                a: [
                    { text: "Melihatnya dari buku cerita bergambar atau video.", type: 'V' },
                    { text: "Mendengarkan penjelasan dari guru atau teman.", type: 'A' },
                    { text: "Mencoba mempraktikkannya secara langsung.", type: 'K' }
                ]
            },
            {
                q: "Apa yang paling mungkin mengganggu saya saat sedang belajar?",
                a: [
                    { text: "Melihat pemandangan di luar jendela atau orang lewat.", type: 'V' },
                    { text: "Mendengar suara berisik atau teman mengobrol.", type: 'A' },
                    { text: "Harus duduk diam terlalu lama tanpa bergerak.", type: 'K' }
                ]
            },
            {
                q: "Ketika saya punya teman baru, saya paling mudah mengingat...",
                a: [
                    { text: "Wajah mereka dan baju yang mereka pakai.", type: 'V' },
                    { text: "Nama mereka atau suara mereka.", type: 'A' },
                    { text: "Permainan yang kami lakukan bersama.", type: 'K' }
                ]
            },
            {
                q: "Saya lebih suka membaca...",
                a: [
                    { text: "Buku dengan banyak gambar dan warna.", type: 'V' },
                    { text: "Mendengarkan orang lain membacakan cerita untuk saya.", type: 'A' },
                    { text: "Buku cerita petualangan yang seru.", type: 'K' }
                ]
            },
            {
                q: "Saat menunjukkan jalan ke suatu tempat, saya biasanya...",
                a: [
                    { text: "Menggambar peta di kertas.", type: 'V' },
                    { text: "Memberitahu dengan kata-kata (belok kanan, kiri).", type: 'A' },
                    { text: "Berjalan bersama teman untuk menunjukkan langsung.", type: 'K' }
                ]
            },
            {
                q: "Di waktu istirahat atau hari libur, saya lebih suka...",
                a: [
                    { text: "Menonton film kartun atau menggambar.", type: 'V' },
                    { text: "Mendengarkan lagu atau bercerita.", type: 'A' },
                    { text: "Bermain bola, lari-larian, atau bersepeda.", type: 'K' }
                ]
            },
            {
                q: "Jika saya harus menghafal pelajaran, saya akan...",
                a: [
                    { text: "Membacanya berulang kali atau membuat catatan warna-warni.", type: 'V' },
                    { text: "Menghafalnya dengan suara keras atau seperti bernyanyi.", type: 'A' },
                    { text: "Menghafal sambil berjalan bolak-balik.", type: 'K' }
                ]
            },
            {
                q: "Saat mencoba mengeja kata yang sulit, saya...",
                a: [
                    { text: "Membayangkan huruf-hurufnya di kepala saya.", type: 'V' },
                    { text: "Menyebutkan hurufnya keras-keras satu per satu.", type: 'A' },
                    { text: "Menulisnya di kertas dulu agar tahu benar atau salah.", type: 'K' }
                ]
            },
            {
                q: "Ketika mengingat kejadian lucu atau seru, saya paling ingat...",
                a: [
                    { text: "Seperti apa tempat kejadiannya dan apa yang saya lihat.", type: 'V' },
                    { text: "Apa yang dikatakan teman-teman saat itu.", type: 'A' },
                    { text: "Apa yang saya lakukan dan bagaimana perasaan saya.", type: 'K' }
                ]
            },
            {
                q: "Saya lebih suka jika bapak/ibu guru...",
                a: [
                    { text: "Menggunakan papan tulis, poster, atau proyektor.", type: 'V' },
                    { text: "Bercerita dengan seru dan mengajak tanya jawab.", type: 'A' },
                    { text: "Mengajak bermain tebak-tebakan atau praktek langsung.", type: 'K' }
                ]
            },
            {
                q: "Ketika saya merasa bosan di kelas, saya biasanya...",
                a: [
                    { text: "Mencoret-coret atau menggambar di buku.", type: 'V' },
                    { text: "Mengobrol dengan teman sebelah atau bersenandung pelan.", type: 'A' },
                    { text: "Menggoyangkan kaki, bermain pensil, atau ingin jalan-jalan.", type: 'K' }
                ]
            },
            {
                q: "Saya belajar berhitung atau matematika paling baik dengan...",
                a: [
                    { text: "Melihat guru menuliskan cara berhitung di papan tulis.", type: 'V' },
                    { text: "Mendengarkan guru menjelaskan langkah-langkahnya.", type: 'A' },
                    { text: "Menggunakan jari, lidi, atau balok untuk menghitung langsung.", type: 'K' }
                ]
            },
            {
                q: "Saya ingat kalau ada PR (Pekerjaan Rumah) dengan cara...",
                a: [
                    { text: "Melihat catatan yang saya tulis di buku tulis.", type: 'V' },
                    { text: "Mengingat ucapan guru sebelum pulang sekolah.", type: 'A' },
                    { text: "Menaruh buku PR di tempat yang pasti akan saya pegang.", type: 'K' }
                ]
            },
            {
                q: "Ketika saya sedang sangat gembira atau sedih, saya lebih suka...",
                a: [
                    { text: "Menulisnya di buku harian atau menggambar.", type: 'V' },
                    { text: "Bercerita kepada orang tua atau sahabat.", type: 'A' },
                    { text: "Berlari, melompat kegirangan, atau bermain di luar.", type: 'K' }
                ]
            }
        ];"""

# Replace the whole questions array
# Find the start and end of the questions array
start_idx = content.find('var questions = [')
end_idx = content.find('];', start_idx) + 2

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + new_questions + content[end_idx:]

with open('larikelas6.html', 'w', encoding='utf-8') as f:
    f.write(content)
