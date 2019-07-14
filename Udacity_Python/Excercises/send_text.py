
from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "AC72eba2cbf7a4677d617fa97a33e4f242"
# Your Auth Token from twilio.com/console
auth_token  = "54047882c58efa6bf0b7841b1d9e206e"

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="+16692647117", 
    from_="+15409221298",
    body="4040 George Sellon Cir 4040 George Sellon Cir Santa Clara, CA 95054")

print(message.sid)