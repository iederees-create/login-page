fetch('users.json')
    .then(response => response.json())
    .then(users => {
        document.getElementById('loginForm').addEventListener('submit', function(event) {
            event.preventDefault();
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            if (users[username] && users[username] === password) {
                document.getElementById('message').innerText = "Login successful!";
            } else {
                document.getElementById('message').innerText = "Invalid username or password.";
            }
        });
    })
    .catch(error => {
        document.getElementById('message').innerText = "Failed to load user data.";
    });

