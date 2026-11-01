from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>Changing Background</title>
        <style>
            body {
                background: linear-gradient(45deg, red, blue, purple);
                background-size: 400% 400%;
                animation: colorChange 5s infinite;
            }

            @keyframes colorChange {
                0% {
                    background-position: 0% 50%;
                }
                50% {
                    background-position: 100% 50%;
                }
                100% {
                    background-position: 0% 50%;
                }
            }
        </style>
    </head>

    <body>
        <h1>Welcome to Flask</h1>
        <h2>Background Color is Changing!</h2>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
