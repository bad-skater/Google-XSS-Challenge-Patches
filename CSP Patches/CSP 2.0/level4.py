from threading import Timer
from flask import Flask
from flask.templating import render_template
from flask import request



app = Flask(__name__)

@app.after_request
def apply_caching(response):
    response.headers['X-XSS-Protection'] = "0"
    return response


@app.route('/')
def level4():
    set_time = request.args.get('timer')
    if not set_time:
        return render_template('index4.html')  
    return render_template('timer.html', timer = set_time)

if __name__ == "__main__":
  app.run()
