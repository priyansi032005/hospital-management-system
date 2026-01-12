console.log("Login JS loaded");

const SITE_URL = window.location.origin;
const LOGIN_API = `${SITE_URL}/api/login/`;

document.getElementById("login-form").addEventListener("submit", async function (e) {
    e.preventDefault();

    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();

    try {
        const response = await fetch(LOGIN_API, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();
        console.log("Response Data:", data);

        if (!response.ok) {
            alert(data.detail || "Invalid credentials");
            return;
        }

        // Save JWT tokens in localStorage
        localStorage.setItem("access", data.access);
        console.log("Access Token:", data.access);
        localStorage.setItem("refresh", data.refresh);
        console.log("Refresh Token:", data.refresh);
        console.log("User Role:", data.role);

        // Redirect to dashboard
        if (data.role === "PATIENT") {
            window.location.href = "/patient/dashboard/";
        } else if (data.role === "DOCTOR") {
            window.location.href = "/doctor/dashboard/";
        } else if (data.role === "ADMIN") {
            window.location.href = "/admin/";
        } else {
            alert("Unknown user role");
        }

    } catch (err) {
        console.error(err);
        alert("Server error. Try again.");
    }
});
