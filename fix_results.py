import re

with open('larikelas6.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = """        function endGame(wid) {
            gameActive = false;
            const duration = ((new Date() - startTime) / 1000).toFixed(1);

            // Karena ini kuesioner, "pemenang" ditentukan oleh gaya belajar dominan
            let winnerText = "Hasil Kuesioner:";
            let dominantStyle = '';
            let maxCount = -1;

            const activePlayers = getActivePlayersId();

            // Sembunyikan elemen 1-player secara default
            document.getElementById('player-result-summary').style.display = 'none';
            document.getElementById('view-recommendation-btn').style.display = 'none';
            document.getElementById('two-player-results-container').style.display = 'none';

            if (activePlayers.length === 1) {
                const p1 = players[activePlayers[0]];
                const counts = { V: p1.vCount, A: p1.aCount, K: p1.kCount };

                dominantStyle = calculateDominant(p1.vCount, p1.aCount, p1.kCount);

                winnerText = `${p1.name} memiliki Gaya Belajar: ${dominantStyle}`;
                document.getElementById('player-result-summary').innerHTML = `(Visual: ${p1.vCount}, Auditori: ${p1.aCount}, Kinestetik: ${p1.kCount})`;
                document.getElementById('player-result-summary').style.display = 'block';

                // Tampilkan tombol rekomendasi dan AI untuk 1 pemain
                const recoBtn = document.getElementById('view-recommendation-btn');
                recoBtn.style.display = 'inline-block';
                recoBtn.onclick = () => {
                    window.location.href = `rekomendasi.html?style=${dominantStyle}&name=${encodeURIComponent(p1.name)}&v=${p1.vCount}&a=${p1.aCount}&k=${p1.kCount}`;
                };

                document.getElementById('self-learn-ai-btn').style.display = 'inline-block';

            } else if (activePlayers.length === 2) {
                const p1 = players[activePlayers[0]];
                const p2 = players[activePlayers[1]];

                document.getElementById('two-player-results-container').style.display = 'flex';
                document.getElementById('player-result-summary').style.display = 'none';
                document.getElementById('view-recommendation-btn').style.display = 'none';

                // --- Player 1 Results ---
                document.getElementById('p1-two-player-name').innerText = p1.name;
                const p1Counts = { V: p1.vCount, A: p1.aCount, K: p1.kCount };
                const p1Dominant = calculateDominant(p1.vCount, p1.aCount, p1.kCount);

                document.getElementById('p1-two-player-dominant').innerText = `Gaya Belajar: ${p1Dominant}`;
                document.getElementById('p1-two-player-counts').innerText = `(V: ${p1.vCount}, A: ${p1.aCount}, K: ${p1.kCount})`;
                document.getElementById('two-player-reco-btn-p1').onclick = () => {
                    window.location.href = `rekomendasi.html?style=${p1Dominant}&name=${encodeURIComponent(p1.name)}&v=${p1.vCount}&a=${p1.aCount}&k=${p1.kCount}`;
                };

                // --- Player 2 Results ---
                document.getElementById('p2-two-player-name').innerText = p2.name;
                const p2Counts = { V: p2.vCount, A: p2.aCount, K: p2.kCount };
                const p2Dominant = calculateDominant(p2.vCount, p2.aCount, p2.kCount);

                document.getElementById('p2-two-player-dominant').innerText = `Gaya Belajar: ${p2Dominant}`;
                document.getElementById('p2-two-player-counts').innerText = `(V: ${p2.vCount}, A: ${p2.aCount}, K: ${p2.kCount})`;
                document.getElementById('two-player-reco-btn-p2').onclick = () => {
                    window.location.href = `rekomendasi.html?style=${p2Dominant}&name=${encodeURIComponent(p2.name)}&v=${p2.vCount}&a=${p2.aCount}&k=${p2.kCount}`;
                };

                // Pastikan tombol AI dan Main Lagi terlihat
                document.getElementById('self-learn-ai-btn').style.display = 'inline-block';
            }"""

replacement = """        function calculateDominant(v, a, k) {
            let max = Math.max(v, a, k);
            if (max === v) return 'Visual';
            if (max === a) return 'Auditori';
            return 'Kinestetik';
        }

        function endGame(wid) {
            gameActive = false;
            const duration = ((new Date() - startTime) / 1000).toFixed(1);

            // Karena ini kuesioner, "pemenang" ditentukan oleh gaya belajar dominan
            let winnerText = "Hasil Kuesioner:";
            let dominantStyle = '';

            const activePlayers = getActivePlayersId();

            // Sembunyikan elemen 1-player secara default
            document.getElementById('player-result-summary').style.display = 'none';
            document.getElementById('view-recommendation-btn').style.display = 'none';
            document.getElementById('two-player-results-container').style.display = 'none';

            if (activePlayers.length === 1) {
                const p1 = players[activePlayers[0]];
                dominantStyle = calculateDominant(p1.vCount, p1.aCount, p1.kCount);

                let vPct = Math.round((p1.vCount / TOTAL_STEPS) * 100);
                let aPct = Math.round((p1.aCount / TOTAL_STEPS) * 100);
                let kPct = Math.round((p1.kCount / TOTAL_STEPS) * 100);

                winnerText = `${p1.name} memiliki Gaya Belajar: ${dominantStyle}`;
                document.getElementById('player-result-summary').innerHTML = `(Visual: ${vPct}%, Auditori: ${aPct}%, Kinestetik: ${kPct}%)`;
                document.getElementById('player-result-summary').style.display = 'block';

                // Tampilkan tombol rekomendasi dan AI untuk 1 pemain
                const recoBtn = document.getElementById('view-recommendation-btn');
                recoBtn.style.display = 'inline-block';
                recoBtn.onclick = () => {
                    window.location.href = `rekomendasi.html?style=${dominantStyle}&name=${encodeURIComponent(p1.name)}&v=${p1.vCount}&a=${p1.aCount}&k=${p1.kCount}`;
                };

                document.getElementById('self-learn-ai-btn').style.display = 'inline-block';

            } else if (activePlayers.length === 2) {
                const p1 = players[activePlayers[0]];
                const p2 = players[activePlayers[1]];

                document.getElementById('two-player-results-container').style.display = 'flex';
                document.getElementById('player-result-summary').style.display = 'none';
                document.getElementById('view-recommendation-btn').style.display = 'none';

                // --- Player 1 Results ---
                document.getElementById('p1-two-player-name').innerText = p1.name;
                const p1Dominant = calculateDominant(p1.vCount, p1.aCount, p1.kCount);
                
                let p1vPct = Math.round((p1.vCount / TOTAL_STEPS) * 100);
                let p1aPct = Math.round((p1.aCount / TOTAL_STEPS) * 100);
                let p1kPct = Math.round((p1.kCount / TOTAL_STEPS) * 100);

                document.getElementById('p1-two-player-dominant').innerText = `Gaya Belajar: ${p1Dominant}`;
                document.getElementById('p1-two-player-counts').innerText = `(V: ${p1vPct}%, A: ${p1aPct}%, K: ${p1kPct}%)`;
                document.getElementById('two-player-reco-btn-p1').onclick = () => {
                    window.location.href = `rekomendasi.html?style=${p1Dominant}&name=${encodeURIComponent(p1.name)}&v=${p1.vCount}&a=${p1.aCount}&k=${p1.kCount}`;
                };

                // --- Player 2 Results ---
                document.getElementById('p2-two-player-name').innerText = p2.name;
                const p2Dominant = calculateDominant(p2.vCount, p2.aCount, p2.kCount);
                
                let p2vPct = Math.round((p2.vCount / TOTAL_STEPS) * 100);
                let p2aPct = Math.round((p2.aCount / TOTAL_STEPS) * 100);
                let p2kPct = Math.round((p2.kCount / TOTAL_STEPS) * 100);

                document.getElementById('p2-two-player-dominant').innerText = `Gaya Belajar: ${p2Dominant}`;
                document.getElementById('p2-two-player-counts').innerText = `(V: ${p2vPct}%, A: ${p2aPct}%, K: ${p2kPct}%)`;
                document.getElementById('two-player-reco-btn-p2').onclick = () => {
                    window.location.href = `rekomendasi.html?style=${p2Dominant}&name=${encodeURIComponent(p2.name)}&v=${p2.vCount}&a=${p2.aCount}&k=${p2.kCount}`;
                };

                // Pastikan tombol AI dan Main Lagi terlihat
                document.getElementById('self-learn-ai-btn').style.display = 'inline-block';
            }"""

if target in content:
    content = content.replace(target, replacement)
    with open('larikelas6.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed calculateDominant and updated to percentages.")
else:
    print("Target string not found!")
