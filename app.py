from flask import Flask, render_template, request
import subprocess
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("command.html")

@app.route('/Terminal', methods=['POST'])
def terminal():
    command = request.form.get('command')
    if command:
        try:
            home_directory = os.path.expanduser("~")
            full_command = f'cd {home_directory} && {command}'
            p = subprocess.Popen(full_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, cwd=home_directory)
            output, error = p.communicate()
            p_status = p.wait()
            if p_status == 0:
                c_output = output.decode(errors='replace')
            else:
                c_output = f"Error: {error.decode(errors='replace')}"
        except Exception as e:
            c_output = f"Exception occurred: {str(e)}"
    else:
        c_output = "No command received."

    return render_template("command.html", c_output=c_output)

if __name__ == "__main__":
    app.run(debug=True)
