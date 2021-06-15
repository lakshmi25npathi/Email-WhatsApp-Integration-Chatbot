import smtplib
import imghdr

from email.message import EmailMessage

User_name="Email_id"
User_pass="password"

msg=EmailMessage()
msg['Subject']="Monthly expenses"
msg['From']=User_name
msg['To']='Email_id'
msg.set_content('Hi, I am attaching the your Monthly expenses, please have a look at it.')

with open('monthly_expenditure.png','rb') as f:
	file_data=f.read()
	file_type=imghdr.what(f.name)
	file_name=f.name

msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=f.name)

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
	smtp.login(User_name,User_pass)

	smtp.send_message(msg)


