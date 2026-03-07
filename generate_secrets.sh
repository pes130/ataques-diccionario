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

# Dar permisos restrictivos para que no se puedan leer fácilmente si no eres root
chmod 600 env/*.env