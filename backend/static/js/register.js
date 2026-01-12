console.log("Register JS loaded");

const SITE_URL = window.location.origin;
const REGISTER_API = `${SITE_URL}/api/register/`;

document.querySelector("form").addEventListener("submit", async function (e) {
    e.preventDefault();

    // Get input values
    const username = document.querySelector("input[name='username']").value.trim();
    const password = document.querySelector("input[name='password']").value.trim();
    const role = document.querySelector("select[name='role']").value;

    // Basic validation
    if (!username || !password || !role) {
        alert("Please fill all fields");
        return;
    }

    try {
        const response = await fetch(REGISTER_API, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password, role })
        });

        const data = await response.json();
        console.log("Response Data:", data);

        if (!response.ok) {
            alert(data.detail || "Registration failed");
            return;
        }

        alert("Registration successful! Please login.");
        window.location.href = "/login/"; // Redirect to login page

    } catch (err) {
        console.error(err);
        alert("Server error. Try again.");
    }
});
