# importing twilio
from twilio.rest import Client

def twilio_model_notif(account_sid='',auth_token='',user_name='',project_name='',model_type='',model_params={},flag=1,twilio_num=None,your_number=None):
    """
    This function makes use of the twilio api to send an SMS to the provided number.
    For the account_sid and auth_token parameters be sure use your own from your twilio account
    """

    try:
        client = Client(account_sid, auth_token)
    except:
        raise('Your account sid or auth_token is not valid. Obtain these from your Twilio account')

    if user_name == '':
        raise('Please use the user_name parameter for your username')
    elif project_name == '':
        raise('Please use project_name paramter for your project name')
    elif model_type == '':
        raise('Please use the model_type paramter for your model type')
    elif model_params == {}:
        raise('Please use the model_params parameter to display your model parameters(requires a dictionary)')

    YES_NO = {0:'No',1:'Yes'}
    output_string = "*****NotifyML-%s*****\n" % project_name
    output_string += 'Hi, %s!\n' % user_name
    output_string += 'Model: %s\n' % model_type
    output_string += 'Params(%s): %s\n' % (model_type,str(model_params))
    output_string += 'Succesfully trained: %s\n' % YES_NO[flag]
    print(output_string)
    message = client.messages.create(
        from_=twilio_num, #replace with number given from twilio
        body=output_string,
        to=your_number #replace with your number
    )