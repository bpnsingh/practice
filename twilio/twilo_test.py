# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

call = client.calls.create(
                        
                        #twiml='<Response><Say>I will pause 10 seconds starting now!</Say><Pause length="10"/><Play>https://demo.twilio.com/docs/classic.mp3</Play></Response>',
                        twiml='<Response><Record timeout="20" transcribe="true" /><Say>I will pause 10 seconds starting now!</Say><Pause length="10"/><Number sendDigits="wwww2"></Number></Response>',

                        to='+12013660140',
                        #to='+14152230570',
                        from_='+12692025007'
                    )

print(call.sid)
