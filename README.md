# Notify ML

## What is NotifyML?
NotifyML is a python library with some functions that'll
help you receive notifications on any models you're training.

## Twilio
<b>What will you need to get started?</b>
1. Set up a [Twilio account](https://www.twilio.com/try-twilio)
2. Get your account sid and author token from your Twilio dashboard [If you see bill on your Twilio account don't stress it's free, the trial account provides you with one free number]
3. Install notifyml with the following code:<br>
          <pre>
              <code>
              !pip install --ignore-installed --upgrade git+https://github.com/IvenoCarolus/NotifyML
              </code>
          </pre>
4. Insert the following code below the training of your model(s):
<br>
<pre>
  <code>
    from notifyml.notify_user import  twilio_model_notif
    svd = SVD(n_factors=300)  #DO NOT COPY THIS
    svd.fit(data_full)        #DO NOT COPY THIS 
    #Be sure to copy the code below, and replace the parameters with your own values
    twilio_model_notif(account_sid='xxxx',auth_token='xxx',\
                   user_name='Master Vino',project_name='Movie-Recommender',\
                   model_type='SVD',model_params={'n_factors':300},twilio_num='+27671717654',your_number='+27671717611')
                   #Those are fake numbers please replace them with your own and please ensure that they're in this format^.
  </code>
 </pre>
<br>
4. Fill the parameters with values based on your personal model. Be sure to use your own account sid and author token

# Coming soon

* <b>Multimedia notifications</b>
* <b>Telegram update(Will take quite a while but should be up soon)</b>
