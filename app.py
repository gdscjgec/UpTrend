from flask import Flask, render_template
from flask import redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

'''Define different functions which handles 
indivisual scripts for every website.
Example: 
For youtube trending video of the day in the scripts folder create a script
named youtube.py (scrape data using beautifulsoup, scrapy or selenium) and then incorpate that into a function
to be reflected on the index page.'''

@app.route('/youtube')
def youtube():
    #logic here
    pass

if __name__=='__main__':
    app.run(debug=True)