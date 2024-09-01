# FLASKUNTU Remote Command Line Manager

This is a Flask application that allows you to manage your command line remotely through a web interface. 

## Features

- Execute command line commands remotely
- View the output of executed commands in the web interface
- Simple and intuitive UI

## Prerequisites

- Python 3.x
- Flask
- Gunicorn

## Installation

1. Clone the repository:
```
https://github.com/zaidrabeh/Flaskuntu.git
cd Flaskuntu
```

2. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
3. Install the required packages:
```
pip install -r requirements.txt
```
## Running the Application

1. Start the Flask application locally:
```
python app.py
```
2. Open your browser and go to http://localhost:5000 to access the application.

## Deploying the Application

### To deploy the application using Gunicorn:

1. Create a Procfile in the root directory of your project:
```
web: gunicorn app:app
```
2. Install Gunicorn if you haven't already:
```
pip install gunicorn
```
3. Run Gunicorn:
```
gunicorn app:app
```
## Usage

1. Open your web browser and navigate to http://localhost:5000.
2. Enter your command in the input field and click on "See output".
3. The output of the command will be displayed on the same page.

## Security Warning

Be careful when using this application, especially on public networks. Executing arbitrary commands can be very dangerous and may compromise your system's security. Use it only in a secure and trusted environment.

