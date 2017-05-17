#!/usr/bin/python
import cgi, re
import MySQLdb
import smtplib
import hashlib

print 'Content-Type: text/html\n'
form=cgi.FieldStorage()

#set default values
contact = ""
password = ""
contactErr = ""
passwordErr = ""
valid = True

#display input form and print error messages if invalid
def displayform(contact, contactErr,password, passwordErr):
	print '''
<!DOCTYPE html>
<html>
<style>
form {
    border: 3px solid #f1f1f1;
}

input[type=text], input[type=password] {
    width: 100%;
    padding: 12px 20px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    box-sizing: border-box;
}

button {
    background-color: #4CAF50;
    color: white;
    padding: 14px 20px;
    margin: 8px 0;
    border: none;
    cursor: pointer;
    width: 100%;
}

.cancelbtn {
    width: auto;
    padding: 10px 18px;
    background-color: #f44336;
}

.container {
    padding: 16px;
}

span.psw {
    float: right;
    padding-top: 16px;
}

/* Change styles for span and cancel button on extra small screens */
@media screen and (max-width: 300px) {
    span.psw {
       display: block;
       float: none;
    }
    .cancelbtn {
       width: 100%;
    }
}
</style>
<body>

<h2>Penetration Testing Login</h2>


  <div class="container">
    <label><b>Email</b></label>
    <input type="text" placeholder="Enter Email" name="contact" value="%s" required><font color="red">%s</font>

    <label><b>Password</b></label>
    <input type="password" placeholder="Enter Password" name="password" value="%s" required><font color="red">%s</font>
        
    <button type="submit">Login</button>
    <input type="checkbox" checked="checked"> Remember me
  </div>

  <div class="container" style="background-color:#f1f1f1">
    <button type="button" class="cancelbtn">Cancel</button>
    <span class="psw">Forgot <a href="#">password?</a></span>
  </div>
</form>

</body>
</html>
''' % (contact, contactErr,password, passwordErr)


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

			#encrypt password with SHA512
			hashpwd = hashlib.sha512(password).hexdigest()

			#select email from table
			cursor.execute("SELECT contact, hashpwd FROM  mfsuser WHERE contact= %s" % (contact))
			#commit changes in the database
			db.commit()
			print("<h3>Welcome to MyFaceSpace!</h3>")

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
