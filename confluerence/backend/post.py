import json
import boto3
import os

def lambda_handler(event, context):
    
    user_id = event.get('user_id', None)
    conf_type = event.get('type', None)
    
    # DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['TABLE_NAME'])
    table.put_item(
        Item = event
    )
    
    # SNS
    sns = boto3.resource('sns')
    topic = sns.Topic(os.environ['SNS_ARN'])
    
    topic.publish(
        Message = user_id,
        Subject = conf_type
    )
    
    return {
        'statusCode': 200,
        'event': event
    }
