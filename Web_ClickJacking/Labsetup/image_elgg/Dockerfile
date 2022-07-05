FROM handsonsecurity/seed-server:apache-php

FROM handsonsecurity/seed-elgg:original

ARG DOWNLOAD=/tmp/download
ARG WWWDir=/var/www/elgg
ARG DataDir=/var/elgg-data


# Load the elgg data (pictures, etc) 
RUN mkdir -p $DOWNLOAD 
COPY elgg/elgg_data.zip $DOWNLOAD
RUN mkdir -p $DataDir \
    && unzip -o $DOWNLOAD/elgg_data.zip  -d $DataDir \
    && chown -R www-data $DataDir \
    && chgrp -R www-data $DataDir \
    && rm -rf $DOWNLOAD 

# Copy the modified Elgg files (settings and disabling countermeasures)
COPY elgg/settings.php $WWWDir/elgg-config/
COPY elgg/views.php     $WWWDir/vendor/elgg/elgg/engine/lib/

# Enable the XSS site
COPY apache_elgg.conf server_name.conf  /etc/apache2/sites-available/
RUN  a2ensite server_name.conf \
     && a2ensite apache_elgg.conf 

# Start the Apache server
CMD service apache2 start && tail -f /dev/null

