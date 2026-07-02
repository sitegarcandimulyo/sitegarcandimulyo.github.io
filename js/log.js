import { auth, db } from './firebase-init.js';
import { onAuthStateChanged } from "https://www.gstatic.com/firebasejs/9.15.0/firebase-auth.js";
import { collection, addDoc, getDocs, doc, deleteDoc, updateDoc, query, orderBy } from "https://www.gstatic.com/firebasejs/9.15.0/firebase-firestore.js";

document.addEventListener('DOMContentLoaded', () => {
    // UI Elements
    const addLogBtn = document.getElementById('add-log-btn');
    const logFormContainer = document.getElementById('log-form-container');
    const logForm = document.getElementById('log-form');
    const cancelLogBtn = document.getElementById('cancel-log-btn');
    const logHistoryContainer = document.getElementById('log-history');
    const logMethodSelect = document.getElementById('log-method');

    // Modal Elements
    const feedbackModalEl = document.getElementById('feedbackModal');
    let feedbackModal = null;
    if (feedbackModalEl) {
        feedbackModal = new bootstrap.Modal(feedbackModalEl);
    }
    const ratingStarsContainer = document.getElementById('rating-stars');
    const feedbackMethodName = document.getElementById('feedback-method-name');
    const saveFeedbackBtn = document.getElementById('save-feedback-btn');
    const hiddenLogIdInput = document.getElementById('feedback-log-index'); // This now stores Firestore ID

    let currentUser = null;

    // --- Auth State ---
    onAuthStateChanged(auth, (user) => {
        if (user) {
            currentUser = user;
            if (addLogBtn) addLogBtn.disabled = false;
            if (typeof renderLogs === 'function') renderLogs();
        } else {
            currentUser = null;
            if (addLogBtn) addLogBtn.disabled = true;
            if (logHistoryContainer) {
                logHistoryContainer.innerHTML = '<p class="text-center text-muted">Silakan login untuk melihat dan mencatat log belajar Anda.</p>';
            }
        }
    });

    const allMethods = {
        'Visual': ['Mind Mapping', 'Kartu Flash (Flashcards) dengan Gambar', 'Menonton Video Pembelajaran', 'Kode Warna pada Catatan'],
        'Auditori': ['Diskusi Kelompok atau Debat', 'Mendengarkan Rekaman (Podcast/Audiobook)', 'Membaca dengan Suara Keras', 'Menggunakan Jembatan Keledai (Mnemonics)'],
        'Kinestetik': ['Belajar Sambil Beraktivitas Fisik', 'Simulasi atau Permainan Peran (Role-Playing)', 'Membangun Model atau Diorama', 'Eksperimen atau Praktik Langsung']
    };

    function populateMethods() {
        for (const category in allMethods) {
            const optgroup = document.createElement('optgroup');
            optgroup.label = category;
            allMethods[category].forEach(method => {
                const option = document.createElement('option');
                option.value = method;
                option.textContent = method;
                optgroup.appendChild(option);
            });
            logMethodSelect.appendChild(optgroup);
        }
    }

    // --- Firestore Logic ---
    async function getLogsFromFirestore() {
        if (!currentUser) return [];
        const logsCol = collection(db, "users", currentUser.uid, "logs");
        const q = query(logsCol, orderBy("date", "desc"));
        const logSnapshot = await getDocs(q);
        return logSnapshot.docs.map(doc => ({ id: doc.id, ...doc.data() }));
    }

    async function renderLogs() {
        if (!currentUser) return;
        const logs = await getLogsFromFirestore();
        logHistoryContainer.innerHTML = '';

        if (logs.length === 0) {
            logHistoryContainer.innerHTML = '<p class="text-center text-muted">Belum ada sesi belajar yang dicatat.</p>';
            return;
        }

        logs.forEach(log => {
            const logCard = document.createElement('div');
            logCard.className = 'card log-entry-card mb-3';
            
            let feedbackHtml = `<button class="btn btn-sm btn-outline-primary feedback-btn" data-log-id="${log.id}" data-method="${log.method}">Beri Umpan Balik</button>`;
            
            if (log.feedback) {
                let stars = '';
                for (let i = 1; i <= 5; i++) {
                    stars += `<i class="fas fa-star ${i <= log.feedback.rating ? 'text-warning' : 'text-secondary'}"></i>`;
                }
                
                let feedbackDetails = '';
                if (log.feedback.successes && log.feedback.successes.length > 0) {
                    feedbackDetails += `<div class="mt-2"><small class="text-success">✓ ${log.feedback.successes.join(', ')}</small></div>`;
                }
                if (log.feedback.challenges && log.feedback.challenges.length > 0) {
                    feedbackDetails += `<div class="mt-1"><small class="text-danger">! ${log.feedback.challenges.join(', ')}</small></div>`;
                }
                
                feedbackHtml = `
                    <div class="feedback-section">
                        <div class="d-flex align-items-center">
                            <div class="log-rating me-2">${stars}</div>
                            <button class="btn btn-sm btn-outline-secondary feedback-btn" data-log-id="${log.id}" data-method="${log.method}">
                                <i class="fas fa-edit"></i>
                            </button>
                        </div>
                        ${feedbackDetails}
                    </div>
                `;
            }

            logCard.innerHTML = `
                <div class="card-body">
                    <div class="d-flex justify-content-between">
                        <h5 class="card-title">${log.subject}</h5>
                        <div class="d-flex align-items-center">
                            ${feedbackHtml}
                            <button class="btn btn-sm btn-outline-danger delete-log-btn ms-2" data-log-id="${log.id}">&times;</button>
                        </div>
                    </div>
                    <h6 class="card-subtitle mb-2 text-muted">${log.method}</h6>
                    <p class="card-text">${log.notes || ''}</p>
                    ${log.feedback && log.feedback.improvementNotes ? 
                        `<p class="card-text"><small class="text-muted"><i class="fas fa-lightbulb me-1"></i>${log.feedback.improvementNotes}</small></p>` 
                        : ''}
                </div>
                <div class="card-footer text-muted d-flex justify-content-between">
                    <span><i class="far fa-calendar-alt me-2"></i>${new Date(log.date).toLocaleDateString('id-ID', { dateStyle: 'long' })}</span>
                    <span><i class="far fa-clock me-2"></i>${log.duration} menit</span>
                </div>
            `;
            logHistoryContainer.appendChild(logCard);
        });

        // Add event listeners
        document.querySelectorAll('.delete-log-btn').forEach(btn => btn.addEventListener('click', e => deleteLog(e.currentTarget.dataset.logId)));
        document.querySelectorAll('.feedback-btn').forEach(btn => btn.addEventListener('click', e => prepareFeedbackModal(e.currentTarget.dataset.logId, e.currentTarget.dataset.method)));
    }

    async function addLog(e) {
        e.preventDefault();
        if (!currentUser) return;
        const newLog = {
            subject: document.getElementById('log-subject').value,
            method: document.getElementById('log-method').value,
            date: document.getElementById('log-date').value,
            duration: document.getElementById('log-duration').value,
            notes: document.getElementById('log-notes').value,
            rating: null,
            userId: currentUser.uid
        };
        await addDoc(collection(db, "users", currentUser.uid, "logs"), newLog);
        logForm.reset();
        logFormContainer.style.display = 'none';
        renderLogs();
    }

    async function deleteLog(logId) {
        if (!currentUser || !logId) return;
        if (confirm('Apakah Anda yakin ingin menghapus log ini?')) {
            await deleteDoc(doc(db, "users", currentUser.uid, "logs", logId));
            renderLogs();
        }
    }

    // --- Feedback Logic ---
    let currentRating = 0;

    function prepareFeedbackModal(logId, methodName) {
        hiddenLogIdInput.value = logId;
        feedbackMethodName.textContent = methodName;
        currentRating = 0;
        updateStars(0);
        
        // Reset checkboxes and textarea
        document.querySelectorAll('.form-check-input').forEach(checkbox => checkbox.checked = false);
        document.getElementById('improvement-notes').value = '';
        
        // Load existing feedback if any
        if (currentUser) {
            const logRef = doc(db, "users", currentUser.uid, "logs", logId);
            getDocs(logRef).then(doc => {
                if (doc.exists() && doc.data().feedback) {
                    const feedback = doc.data().feedback;
                    if (feedback.rating) {
                        currentRating = feedback.rating;
                        updateStars(currentRating);
                    }
                    if (feedback.successes) {
                        feedback.successes.forEach(success => {
                            const checkbox = document.getElementById(`success-${success}`);
                            if (checkbox) checkbox.checked = true;
                        });
                    }
                    if (feedback.challenges) {
                        feedback.challenges.forEach(challenge => {
                            const checkbox = document.getElementById(`challenge-${challenge}`);
                            if (checkbox) checkbox.checked = true;
                        });
                    }
                    if (feedback.improvementNotes) {
                        document.getElementById('improvement-notes').value = feedback.improvementNotes;
                    }
                }
            });
        }
        
        feedbackModal.show();
    }

    function updateStars(rating) {
        const stars = ratingStarsContainer.querySelectorAll('i');
        stars.forEach(star => star.classList.toggle('selected', star.dataset.value <= rating));
    }
    
    ratingStarsContainer.addEventListener('click', e => {
        if (e.target.matches('i')) {
            currentRating = parseInt(e.target.dataset.value);
            updateStars(currentRating);
        }
    });

    ratingStarsContainer.addEventListener('mouseover', e => {
        if (e.target.matches('i')) updateStars(parseInt(e.target.dataset.value));
    });

    ratingStarsContainer.addEventListener('mouseout', () => updateStars(currentRating));

    async function saveFeedback() {
        const logId = hiddenLogIdInput.value;
        if (!currentUser || !logId || currentRating === 0) {
            alert('Silakan pilih rating bintang terlebih dahulu.');
            return;
        }

        // Collect feedback data
        const successes = Array.from(document.querySelectorAll('input[id^="success-"]:checked'))
            .map(cb => cb.id.replace('success-', ''));
        
        const challenges = Array.from(document.querySelectorAll('input[id^="challenge-"]:checked'))
            .map(cb => cb.id.replace('challenge-', ''));
        
        const improvementNotes = document.getElementById('improvement-notes').value;

        const feedbackData = {
            rating: currentRating,
            successes,
            challenges,
            improvementNotes,
            updatedAt: new Date().toISOString()
        };

        const logRef = doc(db, "users", currentUser.uid, "logs", logId);
        await updateDoc(logRef, { 
            rating: currentRating,
            feedback: feedbackData
        });
        
        feedbackModal.hide();
        renderLogs();
    }

    // --- Event Listeners ---
    if (addLogBtn) {
        addLogBtn.addEventListener('click', () => logFormContainer.style.display = 'block');
    }
    if (cancelLogBtn && logForm && logFormContainer) {
        cancelLogBtn.addEventListener('click', () => {
            logForm.reset();
            logFormContainer.style.display = 'none';
        });
    }
    if (logForm) {
        logForm.addEventListener('submit', addLog);
    }
    if (saveFeedbackBtn) {
        saveFeedbackBtn.addEventListener('click', saveFeedback);
    }

    // --- Initial Load ---
    if (typeof populateMethods === 'function' && logMethodSelect) populateMethods();


}); 