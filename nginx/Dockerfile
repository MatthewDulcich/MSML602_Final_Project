# Use the Nginx image
FROM nginx

# Remove default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf
#RUN rm /Users/matthewdulcich/miniforge3/envs/DSFP602/etc/nginx/nginx.conf.default

# Replace with our own nginx.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf
#COPY nginx.conf /etc/nginx/conf.d/
#COPY nginx.conf /Users/matthewdulcich/miniforge3/envs/DSFP602/etc/nginx/nginx.conf.default