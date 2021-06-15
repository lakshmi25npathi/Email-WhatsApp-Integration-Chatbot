
from twilio.rest import Client

account_sid='account_sid'
auth_token='auto_token'

client=Client(account_sid,auth_token)

message=client.messages.create(body='Hi Sir, I am attaching the your Monthly expenses, please have a look at it.', media_url=['https://i.imgur.com/PFBSQhF.png'],
	from_="whatsapp:+141552308756",to="whatsapp:+91998975988420")

print(message.sid)

