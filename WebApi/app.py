import subprocess
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Endpoint to execute commands
@app.route('/api/run_command', methods=['POST'])
def run_command():
    command = request.json.get('command')

    if command:
        try:
            # Execute the command
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            output = result.stdout
            return jsonify({'output': output}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'No command provided'}), 400

# Serve the HTML file
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
