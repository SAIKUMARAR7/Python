from flask import *

app = Flask(__name__)
@app.route('/login',methods=["POST"])
def hello():
    s=request.form['name']
    pas= request.form['password']
    if s=='sai' and pas=='password':
        l=[s,pas]
    return str(l)

if __name__ == '__main__':
   app.run('0.0.0.0',port='9000',debug='true')

 #  HTML code
 <html>
   <body>
      <form action = "http://localhost:9000/login" method = "POST">
         <table>
        <tr><td>Name</td>
        <td><input type ="text" name ="name"></td></tr>
             <tr><td>Password</td>
             <td><input type ="password" name ="password"></td></tr>
        <tr><td><input type = "submit"></td></tr>
    </table>
      </form>
   </body>
</html>
 
 
 
 
 
