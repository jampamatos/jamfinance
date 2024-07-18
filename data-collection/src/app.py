from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return 'Welcome to the Jamfinance Data Collection Service!'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)