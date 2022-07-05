FROM handsonsecurity/seed-server:apache-php

COPY my_server.conf server_name.conf /etc/apache2/sites-available/
#COPY attacker32 /var/www/attacker32
#RUN  chown www-data /var/www/attacker32/zzz.txt 

RUN  a2ensite server_name.conf   \
     && a2ensite my_server.conf 
