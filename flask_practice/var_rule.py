from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

if __name__ == '__main__':
   app.run(debug = True)

"""
Save the above script as hello.py and run it from Python shell. 
Next, open the browser and enter URL http://localhost:5000/hello/TutorialsPoint.

The following output will be displayed in the browser.

Hello TutorialsPoint!
"""


