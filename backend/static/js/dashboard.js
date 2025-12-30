// API Configuration
const API_BASE_URL = 'http://your-api-url.com/api'; // Replace with your actual API URL

// Global state
let doctorData = null;
let appointments = [];

// Initialize dashboard
document.addEventListener('DOMContentLoaded', function() {
    loadDoctorProfile();
    loadAppointmentStats();
    loadAppointmentsList();
    initializeCharts();
});

// Load Doctor Profile
async function loadDoctorProfile() {
    try {
        // Replace with your actual API endpoint
        const response = await fetch(`${API_BASE_URL}/doctor/profile`, {
            headers: {
                'Authorization': `Bearer ${getAuthToken()}`,
                'Content-Type': 'application/json'
            }
        });
        
        if (!response.ok) throw new Error('Failed to load profile');
        
        doctorData = await response.json();
        
        // Update UI with doctor info
        document.getElementById('doctorName').textContent = doctorData.name || 'Doctor';
        
    } catch (error) {
        console.error('Error loading profile:', error);
        // Use fallback data for demo
        doctorData = {
            name: 'Dr. Daniel Bruk',
            specialization: 'Cardiologist',
            email: 'daniel.bruk@hospital.com',
            phone: '+1234567890'
        };
        document.getElementById('doctorName').textContent = doctorData.name;
    }
}

// Load Appointment Statistics
async function loadAppointmentStats() {
    try {
        const response = await fetch(`${API_BASE_URL}/doctor/appointments/stats`, {
            headers: {
                'Authorization': `Bearer ${getAuthToken()}`,
                'Content-Type': 'application/json'
            }
        });
        
        if (!response.ok) throw new Error('Failed to load stats');
        
        const stats = await response.json();
        
        // Update stats cards
        document.getElementById('totalAppointments').textContent = stats.total || 0;
        document.getElementById('pendingAppointments').textContent = stats.pending || 0;
        document.getElementById('approvedAppointments').textContent = stats.approved || 0;
        document.getElementById('canceledAppointments').textContent = stats.canceled || 0;
        
    } catch (error) {
        console.error('Error loading stats:', error);
        // Use fallback data for demo
        document.getElementById('totalAppointments').textContent = '180';
        document.getElementById('pendingAppointments').textContent = '38';
        document.getElementById('approvedAppointments').textContent = '120';
        document.getElementById('canceledAppointments').textContent = '7';
    }
}

// Load Appointments List
async function loadAppointmentsList() {
    try {
        const response = await fetch(`${API_BASE_URL}/doctor/appointments`, {
            headers: {
                'Authorization': `Bearer ${getAuthToken()}`,
                'Content-Type': 'application/json'
            }
        });
        
        if (!response.ok) throw new Error('Failed to load appointments');
        
        appointments = await response.json();
        renderAppointmentsTable(appointments);
        
    } catch (error) {
        console.error('Error loading appointments:', error);
        // Use fallback data for demo
        appointments = [
            {
                id: 1,
                patientName: 'John Doe',
                medicine: 'Aspirin',
                digestion: 'After meals',
                side: 'Nausea',
                disease: 'Hypertension',
                status: 'pending',
                date: '2024-12-27',
                time: '10:00 AM'
            },
            {
                id: 2,
                patientName: 'Jane Smith',
                medicine: 'Metformin',
                digestion: 'Before meals',
                side: 'None',
                disease: 'Diabetes',
                status: 'approved',
                date: '2024-12-28',
                time: '02:00 PM'
            },
            {
                id: 3,
                patientName: 'Bob Johnson',
                medicine: 'Lisinopril',
                digestion: 'Morning',
                side: 'Dizziness',
                disease: 'Heart Disease',
                status: 'completed',
                date: '2024-12-26',
                time: '11:30 AM'
            }
        ];
        renderAppointmentsTable(appointments);
    }
}

// Render Appointments Table
function renderAppointmentsTable(data) {
    const tbody = document.getElementById('appointmentsTable');
    tbody.innerHTML = '';
    
    data.forEach(appointment => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td><input type="checkbox"></td>
            <td>${appointment.medicine || 'N/A'}</td>
            <td>${appointment.digestion || 'N/A'}</td>
            <td>${appointment.side || 'None'}</td>
            <td>${appointment.disease || 'N/A'}</td>
            <td>
                <button class="action-btn" onclick="openAppointmentModal(${appointment.id})">
                    Update
                </button>
            </td>
        `;
        tbody.appendChild(row);
    });
}

// Open Profile Modal
function openProfileModal() {
    const modal = document.getElementById('profileModal');
    modal.classList.add('active');
    
    // Populate form with current data
    if (doctorData) {
        document.getElementById('editName').value = doctorData.name || '';
        document.getElementById('editSpecialization').value = doctorData.specialization || '';
        document.getElementById('editEmail').value = doctorData.email || '';
        document.getElementById('editPhone').value = doctorData.phone || '';
    }
}

// Close Profile Modal
function closeProfileModal() {
    const modal = document.getElementById('profileModal');
    modal.classList.remove('active');
}

// Handle Profile Form Submit
document.getElementById('profileForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const updatedData = {
        name: document.getElementById('editName').value,
        specialization: document.getElementById('editSpecialization').value,
        email: document.getElementById('editEmail').value,
        phone: document.getElementById('editPhone').value
    };
    
    try {
        const response = await fetch(`${API_BASE_URL}/doctor/profile`, {
            method: 'PUT',
            headers: {
                'Authorization': `Bearer ${getAuthToken()}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(updatedData)
        });
        
        if (!response.ok) throw new Error('Failed to update profile');
        
        const result = await response.json();
        
        // Update local data
        doctorData = result;
        document.getElementById('doctorName').textContent = result.name;
        
        alert('Profile updated successfully!');
        closeProfileModal();
        
    } catch (error) {
        console.error('Error updating profile:', error);
        alert('Failed to update profile. Please try again.');
    }
});

// Open Appointment Modal
function openAppointmentModal(appointmentId) {
    const modal = document.getElementById('appointmentModal');
    modal.classList.add('active');
    
    // Find appointment data
    const appointment = appointments.find(a => a.id === appointmentId);
    
    if (appointment) {
        document.getElementById('appointmentId').value = appointment.id;
        document.getElementById('patientName').value = appointment.patientName;
        document.getElementById('appointmentDate').value = `${appointment.date} ${appointment.time}`;
        document.getElementById('appointmentStatus').value = appointment.status;
    }
}

// Close Appointment Modal
function closeAppointmentModal() {
    const modal = document.getElementById('appointmentModal');
    modal.classList.remove('active');
}

// Handle Appointment Form Submit
document.getElementById('appointmentForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const appointmentId = document.getElementById('appointmentId').value;
    const status = document.getElementById('appointmentStatus').value;
    const notes = document.getElementById('appointmentNotes').value;
    
    try {
        const response = await fetch(`${API_BASE_URL}/doctor/appointments/${appointmentId}`, {
            method: 'PATCH',
            headers: {
                'Authorization': `Bearer ${getAuthToken()}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ status, notes })
        });
        
        if (!response.ok) throw new Error('Failed to update appointment');
        
        const result = await response.json();
        
        // Update local data
        const index = appointments.findIndex(a => a.id == appointmentId);
        if (index !== -1) {
            appointments[index].status = status;
        }
        
        // Re-render table
        renderAppointmentsTable(appointments);
        
        // Reload stats
        loadAppointmentStats();
        
        alert('Appointment updated successfully!');
        closeAppointmentModal();
        
    } catch (error) {
        console.error('Error updating appointment:', error);
        alert('Failed to update appointment. Please try again.');
    }
});

// Close modal when clicking outside
window.onclick = function(event) {
    const profileModal = document.getElementById('profileModal');
    const appointmentModal = document.getElementById('appointmentModal');
    
    if (event.target === profileModal) {
        closeProfileModal();
    }
    if (event.target === appointmentModal) {
        closeAppointmentModal();
    }
}

// Initialize Charts (using Chart.js or similar library)
function initializeCharts() {
    // Simple placeholder for charts
    // In production, use Chart.js, Recharts, or similar library
    
    const chart1 = document.getElementById('chart1');
    const chart2 = document.getElementById('chart2');
    const healthChart = document.getElementById('healthChart');
    
    if (chart1) {
        // Initialize chart 1
        drawSimpleChart(chart1, [65, 70, 75, 72, 80, 85, 90]);
    }
    
    if (chart2) {
        // Initialize chart 2
        drawSimpleChart(chart2, [60, 65, 70, 75, 72, 68, 70]);
    }
    
    if (healthChart) {
        // Initialize health chart
        drawSimpleChart(healthChart, [120, 118, 122, 119, 121, 120, 118, 119, 120, 122, 125, 130]);
    }
}

// Simple chart drawing function
function drawSimpleChart(canvas, data) {
    const ctx = canvas.getContext('2d');
    const width = canvas.width = canvas.offsetWidth;
    const height = canvas.height = canvas.offsetHeight;
    
    ctx.clearRect(0, 0, width, height);
    ctx.strokeStyle = '#48B3AF';
    ctx.lineWidth = 2;
    ctx.beginPath();
    
    const step = width / (data.length - 1);
    const max = Math.max(...data);
    const min = Math.min(...data);
    const range = max - min;
    
    data.forEach((value, index) => {
        const x = index * step;
        const y = height - ((value - min) / range) * (height - 20) - 10;
        
        if (index === 0) {
            ctx.moveTo(x, y);
        } else {
            ctx.lineTo(x, y);
        }
    });
    
    ctx.stroke();
}

// Get auth token (implement based on your auth system)
function getAuthToken() {
    // Return the stored auth token
    return localStorage.getItem('authToken') || 'demo-token';
}

// Utility function to format date
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', { 
        year: 'numeric', 
        month: 'short', 
        day: 'numeric' 
    });
}

// Refresh data periodically (every 5 minutes)
setInterval(() => {
    loadAppointmentStats();
    loadAppointmentsList();
}, 300000);