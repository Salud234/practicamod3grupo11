# Usa la imagen oficial de PostgreSQL
FROM postgres:latest
# Copia el script SQL al directorio de inicialización de PostgreSQL
# PostgreSQL ejecutará automáticamente los scripts en /docker-entrypointinitdb.d/
COPY init.sql /docker-entrypoint-initdb.d/
COPY save_data.sql /docker-entrypoint-initdb.d/