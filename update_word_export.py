import re

def update_download_function(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find the start of the function and the end of the script block
        # Since this function is quite large, replacing the whole script block or just the function is best.
        # We will look for "async function downloadHasilLengkapWord() {" and its closing brace, but it's easier to replace it entirely by regex.
        
        func_pattern = re.compile(r'async function downloadHasilLengkapWord\(\) \{.*?(?=</script>)', re.DOTALL)
        
        new_func = """async function downloadHasilLengkapWord() {
            const { Document, Packer, Paragraph, Table, TableRow, TableCell, AlignmentType, WidthType, ShadingType, HeadingLevel, TextRun } = docx;

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

            // 1. HEADER & TES GAYA BELAJAR
            children.push(
                new Paragraph({ text: "HASIL ANALISIS GAYA BELAJAR LENGKAP", heading: HeadingLevel.HEADING_1, alignment: AlignmentType.CENTER, spacing: { after: 400 }, shading: { type: ShadingType.SOLID, color: "4CAF50", fill: "4CAF50" } }),
                new Paragraph({ text: `Nama: ${playerName}`, spacing: { after: 100 } }),
                new Paragraph({ text: `Tanggal: ${tanggal}`, spacing: { after: 100 } }),
                new Paragraph({ text: `Gaya Belajar Dominan: ${dominantStyle}`, spacing: { after: 300 }, bold: true }),
                new Paragraph({ text: "1. HASIL TES GAYA BELAJAR", heading: HeadingLevel.HEADING_2, alignment: AlignmentType.LEFT, spacing: { before: 200, after: 200 }, shading: { type: ShadingType.SOLID, color: "2196F3", fill: "2196F3" } })
            );

            const resultsTable = new Table({
                width: { size: 100, type: WidthType.PERCENTAGE },
                rows: [
                    new TableRow({
                        children: [
                            new TableCell({ children: [new Paragraph({ text: "Gaya Belajar", bold: true, alignment: AlignmentType.CENTER })], shading: { type: ShadingType.SOLID, color: "2196F3", fill: "2196F3" }, width: { size: 30, type: WidthType.PERCENTAGE } }),
                            new TableCell({ children: [new Paragraph({ text: "Jawaban", bold: true, alignment: AlignmentType.CENTER })], shading: { type: ShadingType.SOLID, color: "2196F3", fill: "2196F3" }, width: { size: 20, type: WidthType.PERCENTAGE } }),
                            new TableCell({ children: [new Paragraph({ text: "Persentase", bold: true, alignment: AlignmentType.CENTER })], shading: { type: ShadingType.SOLID, color: "2196F3", fill: "2196F3" }, width: { size: 20, type: WidthType.PERCENTAGE } }),
                            new TableCell({ children: [new Paragraph({ text: "Bar", bold: true, alignment: AlignmentType.CENTER })], shading: { type: ShadingType.SOLID, color: "2196F3", fill: "2196F3" }, width: { size: 30, type: WidthType.PERCENTAGE } })
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
                                new TableCell({ children: [new Paragraph({ text: "Metode", bold: true, alignment: AlignmentType.CENTER })], shading: { type: ShadingType.SOLID, color: colorHead, fill: colorHead }, width: { size: 30, type: WidthType.PERCENTAGE } }),
                                new TableCell({ children: [new Paragraph({ text: "Penjelasan Detail", bold: true, alignment: AlignmentType.CENTER })], shading: { type: ShadingType.SOLID, color: colorHead, fill: colorHead }, width: { size: 70, type: WidthType.PERCENTAGE } })
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
                        new TableRow({ children: [new TableCell({ children: [new Paragraph({ text: "Tips Belajar Paling Seru", bold: true, alignment: AlignmentType.CENTER })], shading: { type: ShadingType.SOLID, color: colorHead, fill: colorHead } })] }),
                        ...items.map(item => new TableRow({ children: [new TableCell({ children: [new Paragraph({ text: `• ${item}` })], shading: { type: ShadingType.SOLID, color: colorBody, fill: colorBody } })] }))
                    ]
                });
            };

            const createSourceTable = (sources, colorHead, colorBody1, colorBody2) => {
                return new Table({
                    width: { size: 100, type: WidthType.PERCENTAGE },
                    rows: [
                        new TableRow({
                            children: [
                                new TableCell({ children: [new Paragraph({ text: "Kategori Platform", bold: true, alignment: AlignmentType.CENTER })], shading: { type: ShadingType.SOLID, color: colorHead, fill: colorHead }, width: { size: 30, type: WidthType.PERCENTAGE } }),
                                new TableCell({ children: [new Paragraph({ text: "Daftar Link & Aplikasi", bold: true, alignment: AlignmentType.CENTER })], shading: { type: ShadingType.SOLID, color: colorHead, fill: colorHead }, width: { size: 70, type: WidthType.PERCENTAGE } })
                            ]
                        }),
                        ...sources.map(res => new TableRow({
                            children: [
                                new TableCell({ children: [new Paragraph({ text: res.kategori, bold: true })], shading: { type: ShadingType.SOLID, color: colorBody1, fill: colorBody1 } }),
                                new TableCell({ children: [new Paragraph({ text: res.platform })], shading: { type: ShadingType.SOLID, color: colorBody2, fill: colorBody2 } })
                            ]
                        }))
                    ]
                });
            };

            if (styles.includes('Visual')) {
                children.push(new Paragraph({ text: "2. REKOMENDASI GAYA BELAJAR VISUAL", heading: HeadingLevel.HEADING_2, alignment: AlignmentType.LEFT, spacing: { before: 400, after: 200 }, shading: { type: ShadingType.SOLID, color: "2196F3", fill: "2196F3" } }));
                const visualReco = [
                    { metode: "Mind Mapping", penjelasan: "Buat peta konsep dengan cabang-cabang untuk menghubungkan ide-ide utama dan detail. Gunakan warna dan gambar untuk memperkuat ingatan." },
                    { metode: "Kartu Flash Bergambar", penjelasan: "Gunakan kartu dengan istilah di satu sisi dan gambar atau diagram yang relevan di sisi lain." },
                    { metode: "Menonton Video", penjelasan: "Tonton video pembelajaran edukasi dan animasi agar dapat melihat langsung konsep materi tersebut." },
                    { metode: "Kode Warna Catatan", penjelasan: "Gunakan stabilo atau pulpen warna-warni untuk mengkategorikan informasi penting." }
                ];
                children.push(createRecoTable(visualReco, "2196F3", "E3F2FD", "FFFFFF"));
                
                children.push(new Paragraph({ text: "", spacing: { after: 200 } }));
                const visualTips = [
                    "Buatlah mind mapping untuk setiap topik baru yang kamu pelajari",
                    "Gunakan highlighter warna-warni untuk menandai poin penting",
                    "Tempel poster atau infografis di dinding kamarmu",
                    "Rekam penjelasan guru dalam bentuk sketsa atau diagram",
                    "Buat flashcard dengan gambar dan warna menarik"
                ];
                children.push(createListTable(visualTips, "1976D2", "E3F2FD"));
                
                children.push(new Paragraph({ text: "3. SUMBER BELAJAR VISUAL LOKAL", heading: HeadingLevel.HEADING_2, alignment: AlignmentType.LEFT, spacing: { before: 400, after: 200 }, shading: { type: ShadingType.SOLID, color: "2196F3", fill: "2196F3" } }));
                const visualSources = [
                    { kategori: "Interactive Learning Apps", platform: "Quick Draw! (Game Tebak Gambar)\\nCanva untuk Anak\\nLet's Read Asia (Buku Cerita Bergambar)" },
                    { kategori: "DIY Project Platforms", platform: "Kok Bisa? (Video Edukasi Animasi)\\nHujan Tanda Tanya (Sains Visual)\\nArt for Kids Hub" },
                    { kategori: "Virtual Labs", platform: "Google Earth (Eksplorasi Peta)\\nPhET (Simulasi Geometri & Optik)" }
                ];
                children.push(createSourceTable(visualSources, "2196F3", "E3F2FD", "FFFFFF"));
            }

            if (styles.includes('Auditori')) {
                children.push(new Paragraph({ text: "2. REKOMENDASI GAYA BELAJAR AUDITORI", heading: HeadingLevel.HEADING_2, alignment: AlignmentType.LEFT, spacing: { before: 400, after: 200 }, shading: { type: ShadingType.SOLID, color: "FBC02D", fill: "FBC02D" } }));
                const auditoryReco = [
                    { metode: "Membaca Suara Keras", penjelasan: "Baca buku catatan atau materi pelajaran dengan suara lantang. Mendengar suara sendiri memperkuat ingatan." },
                    { metode: "Diskusi Kelompok", penjelasan: "Bergabunglah dengan kelompok belajar atau bentuk kelompok diskusi. Mengutarakan ide sangat membantu." },
                    { metode: "Merekam Catatan", penjelasan: "Gunakan perekam suara untuk merekam rangkuman pelajaran dari gurumu." },
                    { metode: "Jembatan Keledai", penjelasan: "Buat akronim atau lagu singkat yang asyik untuk menghafal daftar atau urutan penting." }
                ];
                children.push(createRecoTable(auditoryReco, "FBC02D", "FFF9C4", "FFFFFF"));
                
                children.push(new Paragraph({ text: "", spacing: { after: 200 } }));
                const auditoryTips = [
                    "Rekam suaramu saat membaca materi lalu dengarkan kembali sebelum tidur",
                    "Gunakan irama atau lagu asyik untuk menghafal rumus dan istilah penting",
                    "Ajak teman atau orang tua untuk berdiskusi tentang topik pelajaran baru",
                    "Bacalah buku pelajaran dengan suara lantang layaknya sedang bercerita",
                    "Buatlah kelompok belajar kecil untuk saling melakukan tanya jawab langsung"
                ];
                children.push(createListTable(auditoryTips, "F57F17", "FFF9C4"));

                children.push(new Paragraph({ text: "3. SUMBER BELAJAR AUDITORI LOKAL", heading: HeadingLevel.HEADING_2, alignment: AlignmentType.LEFT, spacing: { before: 400, after: 200 }, shading: { type: ShadingType.SOLID, color: "FBC02D", fill: "FBC02D" } }));
                const auditorySources = [
                    { kategori: "Interactive Learning Apps", platform: "Nussa (Cerita & Lagu Anak)\\nLagu Anak Indonesia Edukasi\\nQuizizz (Kuis Bersuara)" },
                    { kategori: "DIY Project Platforms", platform: "Let's Read Asia (Buku Bersuara)\\nPodcast Cerita Anak (Spotify)\\nChrome Music Lab" },
                    { kategori: "Virtual Labs", platform: "PhET (Simulasi Gelombang & Suara)\\nLabster (Virtual Lab Interaktif)" }
                ];
                children.push(createSourceTable(auditorySources, "FBC02D", "FFF9C4", "FFFFFF"));
            }

            if (styles.includes('Kinestetik')) {
                children.push(new Paragraph({ text: "2. REKOMENDASI GAYA BELAJAR KINESTETIK", heading: HeadingLevel.HEADING_2, alignment: AlignmentType.LEFT, spacing: { before: 400, after: 200 }, shading: { type: ShadingType.SOLID, color: "9C27B0", fill: "9C27B0" } }));
                const kinesReco = [
                    { metode: "Aktivitas Fisik", penjelasan: "Cobalah berjalan bolak-balik atau memantulkan bola saat menghafal. Gerakan fisik menjaga fokus." },
                    { metode: "Role-Playing", penjelasan: "Peragakan sebuah skenario materi sejarah atau ilmiah bersama teman-teman." },
                    { metode: "Membangun Model", penjelasan: "Buat model 3D atau karya seni dari topik yang dipelajari menggunakan balok atau plastisin." },
                    { metode: "Eksperimen Praktis", penjelasan: "Lakukan eksperimen nyata dan uji coba secara langsung menggunakan tanganmu sendiri." }
                ];
                children.push(createRecoTable(kinesReco, "9C27B0", "F3E5F5", "FFFFFF"));

                children.push(new Paragraph({ text: "", spacing: { after: 200 } }));
                const kinestheticTips = [
                    "Lakukan eksperimen secara langsung untuk menguji teori yang sedang dibahas",
                    "Gunakan gerakan tubuh atau berjalan-jalan kecil saat sedang menghafal sesuatu",
                    "Ambil waktu istirahat sejenak di sela belajar untuk sekadar meregangkan badan",
                    "Buatlah model atau prakarya dari benda nyata terkait topik yang dipelajari",
                    "Mainkan peran (role-play) bersama teman untuk mengingat sejarah atau cerita"
                ];
                children.push(createListTable(kinestheticTips, "7B1FA2", "F3E5F5"));

                children.push(new Paragraph({ text: "3. SUMBER BELAJAR KINESTETIK LOKAL", heading: HeadingLevel.HEADING_2, alignment: AlignmentType.LEFT, spacing: { before: 400, after: 200 }, shading: { type: ShadingType.SOLID, color: "9C27B0", fill: "9C27B0" } }));
                const kinestheticSources = [
                    { kategori: "Interactive Learning Apps", platform: "Wordwall (Kuis Aktif Geser & Tarik)\\nKahoot! (Kuis Kompetisi)\\nMinecraft Education" },
                    { kategori: "DIY Project Platforms", platform: "Video Senam Anak SD Ceria\\nVideo Eksperimen Sains Anak\\nInstructables (Proyek Prakarya)" },
                    { kategori: "Virtual Labs", platform: "PhET Simulasi Interaktif\\nChemCollective (Eksperimen Campur Warna)" }
                ];
                children.push(createSourceTable(kinestheticSources, "9C27B0", "F3E5F5", "FFFFFF"));
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
            print(f"Updated word export function in {filepath}")
        else:
            print(f"Could not find word export function in {filepath}")
    except FileNotFoundError:
        pass

update_download_function('rekomendasi.html')
update_download_function('sumber.html')
