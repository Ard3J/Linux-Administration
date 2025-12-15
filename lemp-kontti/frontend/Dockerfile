# syntax=docker/dockerfile:1
FROM nginx:1.27-alpine

# Copy Nginx config and static assets
COPY lemp-kontti/frontend/nginx.conf /etc/nginx/nginx.conf
COPY lemp-kontti/frontend/index.html /usr/share/nginx/html/index.html

EXPOSE 80
