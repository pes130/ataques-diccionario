import os
from flask import Flask, request

app = Flask(__name__)

TARGET_USER = "pablo1985esteban"
TARGET_PASS = os.environ.get('DBZ_PASS', 'Kamehameha')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('pass')
        if user == TARGET_USER and password == TARGET_PASS:
            return "<h1>¡LOGIN CORRECTO! Has invocado a Shenron.</h1>"
        return "Error: Las bolas de dragón no han brillado.", 401

    return '''
        <style>body{background:#f0ad4e; font-family:sans-serif; text-align:center; margin-top:50px;}</style>
        <h2>Capsule Corp. - Acceso Restringido</h2>
        <form method="post">
            Usuario: <input type="text" name="user"><br><br>
            Password: <input type="password" name="pass"><br><br>
            <input type="submit" value="Entrar">
        </form>
        <p><i>Pista: El usuario es nombre+año+apellido del administrador (todo minúsculas).</i></p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)