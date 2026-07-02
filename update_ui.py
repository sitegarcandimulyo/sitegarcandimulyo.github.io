import re

with open('sumber.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_css = '''
    <style>
        :root {
            --bg-color: #0f172a;
            --card-bg: #1e293b;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --visual-color: #06b6d4;
            --auditory-color: #f97316;
            --kinesthetic-color: #ec4899;
            --title-color: #10b981;
        }

        body {
            height: 100vh;
            width: 100vw;
            overflow-x: hidden;
            background-color: var(--bg-color);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            color: var(--text-main);
        }

        /* --- LANDING VIEW --- */
        #landing-view {
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            padding: 20px;
            position: relative;
            overflow: hidden;
        }

        .illustration {
            position: absolute;
            left: -5%;
            bottom: -5%;
            width: 40%;
            max-width: 500px;
            z-index: 1;
            pointer-events: none;
        }

        .landing-content {
            z-index: 2;
            max-width: 1000px;
            width: 100%;
            margin-left: 30%;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
        }

        .badge-top {
            background: linear-gradient(90deg, #d946ef, #ec4899);
            color: white;
            padding: 8px 20px;
            border-radius: 30px;
            font-weight: 800;
            font-size: 0.9rem;
            letter-spacing: 1px;
            margin-bottom: 20px;
            display: inline-block;
            box-shadow: 0 4px 15px rgba(236, 72, 153, 0.4);
        }

        .main-title {
            color: var(--title-color);
            font-size: 3.5rem;
            font-weight: 900;
            margin: 0 0 15px 0;
            letter-spacing: 2px;
            text-shadow: 0 0 20px rgba(16, 185, 129, 0.2);
        }

        .main-subtitle {
            color: var(--text-muted);
            font-size: 1.1rem;
            max-width: 600px;
            margin: 0 auto 30px auto;
            line-height: 1.6;
        }

        .top-buttons {
            display: flex;
            gap: 15px;
            margin-bottom: 40px;
        }

        .top-buttons button {
            background: rgba(30, 41, 59, 0.8);
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: white;
            padding: 10px 20px;
            border-radius: 12px;
            font-weight: bold;
            font-size: 0.9rem;
            cursor: pointer;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .top-buttons button:hover {
            background: rgba(51, 65, 85, 0.8);
            transform: translateY(-2px);
        }

        .icon-blue { color: #3b82f6; }
        .icon-purple { color: #a855f7; }

        .cards-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 25px;
            width: 100%;
        }

        .style-card {
            background: var(--card-bg);
            border-radius: 20px;
            padding: 30px 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            transition: all 0.3s;
            border: 1px solid rgba(255, 255, 255, 0.05);
            position: relative;
            overflow: hidden;
        }

        .style-card:hover {
            transform: translateY(-10px);
        }

        .style-card::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; height: 4px;
        }

        .card-visual { box-shadow: 0 10px 30px rgba(6, 182, 212, 0.1); }
        .card-visual::before { background: var(--visual-color); }
        .card-visual:hover { box-shadow: 0 15px 40px rgba(6, 182, 212, 0.2); border-color: rgba(6, 182, 212, 0.3); }

        .card-auditory { box-shadow: 0 10px 30px rgba(249, 115, 22, 0.1); }
        .card-auditory::before { background: var(--auditory-color); }
        .card-auditory:hover { box-shadow: 0 15px 40px rgba(249, 115, 22, 0.2); border-color: rgba(249, 115, 22, 0.3); }

        .card-kinesthetic { box-shadow: 0 10px 30px rgba(236, 72, 153, 0.1); }
        .card-kinesthetic::before { background: var(--kinesthetic-color); }
        .card-kinesthetic:hover { box-shadow: 0 15px 40px rgba(236, 72, 153, 0.2); border-color: rgba(236, 72, 153, 0.3); }

        .card-icon {
            font-size: 3rem;
            margin-bottom: 20px;
            text-shadow: 0 0 20px currentColor;
        }
        
        .card-visual .card-icon { color: var(--visual-color); }
        .card-auditory .card-icon { color: var(--auditory-color); }
        .card-kinesthetic .card-icon { color: var(--kinesthetic-color); }

        .style-card h3 {
            font-size: 1.5rem;
            margin: 0 0 15px 0;
            color: white;
        }

        .card-visual h3 { color: var(--visual-color); }
        .card-auditory h3 { color: var(--auditory-color); }
        .card-kinesthetic h3 { color: var(--kinesthetic-color); }

        .style-card p {
            color: var(--text-muted);
            font-size: 0.95rem;
            line-height: 1.5;
            margin-bottom: 25px;
            flex-grow: 1;
        }

        .btn-mulai {
            width: 100%;
            padding: 12px;
            border: none;
            border-radius: 10px;
            color: white;
            font-weight: bold;
            font-size: 1rem;
            cursor: pointer;
            transition: all 0.2s;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .card-visual .btn-mulai { background: var(--visual-color); box-shadow: 0 4px 15px rgba(6, 182, 212, 0.3); }
        .card-visual .btn-mulai:hover { background: #0891b2; }

        .card-auditory .btn-mulai { background: var(--auditory-color); box-shadow: 0 4px 15px rgba(249, 115, 22, 0.3); }
        .card-auditory .btn-mulai:hover { background: #ea580c; }

        .card-kinesthetic .btn-mulai { background: var(--kinesthetic-color); box-shadow: 0 4px 15px rgba(236, 72, 153, 0.3); }
        .card-kinesthetic .btn-mulai:hover { background: #db2777; }

        /* --- DETAIL VIEW (Modernized) --- */
        #detail-view {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 40px 20px;
            min-height: 100vh;
        }

        .container {
            background: var(--card-bg);
            padding: 40px;
            border-radius: 25px;
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.4);
            max-width: 900px;
            width: 100%;
            display: flex;
            flex-direction: column;
            gap: 25px;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }

        .container h1 {
            color: white;
            font-size: 2.5rem;
            margin-bottom: 0px;
            text-align: center;
        }
        
        .container > p {
            color: var(--text-muted);
            text-align: center;
        }

        .source-section {
            border-radius: 15px;
            padding: 25px;
            background: rgba(15, 23, 42, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            display: none;
        }
        
        #visual-source h2 { color: var(--visual-color); }
        #auditory-source h2 { color: var(--auditory-color); }
        #kinesthetic-source h2 { color: var(--kinesthetic-color); }

        .source-section h2 {
            font-size: 1.8rem;
            margin-top: 10px;
            margin-bottom: 15px;
            text-align: center;
        }

        .source-section h3 {
            color: white;
            font-size: 1.5rem;
            margin-bottom: 15px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            padding-bottom: 10px;
        }

        .intro-text {
            font-size: 1.1rem;
            color: var(--text-muted);
            text-align: center;
            margin-bottom: 20px;
        }

        .source-section .tips-section {
            margin-top: 30px;
            padding: 20px;
            background: rgba(255, 255, 255, 0.03);
            border-radius: 12px;
            border: 1px dashed rgba(255, 255, 255, 0.2);
        }

        .tips-section h4 {
            color: white;
            font-size: 1.3rem;
            margin-bottom: 15px;
            text-align: center;
        }

        .tips-section li {
            color: var(--text-muted);
            margin-bottom: 8px;
            padding-left: 20px;
            position: relative;
        }
        
        .tips-section li::before {
            content: "•";
            color: var(--title-color);
            position: absolute;
            left: 0;
            font-size: 1.2rem;
            line-height: 1;
        }

        .reco-item {
            margin-top: 20px;
            padding: 20px;
            background: rgba(255, 255, 255, 0.03);
            border-radius: 15px;
            border-left: 4px solid;
            transition: transform 0.2s;
        }

        #visual-source .reco-item { border-left-color: var(--visual-color); }
        #auditory-source .reco-item { border-left-color: var(--auditory-color); }
        #kinesthetic-source .reco-item { border-left-color: var(--kinesthetic-color); }

        .reco-item:hover {
            transform: translateX(5px);
            background: rgba(255, 255, 255, 0.06);
        }

        .reco-item h4 {
            color: white;
            font-size: 1.2rem;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        #visual-source .reco-item h4 i { color: var(--visual-color); }
        #auditory-source .reco-item h4 i { color: var(--auditory-color); }
        #kinesthetic-source .reco-item h4 i { color: var(--kinesthetic-color); }

        .reco-item p {
            color: var(--text-muted);
            margin-bottom: 15px;
        }

        .source-links {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }

        .source-links a {
            background: rgba(255, 255, 255, 0.1);
            color: white;
            padding: 8px 15px;
            border-radius: 20px;
            text-decoration: none;
            font-size: 0.9rem;
            transition: all 0.2s;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }

        .source-links a:hover {
            background: rgba(255, 255, 255, 0.2);
        }

        .action-buttons {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 15px;
            margin-top: 30px;
        }

        .action-buttons button {
            padding: 12px 25px;
            border-radius: 30px;
            border: none;
            color: white;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.2s;
            background: rgba(255, 255, 255, 0.1);
        }

        .action-buttons button:hover {
            background: rgba(255, 255, 255, 0.2);
            transform: translateY(-2px);
        }

        #download-word-btn { background: #10b981; }
        #download-word-btn:hover { background: #059669; }
        
        #tegas-optimal-ai-btn { background: #3b82f6; }
        #tegas-optimal-ai-btn:hover { background: #2563eb; }

        @media (max-width: 1024px) {
            .cards-grid {
                grid-template-columns: repeat(2, 1fr);
            }
            .landing-content {
                margin-left: 0;
            }
            .illustration {
                display: none;
            }
        }

        @media (max-width: 768px) {
            .cards-grid {
                grid-template-columns: 1fr;
            }
            .main-title {
                font-size: 2.5rem;
            }
        }
    </style>
'''

content = re.sub(r'<style>.*?</style>', new_css, content, flags=re.DOTALL)

landing_view_html = '''
    <div id="landing-view">
        <img src="students_music.png" alt="Students" class="illustration">
        <div class="landing-content">
            <div class="badge-top">KELAS 1 - BAB 1: SUMBER BUNYI</div>
            <h1 class="main-title"><i class="fas fa-music"></i> SUMBER BUNYI</h1>
            <p class="main-subtitle">Selamat datang di misi pembelajaran interaktif! Silakan pilih kartu sesuai dengan kelompok gaya belajarmu hari ini.</p>
            
            <div class="top-buttons">
                <button><i class="fas fa-book icon-blue"></i> MATERI SUMBER BUNYI</button>
                <button><i class="fas fa-play icon-purple"></i> VIDEO SUMBER BUNYI</button>
            </div>

            <div class="cards-grid">
                <div class="style-card card-visual">
                    <div class="card-icon"><i class="fas fa-eye"></i></div>
                    <h3>Kelompok Visual</h3>
                    <p>Mengerjakan tantangan dengan mengamati gambar dan kartu visual.</p>
                    <button class="btn-mulai" onclick="showSection('Visual')">MULAI MISI</button>
                </div>
                
                <div class="style-card card-auditory">
                    <div class="card-icon"><i class="fas fa-headphones"></i></div>
                    <h3>Kelompok Auditori</h3>
                    <p>Mengerjakan tantangan dengan mendengarkan rekaman dan simulasi suara.</p>
                    <button class="btn-mulai" onclick="showSection('Auditori')">MULAI MISI</button>
                </div>

                <div class="style-card card-kinesthetic">
                    <div class="card-icon"><i class="fas fa-hand-pointer"></i></div>
                    <h3>Kelompok Kinestetik</h3>
                    <p>Mengerjakan tantangan dengan aktivitas fisik menyusun dan menggeser benda.</p>
                    <button class="btn-mulai" onclick="showSection('Kinestetik')">MULAI MISI</button>
                </div>
            </div>
        </div>
    </div>
    
    <div id="detail-view" style="display: none;">
'''

pattern = r'<div class="animated-background">.*?<div class="container">'
content = re.sub(pattern, landing_view_html + '\n        <div class="container">', content, flags=re.DOTALL)

content = content.replace('<!-- Libraries for Word Document Generation -->', '</div>\n\n    <!-- Libraries for Word Document Generation -->')

js_injection = '''
            window.showSection = function(style) {
                 const currentUrl = new URL(window.location.href);
                 currentUrl.searchParams.set('style', style);
                 window.location.href = currentUrl.href;
            };

            if (!dominantStyle) {
                document.getElementById('landing-view').style.display = 'flex';
                document.getElementById('detail-view').style.display = 'none';
            } else {
                document.getElementById('landing-view').style.display = 'none';
                document.getElementById('detail-view').style.display = 'flex';
            }
'''

content = content.replace('// Display relevant sections based on dominant style', js_injection + '\n            // Display relevant sections based on dominant style')

with open('sumber.html', 'w', encoding='utf-8') as f:
    f.write(content)
