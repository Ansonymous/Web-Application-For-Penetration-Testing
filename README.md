# Web Penetration Testing
This is a web penetration testing application with registration system and login system. Used for school project purposes. 
Contributed by Anson Tan

# Installation
- Download web application - registration.cgi and login.cgi
- Install Python and Apache
- Edit Apache confifuration file for access cgi-bin folder
- Place login.cgi and mysenecaid.cgi into CGI file location

# Local host web page Link
http://localhost/cgi-bin/mysenecaid.cgi

# HTML web page location
/var/www

# CGI file location
/usr/lib/cgi-bin

# Apache configuration file
/etc/apache2/apache2.conf

# Add CGI into Apache configuration
ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/  
<Directory /usr/lib/cgi-bin>  
Options +ExecCGI  
AddHandler cgi-script .cgi .py  
Options FollowSymLinks  
Require all granted  
</Directory>  

# Enable script modules
sudo a2enmod cgi

# Restart apache service
sudo service apache2 restart
