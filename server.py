import sys
from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route('/')
def index():
    return 'CPSY 350 Project: GitHub Actions CI. SAIT ID:000123456\n'

host = "0.0.0.0"
port = 3000

# main driver function
if __name__ == '__main__':
    print(f"Running on http://{host}:{port}")
    sys.stdout.flush()
    serve(app, host=host, port=port)
