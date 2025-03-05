from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

# Simulating a basic login system
users = {
    "user1": "password1",
    "user2": "password2"
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Simple login form
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check for valid username/password
        if username in users and users[username] == password:
            next_url = request.args.get('next', '/dashboard')
            return redirect(next_url)  # Open redirect vulnerability
        else:
            return "Invalid credentials", 403

    return render_template_string("""
        <form method="POST">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    """)

@app.route('/dashboard')
def dashboard():
    return "Welcome to your dashboard!"

if __name__ == '__main__':
    app.run(debug=True)
