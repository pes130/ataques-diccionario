import os
import time
from flask import Flask, request

app = Flask(__name__)

# Lee el PIN inyectado por Docker (generado por el script .sh)
PIN_CORRECTO = os.environ.get('BANCO_PIN', '0000')
intentos = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    ip = request.remote_addr
    if request.method == 'POST':
        # Handicap: bloqueo temporal si hay muchos intentos seguidos
        if intentos.get(ip, 0) > 15:
            time.sleep(1.5)
        
        pin = request.form.get('pin')
        if pin == PIN_CORRECTO:
            return "<h1>ACCESO CONCEDIDO. Saldo: 999.999 Zenos.</h1>"
        else:
            intentos[ip] = intentos.get(ip, 0) + 1
            return "PIN INCORRECTO", 401
            
    return '''
        <style>body{font-family:sans-serif; text-align:center; margin-top:50px;}</style>
        <h2>Banco Central de la Capital del Oeste</h2>
        <form method="post">
            PIN (4 cifras): <input type="text" name="pin" maxlength="4">
            <input type="submit" value="Validar">
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)