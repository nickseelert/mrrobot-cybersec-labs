FROM php:7.4-apache

# Install additional packages
RUN apt-get update && apt-get install -y \
    curl \
    netcat-traditional \
    telnet \
    && rm -rf /var/lib/apt/lists/*

# Enable Apache modules
RUN a2enmod rewrite headers

# Copy vulnerable web application
COPY ./app /var/www/html/

# Set permissions
RUN chown -R www-data:www-data /var/www/html

# Configure Apache for vulnerable setup
RUN echo "ServerTokens Full" >> /etc/apache2/apache2.conf && \
    echo "ServerSignature On" >> /etc/apache2/apache2.conf

# Create some interesting files for discovery
RUN mkdir -p /var/www/html/backup && \
    echo "admin:coffee123" > /var/www/html/backup/.htpasswd && \
    echo "Database: customers.db" > /var/www/html/backup/config.txt

EXPOSE 80

CMD ["apache2-foreground"]