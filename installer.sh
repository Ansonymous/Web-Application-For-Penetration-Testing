#!/bin/sh
sudo cp login.php /usr/lib/cgi-bin
echo 'Copied login.php to /usr/lib/cgi-bin/login.php'
sudo cp mysenecaid.cgi /usr/lib/cgi-bin
echo 'Copied mysenecaid.cgi to /usr/lib/cgi-bin/mysenecaid.cgi'
firefox localhost/cgi-bin/mysenecaid.cgi
