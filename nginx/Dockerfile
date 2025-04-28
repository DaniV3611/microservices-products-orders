# Usa la imagen oficial de NGINX
FROM nginx:latest

# Copia el archivo de configuración NGINX al contenedor
COPY nginx.conf /etc/nginx/nginx.conf

# Expone el puerto 80 para acceso web
EXPOSE 80

# Comando para ejecutar NGINX en primer plano
CMD ["nginx", "-g", "daemon off;"]
