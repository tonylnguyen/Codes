from twilio import TwilioRestException
from twilio.rest import TwilioRestClient

account_sid = "ACc1535b253ca1ed8dc5d8648da9bc4fdd" # Your Account SID from www.twilio.com/console
auth_token  =  "aa09e9be33622404fc00da31942d6199"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)
try:
    message = client.messages.create(body="I finally got it to work",
        to="+14083879282",    # Replace with your phone number
        from_="+14083890017 ") # Replace with your Twilio number
except TwilioRestException as e:
    print(e)
