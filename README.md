# DPI902
DPI902 Penetration Testing Web Page

#!/bin/sh  
sudo cp login.php /usr/lib/cgi-bin  
echo 'Copied login.php to /usr/lib/cgi-bin/login.php'  
sudo cp mysenecaid.cgi /usr/lib/cgi-bin  
echo 'Copied mysenecaid.cgi to /usr/lib/cgi-bin/mysenecaid.cgi'  
firefox localhost/cgi-bin/mysenecaid.cgi  



# Installation
- Download web application - mysenecaid.cgi
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
