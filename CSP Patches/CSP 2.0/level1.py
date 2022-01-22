from flask import Flask , request
from flask.templating import render_template_string

page_header = """
<!doctype html>
<html>
  <head>
    <!-- Internal game scripts/styles, mostly boring stuff -->
    <script src="/static/game-frame.js"></script>
    <link rel="stylesheet" href="/static/game-frame-styles.css" />
  </head>
 
  <body id="level1">
    <img src="/static/logos/level1.png">
      <div>
"""
 
page_footer = """
    </div>
  </body>
</html>
"""
 
main_page_markup = """
<form action="" method="GET">
  <input id="query" name="query" value=" "
    onfocus="this.value=''">
  <input id="button" type="submit" value="Search">
</form>
"""
 
app = Flask(__name__)

@app.after_request
def apply_caching(response):
    response.headers['X-XSS-Protection'] = "0"
    return response

@app.after_request
def add_security_headers(resp):
    resp.headers['Content-Security-Policy']='default-src \'self\''
    return resp

@app.route('/')
def frame():
    subject = request.args.get('query')
    if subject != None:
        message = "Sorry, no results were found for <b>" + subject + "</b>."
        message += " <a href='?'>Try again</a>."
        return render_template_string(page_header + message + page_footer)
    return render_template_string(page_header + main_page_markup + page_footer)

if __name__ == "__main__":
  app.run()