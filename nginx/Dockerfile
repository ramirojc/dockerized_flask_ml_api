# Use the Nginx image
#FROM nginx:1.15.2
FROM nginx

# Remove the default nginx.conf
RUN rm /etc/nginx/nginx.conf

# Replace with our own nginx.conf
COPY nginx.conf /etc/nginx/