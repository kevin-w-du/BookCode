FROM handsonsecurity/seed-server:apache-php

COPY my_server.conf server_name.conf /etc/apache2/sites-available/
#COPY bank32 /var/www/bank32
#COPY bank99 /var/www/bank99

RUN  a2ensite server_name.conf   \
     && a2ensite my_server.conf 
