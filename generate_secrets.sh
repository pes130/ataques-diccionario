#!/bin/bash
# Nos aseguramos de estar en el directorio de trabajo
mkdir -p /opt/ataques-diccionario
cd /opt/ataques-diccionario

# Crear directorio para las variables de entorno si no existe
mkdir -p env

# 1. Generar PIN del banco (4 dígitos, rellenando con ceros a la izquierda)
PIN=$(shuf -i 1000-9999 -n 1)
printf "BANCO_PIN=%04d\n" $PIN > env/banco.env

# 2. Generar Pass de Dragon Ball
DBZ_PASS=$(shuf -n 1 diccionario_seguro.txt)
echo "DBZ_PASS=$DBZ_PASS" > env/dbz.env

# 3. Elegimos una contraseña aleatoria del diccionario de servicios
PASS_FTP_usuario1=$(shuf -n 1 diccionario_servicios.txt)
PASS_FTP_usuario2=$(shuf -n 1 diccionario_servicios.txt)
PASS_SMB_usuario1=$(shuf -n 1 diccionario_servicios.txt)
PASS_SMB_usuario2=$(shuf -n 1 diccionario_servicios.txt)
# Guardamos en .env
cat << EOF > .env
FTP_USERS_VAR=bisbal|$PASS_FTP_usuario1|/home/bisbal admin|$PASS_FTP_usuario2|/home/admin
SMB_PASS_1=$PASS_SMB_usuario1
SMB_PASS_2=$PASS_SMB_usuario1
EOF


# Dar permisos restrictivos para que no se puedan leer fácilmente si no eres root
chmod 600 env/*.env