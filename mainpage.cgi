#!/usr/bin/python

import cgi
import MySQLdb
import smtplib

print 'Content-Type: text/html\n'
form=cgi.FieldStorage()
#import the email modules
from email.mime.text import MIMEText

#set default values
com = ""
valid = True

def mainpage(com):
	print'''
<!DOCTYPE html>
<html>
<body style='background-color:powderblue;'><h1 style='text-align:center;'>Welcome to Penetration Testing!</h1><br><br>
<form method="get" action="">
<textarea rows="4" cols="50" name="com" placeholder="Enter comment here..." value="%s"></textarea>
<input type="submit" name="send" value="Send">
<p><b>Warning !!</b> Comment box is currently not available</p>
</form>
</body>
</html>''' % (com)


if form.has_key("send"):
	com = form.getvalue('com')
	
	if com == None:
		com = ""

	if valid:
		try:
		#read host, user, password, database from topsecret file
			fin = open("/home/assign2/secret/topsecret", "r")
			dhconinfo = fin.read()
			host, user, passwd, db = dhconinfo.strip("\n").split("\n")
	
		except IOError:
			#show error if could'nt read topsecret file
			print "Cannot open file"
			exit()

		try:
			#connect to Mysql database
			db = MySQLdb.connect(host, user, passwd, db)
			cursor = db.cursor()	

			cursor.execute("INSERT INTO comment (comment) VALUES ('%s')" % (com))
			print "Comment " + com + " is inserted into database"
			db.commit()
			
			exit()
			#close database
			db.close()
					
		except MySQLdb.Error, e:
			#print error message for duplicate email	
			
			exit()

mainpage(com)
