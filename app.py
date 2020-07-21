from flask import Flask ,render_template
from data import Articles

app = Flask(__name__)
app.debug=True

@app.route('/')
def index():
    print("Suceesss")
    # return "TEST"
    return render_template('home.html')

@app.route('/about')
def about():
    print("Suceesss")
    # return "TEST"
    return render_template('about.html')




@app.route('/articles')
def article():
    print("Success")
    # return "TEST"
    articles = Articles()
    print(len(articles))
    return render_template('articles.html',articles=articles)

@app.route('/test')
def show_image():
    return render_template('image.html')

if __name__ =='__main__':
    # app.run(host='0.0.0.0', port='8080')
    app.run()