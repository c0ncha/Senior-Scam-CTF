from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def scam_website():
        return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Critical System Alert</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/flipclock/0.7.7/flipclock.css">
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #f8d7da;
                color: #721c24;
                margin: 0;
                padding: 20px;
            }
            .alert-box {
                border: 2px solid #f5c6cb;
                background-color: #f8d7da;
                padding: 20px;
                display: inline-block;
                margin: 50px auto;
                border-radius: 10px;
            }
            .alert-box h1 {
                font-size: 2.5em;
                margin: 0 0 10px 0;
            }
            .alert-box p {
                font-size: 1.2em;
            }
            .phone-number {
                font-weight: bold;
                font-size: 1.5em;
                color: #c82333;
                margin-top: 20px;
            }
            #countdown {
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <div class="alert-box">
            <h1>CRITICAL SYSTEM ERROR!</h1>
            <p>Your computer has been locked due to suspicious activity.</p>
            <p>The hard drive will be deleted in:</p>
            <div id="countdown" class="clock"></div>
            <p class="phone-number">Call now to prevent data loss: 1-800-FAKE-NUMBER</p>
        </div>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/flipclock/0.7.7/flipclock.min.js"></script>
        <script>
            $(document).ready(function() {
                var clock = $('.clock').FlipClock(5 * 60, {
                    clockFace: 'MinuteCounter',
                    countdown: true,
                    callbacks: {
                        stop: function() {
                            alert('Your hard drive has been deleted!');
                        }
                    }
                });
            });
        </script>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)
