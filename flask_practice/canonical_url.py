from flask import Flask
app = Flask(__name__)

@app.route('/flask')
def hello_flask():
   return 'Hello Flask'

@app.route('/python/')
def hello_python():
   return 'Hello Python'

if __name__ == '__main__':
   app.run()

""" 
Both the rules appear similar but in the second rule, trailing slash (/) is used. 
As a result, it becomes a canonical URL. Hence, using /python or /python/ returns the 
same output. 
However, in case of the first rule, /flask/ URL results in 404 Not Found page

"""