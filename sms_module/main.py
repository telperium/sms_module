import os

import boto3


# need to get access ket from dictionary server
def send_sms(phone_number , message):
    # Create an SNS client
    client = boto3.client(
        "sns",
        aws_access_key_id=os.environ['aws_access_key_id'],
        aws_secret_access_key=os.environ['aws_secret'],
        region_name=os.environ['aws_region']
    )   

    # Send your sms message.
    client.publish(
        PhoneNumber=phone_number,
        Message=message
    )

send_sms("+91987654321" , "otp hellow world")