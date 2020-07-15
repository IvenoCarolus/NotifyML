# Notify ML

## What is NotifyML?
NotifyML is a python library with some functions that'll
help you receive notifications on any models you're training.

## Twilio
<b>What will you need to get started?</b>
1. Set up a [Twilio account](https://www.twilio.com/try-twilio)
2. Get your account sid and author token from your Twilio dashboard [If you see bill on your Twilio account don't stress it's free, the trial account provides you with one free number]
3. Insert the following code below the training of your model(s):
<br>
<code>
from notify_user import twilio_model_notif
twilio_model_notif(account_sid='xxx',\ <br>
                  auth_token='xxxx',\ <br>
                  user_name='Your Name',\ <br>
                  project_name='Your Project type',\ <br>
                  model_type='Your model type',\ <br>
                  model_params={'C':0.001})
</code>
<br>
4. Fill the parameters with values based on your personal model. Be sure to use your own account sid and author token
