FROM nginx:latest
RUN apt-get update && apt-get install procps -y
RUN apt-get install --no-install-recommends -y apache2-utils
RUN mkdir -p /etc/pwd
RUN mkdir -p /home/app/staticfiles
RUN mkdir -p /home/secure
RUN mkdir -p /home/secure/file