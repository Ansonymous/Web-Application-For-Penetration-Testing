#!/usr/bin/python

import cgi, re
import MySQLdb
import smtplib
import hashlib

print 'Content-Type: text/html\n'
form=cgi.FieldStorage()
#import the email modules
from email.mime.text import MIMEText

#set default values
contact = ""
password = ""
contactErr = ""
passwordErr = ""
valid = True

def mainpage(contact, contactErr, password, passwordErr):
	print'''<body style='background-color:powderblue;'><h1 style='text-align:center;'>Welcome to Penetration Testing!</h1><br><br>
<form action="" id="usrform">
<textarea rows="4" cols="50" name="comment" form="usrform">Enter comment here...</textarea>
<input type="submit" name="send" value="Send">
</form></body>'''


#display input form and print error messages if invalid
def displayform(contact, contactErr, password, passwordErr):
	print '''
<!DOCTYPE html>
<html>
<body style="background-color:powderblue;">
<h2>Penetration Testing Login</h2><br>
<form method="post" action="">
<table>
<tr>
<td>Email</td><td><input type="text" placeholder="Enter Email" name="contact" value="%s" required><font color="red">%s</font></td>
</tr>
<tr>
<td>Password</td><td><input type="password" placeholder="Enter Password" name="password" value="%s" required><font color="red">%s</font></td>
</tr>
<td></td><td><input type="submit" name="submit" value="Login"/><a href="registration.cgi">Registration</a></td>
</table>
</form>
</body>
</html>
''' % (contact, contactErr, password, passwordErr)

#if submit botton is clicked
if form.has_key("submit"):
	
	#get values from input forms
	contact = form.getvalue('contact')
	password = form.getvalue('password')

	#if input forms are blank, set to null
	if contact == None:
	        contact = ""
	if password == None:
        	password = ""
	
	#validation for input, set error in red colour if does not match
	#validation for password
	if not re.match("^ *[^ ]{8,} *$", password):
		valid = False
		passwordErr = "Invalid Password"
	#validation for email
	if not re.match("^[^\-_.][A-Za-z\d\-\.\_]*@[A-Za-z\d\-\.\_]{1,}.[A-Za-z]{2,}$", contact):
		valid = False
		contactErr = "Invalid Email"
	
	#if inputs are valid then connect to database
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

			#encrypt password with MD5
			hashpwd = hashlib.md5(password).hexdigest()
			#select email from table
			cursor.execute("SELECT email FROM mfsuser where email = ('%s') AND password = ('%s')" % (contact, hashpwd))
			result = cursor.fetchall()
			print "Email - " + result[0][0]
			#commit changes in the database
			db.commit()
		
			if result[0][0] == contact:
				mainpage(contact, contactErr, password, passwordErr)
			else:
				print "Invalid Email or Password"

			exit()
			#close database
			db.close()
					
		except MySQLdb.Error, e:
			#print error message for duplicate email	
			contactErr =  "Email or password is incorrect"
			#redisplay form with remembered data
			displayform(contact, contactErr,password, passwordErr)
			exit()

#display input form in browser and show error if invalid input
displayform(contact, contactErr,password, passwordErr)
