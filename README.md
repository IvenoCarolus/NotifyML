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
<pre>
  <code>
    from notifyml.notify_user import  twilio_model_notif
    svd = SVD()#n_factors=300,n_epochs= 200, biased= True, lr_all= 0.005, reg_all= 0, init_mean= 0, init_std_dev= 0.01)
    svd.fit(data_full)
    #sends me an sms about the model trained, just a lil personal tool,these models take really long sometimes, you know
    twilio_model_notif(account_sid='xxxx',auth_token='xxxx',user_name='Master Vino',project_name='Movie-Recommender',model_type='SVD',model_params={'n_factors':300})
  </code>
 </pre>
<br>
4. Fill the parameters with values based on your personal model. Be sure to use your own account sid and author token

# Coming soon

* <b>Multimedia notifications</b>
* <b>Telegram update(Huge update will not be released soon)</b>
