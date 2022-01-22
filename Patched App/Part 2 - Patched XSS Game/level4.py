from threading import Timer
from flask import Flask
from flask.templating import render_template
from flask import request
import re


app = Flask(__name__)

@app.after_request
def apply_caching(response):
    response.headers['X-XSS-Protection'] = "0"
    return response

@app.route('/')
def level4():
    set_time = request.args.get('timer')
    set_times = re.sub('[^0-9 \n\.]','',str(set_time))
    print(set_times)
    if not set_times:
        return render_template('index4.html')  
    return render_template('timer.html', timer = set_times)


if __name__ == "__main__":
  app.run()
