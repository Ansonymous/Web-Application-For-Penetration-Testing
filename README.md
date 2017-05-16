# DPI902
DPI902 Penetration Testing Web Page


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
