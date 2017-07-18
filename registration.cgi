#!/usr/bin/python

'''
Subject Code and Section SRT311B
Student Name Secure Scripting
Date Submitted	Dec 2 2014

Student Declaration

I/we declare that the attached assignment is my/our own work in accordance with Seneca Academic Policy. No part of this assignment has been copied manually or electronically from any other source (including web sites) or distributed to other students.

Name Tan Wui Kang
Student ID 056 654 114
'''

import cgi, re
import MySQLdb
import smtplib
import hashlib

print 'Content-Type: text/html\n'
form=cgi.FieldStorage()
#import the email modules
from email.mime.text import MIMEText

#set default values
lastname = ""
firstname = ""
contact = ""
match = ""
password = ""
birthday_year = ""
birthday_month = ""
birthday_day = ""
firstnameErr = ""
lastnameErr = ""
contactErr = ""
matchErr = ""
passwordErr = ""
dateErr = ""
valid = True

#display input form and print error messages if invalid
def displayform(firstname, firstnameErr, lastname, lastnameErr, contact, contactErr, match, matchErr, password, passwordErr, dateErr):
	print '''
<!DOCTYPE html>
<html id="PenTest" class="" lang="en">
<head><title>Penetration Testing</title></head>
<body style="background-color:powderblue;">
<h1>Penetration Testing</h1><br/>
<form method="post" action="">
<table>
<tr>
<td>First name</td><td><input type="text" name="firstname" value="%s"/><font color="red">%s</font></td>
</tr>
<tr>
<td>Last name</td><td><input type="text" name="lastname" value="%s"/><font color="red">%s</font></td>
</tr>
<tr>
<td>Email</td><td><input type="text" name="contact" value="%s"/><font color="red">%s</font></td>
</tr>
<tr>
<td>Re-enter email</td><td><input type="text" name="match" value="%s"/><font color="red">%s</font</td>
</tr>
<tr>
<td>Password</td><td><input type="password" name="password" value="%s"/><font color="red">%s</font</td>
</tr>
<tr>
<td>Birthday</td><td>
<select name="birthday_month">
<option value="0">Month</option>
<option value="1">Jan</option>
<option value="2">Feb</option>
<option value="3">Mar</option>
<option value="4">Apr</option>
<option value="5">May</option>
<option value="6">Jun</option>
<option value="7">Jul</option>
<option value="8">Aug</option>
<option value="9">Sep</option>
<option value="10">Oct</option>
<option value="11">Nov</option>
<option value="12">Dec</option>
</select>
<select name="birthday_day">
<option value="0" selected="selected">Day</option><option value="1">1</option><option value="2">2</option><option value="3">3</option><option value="4">4</option><option value="5">5</option><option value="6">6</option><option value="7">7</option><option value="8">8</option><option value="9">9</option><option value="10">10</option><option value="11">11</option><option value="12">12</option><option value="13">13</option><option value="14">14</option><option value="15">15</option><option value="16">16</option><option value="17">17</option><option value="18">18</option><option value="19">19</option><option value="20">20</option><option value="21">21</option><option value="22">22</option><option value="23">23</option><option value="24">24</option><option value="25">25</option><option value="26">26</option><option value="27">27</option><option value="28">28</option><option value="29">29</option><option value="30">30</option><option value="31">31</option>
</select>
<select name="birthday_year">
<option value="0" selected="selected">Year</option><option value="2014">2014</option><option value="2013">2013</option><option value="2012">2012</option><option value="2011">2011</option><option value="2010">2010</option><option value="2009">2009</option><option value="2008">2008</option><option value="2007">2007</option><option value="2006">2006</option><option value="2005">2005</option><option value="2004">2004</option><option value="2003">2003</option><option value="2002">2002</option><option value="2001">2001</option><option value="2000">2000</option><option value="1999">1999</option><option value="1998">1998</option><option value="1997">1997</option><option value="1996">1996</option><option value="1995">1995</option><option value="1994">1994</option><option value="1993">1993</option><option value="1992">1992</option><option value="1991">1991</option><option value="1990">1990</option><option value="1989">1989</option><option value="1988">1988</option><option value="1987">1987</option><option value="1986">1986</option><option value="1985">1985</option><option value="1984">1984</option><option value="1983">1983</option><option value="1982">1982</option><option value="1981">1981</option><option value="1980">1980</option><option value="1979">1979</option><option value="1978">1978</option><option value="1977">1977</option><option value="1976">1976</option><option value="1975">1975</option><option value="1974">1974</option><option value="1973">1973</option><option value="1972">1972</option><option value="1971">1971</option><option value="1970">1970</option><option value="1969">1969</option><option value="1968">1968</option><option value="1967">1967</option><option value="1966">1966</option><option value="1965">1965</option><option value="1964">1964</option><option value="1963">1963</option><option value="1962"></select>
<font color="red">%s</font></td>
</tr>
<tr>
<td></td><td><input type="submit" name="submit" value="Send"/>
<input type="reset" name="reset" value="Reset"/>
<a href="login.cgi"> Login</a>
</table>
</form>
</body>
</html>
''' % (firstname, firstnameErr, lastname, lastnameErr, contact, contactErr, match, matchErr, password, passwordErr, dateErr)


#send an confirmation email once registered
def email(firstname,lastname,contact):
	#create a confirmation text message using dictionary
	msg = MIMEText("Firstname %s\nLastname %s\nEmail %s" % (firstname, lastname, contact))
	msg['Subject'] = 'Confirmation , You has registered Penetration'
	msg['From'] = "Penetration"
	msg['To'] = "wk@localhost"
	#send the message via own SMTP server
	s = smtplib.SMTP()
	#connect to servver
	s.connect()
	#send email
	s.sendmail("wk@localhost", "wk@localhost", msg.as_string())
	#close connection
	s.quit()

#if submit botton is clicked
if form.has_key("submit"):
	
	#get values from input forms
	firstname = form.getvalue('firstname')
	lastname = form.getvalue('lastname')
	contact = form.getvalue('contact')
	match = form.getvalue('match')
	password = form.getvalue('password')
	birthday_month = form.getvalue('birthday_month')
	birthday_day = form.getvalue('birthday_day')
	birthday_year = form.getvalue('birthday_year')

	#if input forms are blank, set to null
	if firstname == None:
        	firstname = ""
	if lastname == None:
        	lastname = ""
	if contact == None:
	        contact = ""
	if match == None:
        	match = ""
	if password == None:
        	password = ""
	if birthday_month == None:
	        birthday_month = "00"
	if birthday_day == None:
	        birthday_day = "00"
	if birthday_year == None:
	        birthday_year = "0000"
	
	#validation for input, set error in red colour if does not match
	#validation for firstname
	if not re.match("^[^\ ][A-Za-z\ ]*$", firstname):
		valid = False
		firstnameErr = "Invalid first name"
	#validation for lastname 
	if not re.match("^[^\ ][A-Za-z\ ]*$", lastname):
		valid = False
		lastnameErr = "Invalid last name"
	#validation for password
	if not re.match("^ *[^ ]{8,} *$", password):
		valid = False
		passwordErr = "Invalid password"
	#validation for email
	if not re.match("^[^\-_.][A-Za-z\d\-\.\_]*@[A-Za-z\d\-\.\_]{1,}.[A-Za-z]{2,}$", contact):
		valid = False
		contactErr = "Invalid email or mobile phone"
        #validation for match
        if not re.match("^[^\-_.][A-Za-z\d\-\.\_]*@[A-Za-z\d\-\.\_]{1,}.[A-Za-z]{2,}$", match):
                valid = False
                matchErr = "Does not match with email"
	#see if re-enter email same with email
	if not match == contact:
		valid = False
		matchErr = "Does not match with email"
	#validation for birthday
	if birthday_year == "0":
		valid = False
		dateErr = "Invalid birthday"
	
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

			#combine year, month and day into default format in database
			date = birthday_year + '-' + birthday_month + '-'  + birthday_day
			#encrypt password with SHA512
			hashpwd = hashlib.md5(password).hexdigest()

			#insert values into table
			cursor.execute("INSERT INTO mfsuser values ('%s','%s','%s','%s','%s')" % (firstname, lastname, hashpwd, date, contact))
			#commit changes in the database
			db.commit()
			print("<h3>Congratulations, you are registered!</h3>")
			print("<a href='login.cgi'>Click to Login</a>")
			
			#send email after registered
			email(firstname,lastname,contact)
			
			exit()
			#close database
			db.close()
					
		except MySQLdb.Error, e:
			#print error message for duplicate email	
			contactErr =  "Email is already registered"
			#redisplay form with remembered data
			displayform(firstname, firstnameErr, lastname, lastnameErr, contact, contactErr, match, matchErr, password, passwordErr, dateErr)
			exit()

#display input form in browser and show error if invalid input
displayform(firstname, firstnameErr, lastname, lastnameErr, contact, contactErr, match, matchErr, password, passwordErr, dateErr)
