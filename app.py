import os
import socket
from flask import Flask, render_template_string

app = Flask(__name__)

# Basic HTML template embedded directly for simplicity
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Showcase App</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f6f9; text-align: center; padding: 50px; }
        .card { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); display: inline-block; }
        h1 { color: #333; }
        .meta { font-weight: bold; color: #007bff; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🚀 DevOps Portfolio Project</h1>
        <p>Status: <span style="color: green; font-weight: bold;">Healthy & Running</span></p>
        <hr>
        <p><strong>Hostname:</strong> <span class="meta">{{ hostname }}</span></p>
        <p><strong>Environment:</strong> <span class="meta">{{ env }}</span></p>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    hostname = socket.gethostname()
    env = os.getenv('APP_ENV', 'Development') # Default to Development if not set
    return render_template_string(HTML_TEMPLATE, hostname=hostname, env=env)

if __name__ == '__main__':
    # Run on all interfaces (0.0.0.0) so the container can expose it
    app.run(host='0.0.0.0', port=5000)

