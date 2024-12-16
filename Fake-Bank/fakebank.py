from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/')
def fake_bank_home():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Trusted Bank - Secure Banking</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                color: #333;
                margin: 0;
                padding: 0;
                text-align: center;
            }
            .container {
                max-width: 600px;
                margin: 50px auto;
                padding: 20px;
                background: #fff;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #2c3e50;
            }
            form {
                margin: 20px 0;
            }
            input[type="text"], input[type="password"] {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ccc;
                border-radius: 5px;
                box-sizing: border-box;
            }
            input[type="submit"] {
                background-color: #3498db;
                color: white;
                padding: 10px 15px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            input[type="submit"]:hover {
                background-color: #2980b9;
            }
            .alert {
                color: #c0392b;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to Trusted Bank</h1>
            <p>Your secure banking partner.</p>
            <form method="POST" action="/login">
                <input type="text" name="username" placeholder="Username" required>
                <input type="password" name="password" placeholder="Password" required>
                <input type="submit" value="Login">
            </form>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)

@app.route('/login', methods=['POST'])
def fake_login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Simulate showing a hacked message and a 0 balance
    response_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Trusted Bank - Account Hacked</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #fff3f3;
                color: #333;
                text-align: center;
                padding: 20px;
            }}
            .alert {{
                color: #c0392b;
                font-weight: bold;
            }}
            .balance {{
                margin: 20px 0;
                font-size: 1.5em;
                color: #e74c3c;
            }}
        </style>
    </head>
    <body>
        <h1>Account Overview</h1>
        <p>Welcome, {username}.</p>
        <p class="alert">WARNING: Your account has been compromised!</p>
        <p class="balance">Current Balance: $0.00</p>
        <p>Please contact our support team immediately.</p>
    </body>
    </html>
    """
    return render_template_string(response_content)

if __name__ == "__main__":
    app.run(debug=True)
