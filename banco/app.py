import os
import time
from flask import Flask, request, render_template

app = Flask(__name__)

# Lee el PIN inyectado por Docker (generado por el script .sh)
PIN_CORRECTO = os.environ.get('BANCO_PIN', '0000')
intentos = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    # Ojo con esto, que aquí tienes la trampa para saltarte la restricción por IP de 15 intentos.
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    mensaje = None
    estado = None

    if request.method == 'POST':
        # Handicap: bloqueo temporal si hay muchos intentos seguidos
        if intentos.get(ip, 0) > 15:
            time.sleep(1.5)
        
        pin = request.form.get('pin')
        if pin == PIN_CORRECTO:
            mensaje = "ACCESO CONCEDIDO. Saldo: 999.999 €."
            estado = "success" # Clase de Bootstrap para verde
        else:
            intentos[ip] = intentos.get(ip, 0) + 1
            mensaje = "PIN INCORRECTO"
            estado = "danger"  # Clase de Bootstrap para rojo
            
    return render_template('index.html', mensaje=mensaje, estado=estado), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)