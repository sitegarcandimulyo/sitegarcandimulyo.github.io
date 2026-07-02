import re

with open('larikelas6.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add #phase-selection-screen HTML after #main-dashboard
main_dashboard_html = """    </div>

    <!-- HALAMAN REGISTRASI -->
    <div id="login-screen" style="display: none;">"""

phase_selection_html = """    </div>

    <!-- DASHBOARD FASE (Pilih Fase) -->
    <div id="phase-selection-screen" style="display: none; position: absolute; z-index: 110; width: 100%; height: 100%; flex-direction: column; justify-content: center; align-items: center; background: rgba(0,0,0,0.2); backdrop-filter: blur(5px);">
        <div class="dashboard-header" style="text-align: center; background: rgba(26, 32, 44, 0.95); padding: 40px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 1px solid rgba(255, 255, 255, 0.1);">
            <img src="logo.png" alt="Logo Si Tegar" style="max-width: 150px; margin-bottom: 15px; filter: drop-shadow(0 0 10px rgba(255,255,255,0.2));">
            <h1 style="color: #ffffff; font-weight: 800; margin-top: 15px; font-size: 2.5rem; text-shadow: 0 0 10px rgba(255,255,255,0.3);">PILIH FASE</h1>
            <p class="subtitle" style="font-weight: bold; color: #94a3b8; font-size: 1.2rem;">Pilih Fase Kelas</p>
            <div class="mode-selection d-flex justify-content-center gap-4 mt-4 flex-wrap">
                <button onclick="selectPhase('bawah')" class="btn btn-outline-primary" style="width: 160px; height: 150px; border-radius: 15px; border-width: 3px; display: flex; flex-direction: column; align-items: center; justify-content: center; transition: all 0.3s; background: rgba(255, 255, 255, 0.05);">
                    <i class="fas fa-child mb-3 text-primary" style="font-size: 3rem;"></i>
                    <span class="mode-text fs-5 fw-bold text-white">Fase Kelas Bawah</span>
                </button>
                <button onclick="selectPhase('atas')" class="btn btn-outline-warning" style="width: 160px; height: 150px; border-radius: 15px; border-width: 3px; display: flex; flex-direction: column; align-items: center; justify-content: center; transition: all 0.3s; background: rgba(255, 255, 255, 0.05);">
                    <i class="fas fa-user-graduate mb-3 text-warning" style="font-size: 3rem;"></i>
                    <span class="mode-text fs-5 fw-bold text-white">Fase Kelas Atas</span>
                </button>
            </div>
            <button onclick="returnToDashboardFromPhase()" class="btn btn-secondary mt-4 w-100 fw-bold" style="border-radius: 12px; padding: 12px;">Kembali</button>
        </div>
    </div>

    <!-- HALAMAN REGISTRASI -->
    <div id="login-screen" style="display: none;">"""
content = content.replace(main_dashboard_html, phase_selection_html)

# 2. Add phase variables and functions in JS
js_vars_target = """        var isSetupComplete = false;"""
js_vars_new = """        var isSetupComplete = false;
        var selectedPhase = '';"""
content = content.replace(js_vars_target, js_vars_new)

# 3. Change showPlayerSetup logic and add selectPhase
show_player_setup_target = """        function showPlayerSetup(mode) {
            playerCount = mode;

            document.querySelectorAll('.player-input-box').forEach(box => box.classList.add('hidden'));
            document.querySelector('.p1-box').classList.remove('hidden');
            
            if (mode === 2) {
                document.querySelector('.p2-box').classList.remove('hidden');
                document.getElementById('setup-title').innerText = "Registrasi 2 Pelari";
                document.getElementById('player-inputs').style.gridTemplateColumns = '1fr 1fr';
            } else {
                document.getElementById('setup-title').innerText = "Registrasi 1 Pelari";
                document.getElementById('player-inputs').style.gridTemplateColumns = '1fr';
                document.getElementById('p2-name').value = '';
            }

            document.getElementById('main-dashboard').style.display = 'none';
            document.getElementById('login-screen').style.display = 'flex';
            checkInputs();
        }

        function returnToDashboard() {
            document.getElementById('login-screen').style.display = 'none';
            document.getElementById('main-dashboard').style.display = 'flex';
        }"""
show_player_setup_new = """        function showPlayerSetup(mode) {
            playerCount = mode;
            document.getElementById('main-dashboard').style.display = 'none';
            document.getElementById('phase-selection-screen').style.display = 'flex';
        }

        function returnToDashboardFromPhase() {
            document.getElementById('phase-selection-screen').style.display = 'none';
            document.getElementById('main-dashboard').style.display = 'flex';
        }

        function selectPhase(phase) {
            selectedPhase = phase;
            document.getElementById('phase-selection-screen').style.display = 'none';
            proceedToLoginScreen();
        }

        function proceedToLoginScreen() {
            document.querySelectorAll('.player-input-box').forEach(box => box.classList.add('hidden'));
            document.querySelector('.p1-box').classList.remove('hidden');
            
            let phaseText = selectedPhase === 'bawah' ? "Kelas Bawah" : "Kelas Atas";
            
            if (playerCount === 2) {
                document.querySelector('.p2-box').classList.remove('hidden');
                document.getElementById('setup-title').innerText = "Registrasi 2 Pelari (" + phaseText + ")";
                document.getElementById('player-inputs').style.gridTemplateColumns = '1fr 1fr';
            } else {
                document.getElementById('setup-title').innerText = "Registrasi 1 Pelari (" + phaseText + ")";
                document.getElementById('player-inputs').style.gridTemplateColumns = '1fr';
                document.getElementById('p2-name').value = '';
            }

            document.getElementById('login-screen').style.display = 'flex';
            checkInputs();
        }

        function returnToDashboard() {
            document.getElementById('login-screen').style.display = 'none';
            document.getElementById('phase-selection-screen').style.display = 'flex';
        }"""
content = content.replace(show_player_setup_target, show_player_setup_new)

with open('larikelas6.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Changes applied successfully!")
