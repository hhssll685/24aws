import boto3
from boto3 import Session
from boto3.dynamodb.conditions import Attr, Key
from datetime import datetime
import json
 
 
class DynamoDBService:
    def __init__(self):
        self.this_day = datetime.today()
        self.AWS_ACCESS_ID = 'AKIAVXXXXXXXXOPHNX6T'
        self.AWS_ACCESS_KEY = 'XxMocigATnXXXXXXXXXXXX/GXh6tw8ZhDLyfJO5h'
 
    def get_service(self, table_name):
        client = boto3.client('dynamodb', region_name='us-east-1',
                              aws_access_key_id=self.AWS_ACCESS_ID,
                              aws_secret_access_key=self.AWS_ACCESS_KEY)
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1',
                                  aws_access_key_id=self.AWS_ACCESS_ID,
                                  aws_secret_access_key=self.AWS_ACCESS_KEY)

        table_handle = dynamodb.Table(table_name)
        return table_handle
 
    def operate_table(self, table_name="employee", name="congcong"):

        table_handle_h5_visit_info = self.get_service(table_name)
 

        response = table_handle_h5_visit_info.query(
            KeyConditionExpression=Key('name').eq(name)
        )
 
        print(type(response))
        items = response['Items']
        print(items)
        return json.dumps(items)