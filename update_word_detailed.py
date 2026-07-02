import re

def update_detailed_word_export(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        func_pattern = re.compile(r'async function downloadHasilLengkapWord\(\) \{.*?(?=</script>)', re.DOTALL)
        
        # We will use python raw string to avoid escaping issues
        new_func = r"""async function downloadHasilLengkapWord() {
            const { Document, Packer, Paragraph, Table, TableRow, TableCell, AlignmentType, WidthType, ShadingType, HeadingLevel, TextRun, BorderStyle } = docx;

            const urlParams = new URLSearchParams(window.location.search);
            const playerName = urlParams.get('name') || 'Siswa';
            const dominantStyle = urlParams.get('style') || 'Umum';
            const vCount = parseInt(urlParams.get('v')) || 0;
            const aCount = parseInt(urlParams.get('a')) || 0;
            const kCount = parseInt(urlParams.get('k')) || 0;

            const totalQuestions = vCount + aCount + kCount;
            const percentV = totalQuestions > 0 ? ((vCount / totalQuestions) * 100).toFixed(0) : 0;
            const percentA = totalQuestions > 0 ? ((aCount / totalQuestions) * 100).toFixed(0) : 0;
            const percentK = totalQuestions > 0 ? ((kCount / totalQuestions) * 100).toFixed(0) : 0;

            const today = new Date();
            const tanggal = `${today.getDate()}-${today.getMonth() + 1}-${today.getFullYear()}`;

            const children = [];

            // 1. HEADER
            children.push(
                new Paragraph({ text: "LAPORAN ANALISIS GAYA BELAJAR KOMPREHENSIF", heading: HeadingLevel.HEADING_1, alignment: AlignmentType.CENTER, spacing: { after: 400 }, shading: { type: ShadingType.SOLID, color: "4CAF50", fill: "4CAF50" } }),
                new Paragraph({ text: `Nama Siswa: ${playerName}`, spacing: { after: 100 }, bold: true }),
                new Paragraph({ text: `Tanggal Tes: ${tanggal}`, spacing: { after: 100 } }),
                new Paragraph({ text: `Gaya Belajar Dominan: ${dominantStyle}`, spacing: { after: 300 }, bold: true }),
                
                new Paragraph({ text: "1. HASIL EVALUASI KUESIONER", heading: HeadingLevel.HEADING_2, alignment: AlignmentType.LEFT, spacing: { before: 200, after: 200 }, shading: { type: ShadingType.SOLID, color: "2196F3", fill: "2196F3" } }),
                new Paragraph({ text: "Tabel di bawah ini menunjukkan proporsi jawaban Anda berdasarkan tiga gaya belajar utama. Gaya belajar dengan persentase tertinggi merupakan gaya belajar dominan Anda.", spacing: { after: 200 } })
            );

            const resultsTable = new Table({
                width: { size: 100, type: WidthType.PERCENTAGE },
                rows: [
                    new TableRow({
                        children: [
                            new TableCell({ children: [new Paragraph({ text: "Gaya Belajar", bold: true, alignment: AlignmentType.CENTER })], shading: { type: ShadingType.SOLID, color: "2196F3", fill: "2196F3" }, width: { size: 30, type: WidthType.PERCENTAGE } }),
                            new TableCell({ children: [new Paragraph({ text: "Skor", bold: true, alignment: AlignmentType.CENTER })], shading: { type: ShadingType.SOLID, color: "2196F3", fill: "2196F3" }, width: { size: 20, type: WidthType.PERCENTAGE } }),
                            new TableCell({ children: [new Paragraph({ text: "Persentase", bold: true, alignment: AlignmentType.CENTER })], shading: { type: ShadingType.SOLID, color: "2196F3", fill: "2196F3" }, width: { size: 20, type: WidthType.PERCENTAGE } }),
                            new TableCell({ children: [new Paragraph({ text: "Grafik Visual", bold: true, alignment: AlignmentType.CENTER })], shading: { type: ShadingType.SOLID, color: "2196F3", fill: "2196F3" }, width: { size: 30, type: WidthType.PERCENTAGE } })
                        ]
                    }),
                    new TableRow({
                        children: [
                            new TableCell({ children: [new Paragraph({ text: "Visual", alignment: AlignmentType.CENTER, bold: true })], shading: { type: ShadingType.SOLID, color: "E3F2FD", fill: "E3F2FD" } }),
                            new TableCell({ children: [new Paragraph({ text: vCount.toString(), alignment: AlignmentType.CENTER })], shading: { type: ShadingType.SOLID, color: "E3F2FD", fill: "E3F2FD" } }),
                            new TableCell({ children: [new Paragraph({ text: `${percentV}%`, alignment: AlignmentType.CENTER, bold: true })], shading: { type: ShadingType.SOLID, color: "2196F3", fill: "2196F3" } }),
                            new TableCell({ children: [new Paragraph({ text: "█".repeat(Math.round(percentV / 5)), alignment: AlignmentType.LEFT })], shading: { type: ShadingType.SOLID, color: "E3F2FD", fill: "E3F2FD" } })
                        ]
                    }),
                    new TableRow({
                        children: [
                            new TableCell({ children: [new Paragraph({ text: "Auditori", alignment: AlignmentType.CENTER, bold: true })], shading: { type: ShadingType.SOLID, color: "FFF9C4", fill: "FFF9C4" } }),
                            new TableCell({ children: [new Paragraph({ text: aCount.toString(), alignment: AlignmentType.CENTER })], shading: { type: ShadingType.SOLID, color: "FFF9C4", fill: "FFF9C4" } }),
                            new TableCell({ children: [new Paragraph({ text: `${percentA}%`, alignment: AlignmentType.CENTER, bold: true })], shading: { type: ShadingType.SOLID, color: "FBC02D", fill: "FBC02D" } }),
                            new TableCell({ children: [new Paragraph({ text: "█".repeat(Math.round(percentA / 5)), alignment: AlignmentType.LEFT })], shading: { type: ShadingType.SOLID, color: "FFF9C4", fill: "FFF9C4" } })
                        ]
                    }),
                    new TableRow({
                        children: [
                            new TableCell({ children: [new Paragraph({ text: "Kinestetik", alignment: AlignmentType.CENTER, bold: true })], shading: { type: ShadingType.SOLID, color: "F3E5F5", fill: "F3E5F5" } }),
                            new TableCell({ children: [new Paragraph({ text: kCount.toString(), alignment: AlignmentType.CENTER })], shading: { type: ShadingType.SOLID, color: "F3E5F5", fill: "F3E5F5" } }),
                            new TableCell({ children: [new Paragraph({ text: `${percentK}%`, alignment: AlignmentType.CENTER, bold: true })], shading: { type: ShadingType.SOLID, color: "9C27B0", fill: "9C27B0" } }),
                            new TableCell({ children: [new Paragraph({ text: "█".repeat(Math.round(percentK / 5)), alignment: AlignmentType.LEFT })], shading: { type: ShadingType.SOLID, color: "F3E5F5", fill: "F3E5F5" } })
                        ]
                    })
                ]
            });
            children.push(resultsTable);

            const styles = dominantStyle ? dominantStyle.split('/') : [];
            
            // Helper functions for tables
            const createRecoTable = (items, colorHead, colorBody1, colorBody2) => {
                return new Table({
                    width: { size: 100, type: WidthType.PERCENTAGE },
                    rows: [
                        new TableRow({
                            children: [
                                new TableCell({ children: [new Paragraph({ text: "Metode Spesifik", bold: true, alignment: AlignmentType.CENTER })], shading: { type: ShadingType.SOLID, color: colorHead, fill: colorHead }, width: { size: 30, type: WidthType.PERCENTAGE } }),
                                new TableCell({ children: [new Paragraph({ text: "Uraian & Cara Penerapan", bold: true, alignment: AlignmentType.CENTER })], shading: { type: ShadingType.SOLID, color: colorHead, fill: colorHead }, width: { size: 70, type: WidthType.PERCENTAGE } })
                            ]
                        }),
                        ...items.map(res => new TableRow({
                            children: [
                                new TableCell({ children: [new Paragraph({ text: res.metode, bold: true })], shading: { type: ShadingType.SOLID, color: colorBody1, fill: colorBody1 } }),
                                new TableCell({ children: [new Paragraph({ text: res.penjelasan })], shading: { type: ShadingType.SOLID, color: colorBody2, fill: colorBody2 } })
                            ]
                        }))
                    ]
                });
            };

            const createListTable = (items, colorHead, colorBody) => {
                return new Table({
                    width: { size: 100, type: WidthType.PERCENTAGE },
                    rows: [
                        new TableRow({ children: [new TableCell({ children: [new Paragraph({ text: "Panduan Kebiasaan Belajar Harian (Tips Cepat)", bold: true, alignment: AlignmentType.CENTER })], shading: { type: ShadingType.SOLID, color: colorHead, fill: colorHead } })] }),
                        ...items.map(item => new TableRow({ children: [new TableCell({ children: [new Paragraph({ text: `• ${item}`, spacing: { before: 50, after: 50 } })], shading: { type: ShadingType.SOLID, color: colorBody, fill: colorBody } })] }))
                    ]
                });
            };

            const createSourceTableDetailed = (sources, colorHead, colorBody1, colorBody2) => {
                return new Table({
                    width: { size: 100, type: WidthType.PERCENTAGE },
                    rows: [
                        new TableRow({
                            children: [
                                new TableCell({ children: [new Paragraph({ text: "Kategori Platform", bold: true, alignment: AlignmentType.CENTER })], shading: { type: ShadingType.SOLID, color: colorHead, fill: colorHead }, width: { size: 30, type: WidthType.PERCENTAGE } }),
                                new TableCell({ children: [new Paragraph({ text: "Daftar Link & Aplikasi", bold: true, alignment: AlignmentType.CENTER })], shading: { type: ShadingType.SOLID, color: colorHead, fill: colorHead }, width: { size: 40, type: WidthType.PERCENTAGE } }),
                                new TableCell({ children: [new Paragraph({ text: "Manfaat Spesifik", bold: true, alignment: AlignmentType.CENTER })], shading: { type: ShadingType.SOLID, color: colorHead, fill: colorHead }, width: { size: 30, type: WidthType.PERCENTAGE } })
                            ]
                        }),
                        ...sources.map(res => new TableRow({
                            children: [
                                new TableCell({ children: [new Paragraph({ text: res.kategori, bold: true })], shading: { type: ShadingType.SOLID, color: colorBody1, fill: colorBody1 } }),
                                new TableCell({ children: [new Paragraph({ text: res.platform })], shading: { type: ShadingType.SOLID, color: colorBody2, fill: colorBody2 } }),
                                new TableCell({ children: [new Paragraph({ text: res.manfaat })], shading: { type: ShadingType.SOLID, color: colorBody2, fill: colorBody2 } })
                            ]
                        }))
                    ]
                });
            };

            if (styles.includes('Visual')) {
                children.push(new Paragraph({ text: "2. ANALISIS & REKOMENDASI: GAYA BELAJAR VISUAL", heading: HeadingLevel.HEADING_2, alignment: AlignmentType.LEFT, spacing: { before: 400, after: 150 }, shading: { type: ShadingType.SOLID, color: "2196F3", fill: "2196F3" } }));
                children.push(new Paragraph({ text: "Profil Singkat: Sebagai pembelajar visual, Anda menyerap informasi paling optimal melalui apa yang Anda lihat. Gambar, diagram, warna, dan imajinasi keruangan adalah kekuatan utama Anda dalam memahami materi pelajaran.", spacing: { after: 200 } }));

                const visualReco = [
                    { metode: "Pembuatan Peta Konsep (Mind Mapping)", penjelasan: "Buatlah peta konsep secara mandiri. Gunakan berbagai cabang untuk menghubungkan ide pokok dengan detail-detailnya. Tambahkan ikon atau gambar kecil agar otak lebih mudah memanggil memori tersebut saat ujian." },
                    { metode: "Kartu Flash Bergambar", penjelasan: "Gunakan kartu belajar dua sisi. Tulis istilah di satu sisi dan gambarkan wujud atau diagramnya di sisi lain. Ini akan memperkuat hubungan kognitif antara kata dan visual." },
                    { metode: "Eksplorasi Video Animasi", penjelasan: "Sains atau sejarah terkadang membosankan jika hanya dibaca. Tontonlah video dokumenter atau animasi edukasi agar Anda dapat 'melihat' langsung bagaimana konsep tersebut bekerja." },
                    { metode: "Sistem Kode Warna", penjelasan: "Berikan warna pada catatanmu! Gunakan stabilo kuning untuk definisi, hijau untuk contoh, dan merah untuk rumus penting. Warna akan menyortir memori secara otomatis." }
                ];
                children.push(createRecoTable(visualReco, "2196F3", "E3F2FD", "FFFFFF"));
                
                children.push(new Paragraph({ text: "", spacing: { after: 200 } }));
                const visualTips = [
                    "Selalu buat mind mapping berwarna untuk merangkum bab pelajaran yang panjang",
                    "Tandai buku paketmu menggunakan highlighter warna-warni secara konsisten",
                    "Hias dinding kamar belajarmu dengan poster edukasi atau tabel periodik",
                    "Jika guru sedang bercerita, cobalah mencoret-coret sketsa dari cerita tersebut",
                    "Gunakan aplikasi digital berbasis gambar untuk melatih kreativitasmu"
                ];
                children.push(createListTable(visualTips, "1976D2", "E3F2FD"));
                
                children.push(new Paragraph({ text: "3. DIREKTORI SUMBER BELAJAR VISUAL", heading: HeadingLevel.HEADING_2, alignment: AlignmentType.LEFT, spacing: { before: 400, after: 200 }, shading: { type: ShadingType.SOLID, color: "2196F3", fill: "2196F3" } }));
                const visualSources = [
                    { kategori: "Interactive Learning Apps", platform: `Quick Draw! (Tebak Gambar)\nCanva untuk Pendidikan\nLet's Read Asia (Cerita Visual)`, manfaat: "Melatih imajinasi keruangan dan kreativitas desain secara interaktif." },
                    { kategori: "DIY Project Platforms", platform: `Kok Bisa? (Animasi YouTube)\nHujan Tanda Tanya\nArt for Kids Hub`, manfaat: "Menyediakan visualisasi tajam untuk menjelaskan fenomena rumit." },
                    { kategori: "Virtual Labs", platform: `Google Earth\nPhET (Simulasi Geometri)`, manfaat: "Mengeksplorasi bentuk dan struktur benda dari layar Anda secara 3D." }
                ];
                children.push(createSourceTableDetailed(visualSources, "2196F3", "E3F2FD", "FFFFFF"));
                
                children.push(new Paragraph({ text: "Pesan Semangat: Teruslah berkreasi dengan imajinasimu yang luar biasa! Warnai setiap proses belajarmu dengan ceria karena dunia ini adalah kanvas besarmu! 🎨✨", spacing: { before: 300, after: 100 }, bold: true, alignment: AlignmentType.CENTER }));
            }

            if (styles.includes('Auditori')) {
                children.push(new Paragraph({ text: "2. ANALISIS & REKOMENDASI: GAYA BELAJAR AUDITORI", heading: HeadingLevel.HEADING_2, alignment: AlignmentType.LEFT, spacing: { before: 400, after: 150 }, shading: { type: ShadingType.SOLID, color: "FBC02D", fill: "FBC02D" } }));
                children.push(new Paragraph({ text: "Profil Singkat: Sebagai pembelajar auditori, pendengaran adalah senjata utamamu. Anda sangat peka terhadap nada suara, ritme, dan lebih mudah mencerna materi melalui diskusi, mendengarkan cerita, atau penjelasan lisan.", spacing: { after: 200 } }));

                const auditoryReco = [
                    { metode: "Teknik Membaca Bersuara", penjelasan: "Jangan membaca dalam hati. Bacalah buku catatan atau materi pelajaran dengan suara lantang yang jelas. Telinga Anda akan merekam suara Anda sendiri dan mengubahnya menjadi ingatan jangka panjang." },
                    { metode: "Diskusi & Kelompok Belajar", penjelasan: "Bentuklah kelompok belajar. Menjelaskan materi kepada teman atau mendengarkan teman berpendapat akan membuat materi jauh lebih mudah menempel di kepala Anda." },
                    { metode: "Audio & Podcast Edukasi", penjelasan: "Ganti kebiasaan membaca buku tebal dengan mendengarkan audiobook atau rekaman guru saat sedang bersantai atau dalam perjalanan." },
                    { metode: "Irama & Jembatan Keledai", penjelasan: "Ubah daftar hafalan yang membosankan menjadi lagu singkat yang asyik. Rima dan nada musik mempercepat proses penyerapan informasi." }
                ];
                children.push(createRecoTable(auditoryReco, "FBC02D", "FFF9C4", "FFFFFF"));
                
                children.push(new Paragraph({ text: "", spacing: { after: 200 } }));
                const auditoryTips = [
                    "Selalu rekam suaramu saat membaca rangkuman dan dengarkan sebelum tidur",
                    "Gunakan irama lagu favoritmu untuk menghafal rumus-rumus matematika",
                    "Ajak orang tua atau saudara berdiskusi ringan mengenai apa yang baru kamu pelajari",
                    "Gunakan fitur 'Text-to-Speech' di HP untuk membacakan artikel panjang",
                    "Bermain kuis tebak-tebakan lisan dengan teman akan sangat menyenangkan"
                ];
                children.push(createListTable(auditoryTips, "F57F17", "FFF9C4"));

                children.push(new Paragraph({ text: "3. DIREKTORI SUMBER BELAJAR AUDITORI", heading: HeadingLevel.HEADING_2, alignment: AlignmentType.LEFT, spacing: { before: 400, after: 200 }, shading: { type: ShadingType.SOLID, color: "FBC02D", fill: "FBC02D" } }));
                const auditorySources = [
                    { kategori: "Interactive Learning Apps", platform: `Nussa (Lagu Edukasi)\nLagu Anak Indonesia\nQuizizz (Kuis Bersuara)`, manfaat: "Menyediakan input suara dan lagu yang ritmis untuk daya ingat." },
                    { kategori: "DIY Project Platforms", platform: `Let's Read Asia (Audiobook)\nPodcast Edukasi Anak\nChrome Music Lab`, manfaat: "Eksplorasi nada dan mendengarkan cerita tanpa harus lelah membaca." },
                    { kategori: "Virtual Labs", platform: `PhET (Simulasi Suara)\nLabster (Instruksi Audio)`, manfaat: "Fokus pada pendengaran untuk bereksperimen dengan gelombang suara." }
                ];
                children.push(createSourceTableDetailed(auditorySources, "FBC02D", "FFF9C4", "FFFFFF"));

                children.push(new Paragraph({ text: "Pesan Semangat: Jadikan setiap pelajaran sebagai melodi yang indah! Jangan ragu untuk selalu bersuara dan berdiskusi. Dunia menantikan ide-ide brilianmu! 🎧🗣️", spacing: { before: 300, after: 100 }, bold: true, alignment: AlignmentType.CENTER }));
            }

            if (styles.includes('Kinestetik')) {
                children.push(new Paragraph({ text: "2. ANALISIS & REKOMENDASI: GAYA BELAJAR KINESTETIK", heading: HeadingLevel.HEADING_2, alignment: AlignmentType.LEFT, spacing: { before: 400, after: 150 }, shading: { type: ShadingType.SOLID, color: "9C27B0", fill: "9C27B0" } }));
                children.push(new Paragraph({ text: "Profil Singkat: Sebagai pembelajar kinestetik, tubuh dan tangan Anda tidak bisa diam! Anda belajar paling efektif melalui sentuhan, gerakan fisik, eksperimen langsung, dan praktik lapangan (learning by doing).", spacing: { after: 200 } }));

                const kinesReco = [
                    { metode: "Integrasi Aktivitas Fisik", penjelasan: "Saat sedang menghafal, jangan duduk diam. Cobalah berjalan bolak-balik di dalam kamar, memantulkan bola basket, atau menggunakan fidget spinner. Gerakan akan merangsang kerja otakmu." },
                    { metode: "Simulasi & Role-Playing", penjelasan: "Peragakan materi yang sedang dipelajari layaknya seorang aktor. Jika belajar sejarah, jadilah tokoh utamanya. Jika belajar biologi, peragakan cara kerja sel tubuh." },
                    { metode: "Konstruksi Model 3D", penjelasan: "Ubah materi abstrak menjadi wujud nyata. Gunakan plastisin, stik es krim, atau balok lego untuk membangun model dari topik pelajaran (misal: tata surya atau struktur bangunan)." },
                    { metode: "Eksperimen Lapangan", penjelasan: "Terjun langsung adalah cara terbaik. Tanam biji kacang hijau secara nyata daripada hanya membaca proses fotosintesis. Lakukan eksperimen sains sederhana di dapur." }
                ];
                children.push(createRecoTable(kinesReco, "9C27B0", "F3E5F5", "FFFFFF"));

                children.push(new Paragraph({ text: "", spacing: { after: 200 } }));
                const kinestheticTips = [
                    "Lakukan uji coba praktis dan eksperimen sains setiap akhir pekan",
                    "Gunakan gerakan tangan yang ekspresif saat mengingat sebuah daftar hafalan",
                    "Ambil waktu istirahat (stretching) setiap 20 menit agar tubuh tidak pegal",
                    "Ubah tugas sekolah menjadi proyek seni atau prakarya 3 Dimensi",
                    "Jadilah relawan untuk maju ke depan kelas dan mempraktikkan pelajaran"
                ];
                children.push(createListTable(kinestheticTips, "7B1FA2", "F3E5F5"));

                children.push(new Paragraph({ text: "3. DIREKTORI SUMBER BELAJAR KINESTETIK", heading: HeadingLevel.HEADING_2, alignment: AlignmentType.LEFT, spacing: { before: 400, after: 200 }, shading: { type: ShadingType.SOLID, color: "9C27B0", fill: "9C27B0" } }));
                const kinestheticSources = [
                    { kategori: "Interactive Learning Apps", platform: `Wordwall (Kuis Tarik-Geser)\nKahoot! (Kuis Cepat)\nMinecraft Education`, manfaat: "Aktivitas motorik pada jari untuk menyeret objek dan berkompetisi." },
                    { kategori: "DIY Project Platforms", platform: `Video Senam Edukasi\nEksperimen Sains Anak\nInstructables (Prakarya)`, manfaat: "Memberikan panduan langkah-demi-langkah untuk membuat sesuatu secara fisik." },
                    { kategori: "Virtual Labs", platform: `PhET (Simulasi Interaktif)\nChemCollective`, manfaat: "Menggeser tuas dan mencampur cairan dalam laboratorium virtual." }
                ];
                children.push(createSourceTableDetailed(kinestheticSources, "9C27B0", "F3E5F5", "FFFFFF"));

                children.push(new Paragraph({ text: "Pesan Semangat: Jangan takut untuk terus bergerak dan bereksperimen! Dunia ini adalah laboratorium besarmu. Teruslah berkarya melalui sentuhan tanganmu! 🏃‍♂️🔬", spacing: { before: 300, after: 100 }, bold: true, alignment: AlignmentType.CENTER }));
            }

            // Create and download document
            const doc = new Document({ sections: [{ properties: {}, children: children }] });
            const blob = await Packer.toBlob(doc);
            saveAs(blob, `HasilLengkapGayaBelajar_${dominantStyle}_${playerName}_${tanggal}.docx`);
        }
        """

        if func_pattern.search(content):
            content = func_pattern.sub(new_func, content)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated detailed word export function in {filepath}")
        else:
            print(f"Could not find word export function in {filepath}")
    except FileNotFoundError:
        pass

update_detailed_word_export('rekomendasi.html')
update_detailed_word_export('sumber.html')
