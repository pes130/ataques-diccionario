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
echo "FTP_USERS=bisbal|$PASS_FTP_usuario1|/home/bisbal admin|$PASS_FTP_usuario1|/home/admin" > env/ftp.env
echo "SMB_PASS_usuario1=$PASS_SMB_usuario1" > env/samba.env
echo "SMB_PASS_usuario2=$PASS_SMB_usuario2" >> env/samba.env


# Dar permisos restrictivos para que no se puedan leer fácilmente si no eres root
chmod 600 env/*.env