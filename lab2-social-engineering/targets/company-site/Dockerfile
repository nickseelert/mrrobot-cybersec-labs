FROM php:7.4-apache

# Install required packages
RUN apt-get update && apt-get install -y \
    libpng-dev \
    libjpeg-dev \
    libfreetype6-dev \
    zip \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Configure GD library
RUN docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-install gd

# Enable Apache modules
RUN a2enmod rewrite headers

# Copy website files
COPY ./content /var/www/html/

# Set permissions
RUN chown -R www-data:www-data /var/www/html

# Create directories for employee data
RUN mkdir -p /var/www/html/data/employees /var/www/html/data/documents

EXPOSE 80

CMD ["apache2-foreground"]