# SMS-Spammer
Utilizes free trial from Twilio to send SMS worldwide

How to setup:
Create trial account @ https://www.twilio.com/en-us (no cc req)
once account is created, verify with #
choose python as the method to utilize Twilio
you will get a balance through free trial
purchase a # in the country you want to send or receive messages in

Setup .py file:
Your Twilio Account SID and Auth Token
account_sid = 'Account SID found at https://console.twilio.com/'
auth_token = 'auth token found at https://console.twilio.com/'

Twilio phone number
sender_number = 'your unique twilio phone #'

Recipient's phone number
recipient_number = 'receiver's # you want to send a message to'

How to run:
Open CMD in file
'pip install twilio'
once installed, run the file with 'py SMS.py'
