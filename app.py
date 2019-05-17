from flask import Flask, render_template, json, request
import pymysql
app = Flask(__name__)


class Database:
    def __init__(self):
        host = "127.0.0.1"
        user = "root"
        password = "1q2w3e4r"
        db = "BucketList"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()
    def list_employees(self, user_name, password):
        sql = "SELECT user_name, user_username, user_password FROM tbl_user where user_name=%s and user_password=%s";
        un = (user_name, password)
        #self.cur.execute("SELECT user_name, user_username, user_password FROM tbl_user")
        self.cur.execute(sql, un)
        result = self.cur.fetchall()
        return result


@app.route("/")
def main():
	return render_template('index.html')


@app.route("/sushi")
def sushi():
	return render_template('sushi.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp',methods=['POST'])
def signUp():
 
    _name = request.form['inputName']
    _password = request.form['inputPassword']

    db = Database()
    emps = db.list_employees(_name, _password)
 
    if len(emps) == 0:
      return json.dumps({'status':'failed'})
    elif len(emps) == 1 and emps[0]['user_password'] == _password:
      return json.dumps({'status':'success'})
      

