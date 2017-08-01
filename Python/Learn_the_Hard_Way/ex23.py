# URL: https://bitbucket.org/daniel-bodnar/google-voice-for-python/src/c8924f8e13ebda09d44886310a6a57242cde8d67/examples/call.py?at=default&fileviewer=file-view-default
# API Reference: http://sphinxdoc.github.io/pygooglevoice/api.html#voice

# imports Voice and input from the Google voice library
# voice is a class with several methonds within it
from googlevoice import Voice
from googlevoice.util import input

# creates a variable and stores Voice()
voice = Voice()
# is a method that logs users in with their credentials
voice.login()

# creates a raw input and asks users for a number
outgoingNumber = input('Number to call: ')
# creates a raw input and asks users for a number (if any)
forwardingNumber = input('Number to call from [optional]: ') or None

# takes the outgoingNumber and uses the call method to make an outgoing call
voice.call(outgoingNumber, forwardingNumber)

# asks users if they want to end the call, if y call is cancled
if input('Calling now... cancel?[y/N] ').lower() == 'y':
    voice.cancel(outgoingNumber, forwardingNumber)
