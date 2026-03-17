import os
from flask import Flask, request, render_template

app = Flask(__name__)

# Credenciales objetivo
TARGET_USER = "gustavo1983luque"
TARGET_PASS = os.environ.get('DBZ_PASS', 'Kamehameha')

@app.route('/', methods=['GET', 'POST'])
def login():
    mensaje = None
    estado = None

    if request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('pass')
        
        if user == TARGET_USER and password == TARGET_PASS:
            mensaje = "¡LOGIN CORRECTO! Has invocado a Shenron. Acceso a los planos del radar concedido."
            estado = "success" # Verde en Bootstrap
        else:
            mensaje = "Error de seguridad. Las bolas de dragón no han brillado."
            estado = "danger"  # Rojo en Bootstrap

    return render_template('index.html', mensaje=mensaje, estado=estado), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)