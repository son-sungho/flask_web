from flask import Flask ,render_template , flash , redirect , url_for, session, request, logging

import pymysql
from passlib.hash import pbkdf2_sha256
from data import Articles



app = Flask(__name__)
app.debug=True


db = pymysql.connect(host='localhost', 
                        port=3306, 
                        user='root', 
                        passwd='1234', 
                        db='myflaskapp')
cursor = db.cursor()


# init mysql
# mysql = MySQL(app)

# cur = mysql.connection.sursor()
# result = cur.execute("SELECT * FROM users;")

# users = cur.fatchall()
# print(result)

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




@app.route('/login',methods =['GET','POST'])
def login():
    if request.method == 'POST':
        id = request.form.get('email')
        pw = request.form.get('password')
        # print([id, pw])

        sql='SELECT * FROM users WHERE email = %s'
        cursor = db.cursor()
        cursor.execute(sql, [id])
        users = cursor.fetchone()
        print(users[4])

        # if users()

        if pbkdf2_sha256.verify(pw,users[4] ) :
            return redirect(url_for('home'))
        else:
            return 'LOGIN'
        return "LOGED PAGE"

    else:
        return "LOGED PAGE"


@app.route('/articles')
def article():
    print("Success")
    # return "TEST"
    articles = Articles()
    print(len(articles))
    return render_template('articles.html',articles=articles)

@app.route('/about')
def show_image():
    return render_template('about.html', hello = "Gray")

@app.route('/register',methods=['GET' ,'POST'])
def register():
    if request.method == 'POST':
        # data = request.body.get('author')
        name = request.form.get('name')
        email = request.form.get('email')
        password = pbkdf2_sha256.hash(request.form.get('password'))
        re_password = request.form.get('re_password')
        username = request.form.get('username')
        # name = form.name.data
        if(pbkdf2_sha256.verify(re_password, password)):
            print(pbkdf2_sha256.verify(re_password, password))
            cursor = db.cursor()
            sql = '''
                INSERT INTO users (name , email , username , password) 
                VALUES (%s ,%s,%s,%s )
             '''
            cursor.execute(sql , (name,email,username,password ))
            db.commit()
            

            # cursor = db.cursor()
            # cursor.execute('SELECT * FROM users;')
            # users = cursor.fetchall()
            return "register Success"
        else:
            return "Invalid Password"

            db.close()
    else:
        return render_template('register.html')
















# @app.route('/article', modules = ['GET','POST'])
# def articles():
#     print("Success")
#     articles = Articles()
#     print(len(articles))
#     return render_template('article.html', data=articles)
#     return "Success"


if __name__ =='__main__':
    # app.run(host='0.0.0.0', port='8080')
    app.run()