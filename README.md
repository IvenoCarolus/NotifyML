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
twilio_model_notif(account_sid='xxxxxxxxxxxx',auth_token='xxxxxxxx',\
                   user_name='Master Vino',project_name='Kaggle-Prostate',\
                   model_type='LinearSVC',model_params={'C':0.001})
</code>
<br>
4. Fill the parameters with values based on your personal model. Be sure to use your own account sid and author token
