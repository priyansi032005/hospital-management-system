// Mock data for demonstration
const mockAppointments = [
    {
        id: 1,
        patientName: "John Doe",
        date: "2025-01-15T10:00:00",
        status: "BOOKED",
        reason: "Regular checkup and consultation"
    },
    {
        id: 2,
        patientName: "Jane Smith",
        date: "2025-01-16T14:30:00",
        status: "completed",
        reason: "Follow-up appointment"
    },
    {
        id: 3,
        patientName: "Robert Johnson",
        date: "2025-01-17T09:00:00",
        status: "pending",
        reason: "Initial consultation"
    },
    {
        id: 4,
        patientName: "Emily Davis",
        date: "2025-01-18T11:00:00",
        status: "scheduled",
        reason: "Annual physical examination"
    },
    {
        id: 5,
        patientName: "Michael Brown",
        date: "2025-01-19T15:00:00",
        status: "cancelled",
        reason: "Vaccination appointment"
    }
];

let appointments = [];
let loading = true;

// DOM Elements
const sidebar = document.getElementById('sidebar');
const menuToggle = document.getElementById('menuToggle');
const closeSidebar = document.getElementById('closeSidebar');
const startDateInput = document.getElementById('startDate');
const endDateInput = document.getElementById('endDate');
const loadingSkeleton = document.getElementById('loadingSkeleton');
const errorMessage = document.getElementById('errorMessage');
const noAppointments = document.getElementById('noAppointments');
const appointmentsList = document.getElementById('appointmentsList');

// Toggle Sidebar
menuToggle.addEventListener('click', () => {
    sidebar.classList.toggle('open');
});

closeSidebar.addEventListener('click', () => {
    sidebar.classList.remove('open');
});

// Handle resize
window.addEventListener('resize', () => {
    if (window.innerWidth >= 768) {
        sidebar.classList.remove('open');
    }
});

// Get status color class
function getStatusColor(status) {
    const statusColors = {
        completed: 'status-completed',
        pending: 'status-pending',
        cancelled: 'status-cancelled',
        scheduled: 'status-scheduled',
        booked: 'status-booked',
        BOOKED: 'status-booked'
    };
    return statusColors[status] || 'status-default';
}

// Check if appointment is eligible for video call
function isEligibleForVideoCall(appointment) {
    return appointment.status === 'BOOKED';
}

// Format date
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString();
}

// Format time
function formatTime(dateString) {
    const date = new Date(dateString);
    return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}

// Filter appointments by date range
function filterAppointmentsByDateRange() {
    const startDate = startDateInput.value;
    const endDate = endDateInput.value;

    if (!appointments.length) return [];

    return appointments.filter(app => {
        if (!startDate && !endDate) return true;

        const appointmentDate = new Date(app.date);
        appointmentDate.setHours(0, 0, 0, 0);

        if (startDate && endDate) {
            const start = new Date(startDate);
            start.setHours(0, 0, 0, 0);
            const end = new Date(endDate);
            end.setHours(23, 59, 59, 999);
            return appointmentDate >= start && appointmentDate <= end;
        }

        if (startDate) {
            const start = new Date(startDate);
            start.setHours(0, 0, 0, 0);
            return appointmentDate >= start;
        }

        if (endDate) {
            const end = new Date(endDate);
            end.setHours(23, 59, 59, 999);
            return appointmentDate <= end;
        }

        return true;
    });
}

// Handle video call
function handleStartMeeting(appointment) {
    alert(`Starting video call for appointment #${appointment.id} with ${appointment.patientName}`);
    // In real implementation: window.location.href = `/video-consultation/${appointment.id}`;
}

// Render appointments
function renderAppointments() {
    const filteredAppointments = filterAppointmentsByDateRange();

    appointmentsList.innerHTML = '';

    if (filteredAppointments.length === 0) {
        noAppointments.style.display = 'block';
        appointmentsList.style.display = 'none';
        return;
    }

    noAppointments.style.display = 'none';
    appointmentsList.style.display = 'block';

    filteredAppointments.forEach(appointment => {
        const card = document.createElement('div');
        card.className = 'appointment-card';

        const videoButton = isEligibleForVideoCall(appointment) ? `
            <button class="video-btn" onclick="handleStartMeeting(${JSON.stringify(appointment).replace(/"/g, '&quot;')})">
                <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <polygon points="23 7 16 12 23 17 23 7"></polygon>
                    <rect x="1" y="5" width="15" height="14" rx="2" ry="2"></rect>
                </svg>
                <span>Join Call</span>
            </button>
        ` : '';

        card.innerHTML = `
            <div class="appointment-header">
                <div class="appointment-info">
                    <div class="avatar">
                        <span>${appointment.patientName.charAt(0)}</span>
                    </div>
                    <div class="patient-details">
                        <h3>${appointment.patientName}</h3>
                        <div class="appointment-meta">
                            <div class="meta-item">
                                <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                                    <line x1="16" y1="2" x2="16" y2="6"></line>
                                    <line x1="8" y1="2" x2="8" y2="6"></line>
                                    <line x1="3" y1="10" x2="21" y2="10"></line>
                                </svg>
                                <span>${formatDate(appointment.date)}</span>
                            </div>
                            <div class="meta-item">
                                <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <circle cx="12" cy="12" r="10"></circle>
                                    <polyline points="12 6 12 12 16 14"></polyline>
                                </svg>
                                <span>${formatTime(appointment.date)}</span>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="appointment-actions">
                    <span class="status-badge ${getStatusColor(appointment.status)}">
                        ${appointment.status}
                    </span>
                    ${videoButton}
                </div>
            </div>
            ${appointment.reason ? `
                <div class="appointment-reason">
                    <p><span class="reason-label">Reason:</span> ${appointment.reason}</p>
                </div>
            ` : ''}
        `;

        appointmentsList.appendChild(card);
    });
}

// Fetch appointments (simulated with mock data)
function fetchAppointments() {
    loading = true;
    loadingSkeleton.style.display = 'block';
    appointmentsList.style.display = 'none';
    noAppointments.style.display = 'none';
    errorMessage.style.display = 'none';

    // Simulate API call
    setTimeout(() => {
        try {
            appointments = mockAppointments;
            loading = false;
            loadingSkeleton.style.display = 'none';
            renderAppointments();
        } catch (err) {
            loading = false;
            loadingSkeleton.style.display = 'none';
            errorMessage.textContent = 'An error occurred while fetching appointments.';
            errorMessage.style.display = 'block';
        }
    }, 1000);
}

// Event listeners for date filters
startDateInput.addEventListener('change', renderAppointments);
endDateInput.addEventListener('change', renderAppointments);

// Make handleStartMeeting global
window.handleStartMeeting = handleStartMeeting;

// Initial load
fetchAppointments();