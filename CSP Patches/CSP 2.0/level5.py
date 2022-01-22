from flask import Flask, render_template, request

app = Flask(__name__)

@app.after_request
def add_security_headers(resp):
    resp.headers['Content-Security-Policy']='script-src \'self\''
    return resp


@app.after_request
def apply_caching(response):
    response.headers['X-XSS-Protection'] = "0"
    return response

@app.route('/')
def level5():
    return render_template('welcome.html')

@app.route('/level5/frame/signup/')
def get():
    val = request.args.get('next')
    return render_template('signup.html', next=val)

@app.route('/level5/frame/signup/confirm/')
def con():
    return render_template('confirm.html',next='/')

if __name__ == "__main__":
  app.run()
