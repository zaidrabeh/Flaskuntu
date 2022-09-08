from flask import Flask, render_template, redirect, request
import subprocess
app = Flask(__name__) 

@app.route('/', methods=['GET'])
def output():
	return render_template("command.html")


@app.route('/Call', methods=['POST', 'GET'])
def Call(c_output = None):
	if request.method == 'POST':
		command = request.form.get('command')
		p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
		(output, err) = p.communicate()
		p_status = p.wait()
		print ("Command output : ",output.decode())
		c_output = output.decode()
	return render_template("command.html", c_output = c_output)

if __name__ == "__main__":
	app.run()
