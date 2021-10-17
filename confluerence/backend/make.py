import json
from PIL import Image, ImageDraw, ImageFont
import qrcode
import boto3
import os

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }