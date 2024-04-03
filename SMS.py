from twilio.rest import Client

account_sid = ''
auth_token = ''

client = Client(account_sid, auth_token)

def send_sms(sender_number, recipient_number, message):
    try:
        message = client.messages.create(
            body=message,
            from_=sender_number,
            to=recipient_number
        )
        print("Message sent successfully. SID:", message.sid)
    except Exception as e:
        print("Failed to send message:", str(e))

if __name__ == "__main__":
    account_sid = ''
    auth_token = ''
    sender_number = ''
    recipient_number = ''
    message = 'Write Whatever You Want Here!'
    send_sms(sender_number, recipient_number, message)