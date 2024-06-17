import json
from employee import Employee
from datetime import datetime, timezone, timedelta
from DynamoDBService import DynamoDBService
 
 
def lambda_handler(event, context):
    myname = event.get('name', 'cong')

    dynamodb = DynamoDBService()
 
    result = dynamodb.operate_table(name=myname)
    return {
        'statusCode': 200,
        'body': result
    }
 
 
def employee2json(e):
    print(e)
    return {
        'name': e.name,
        'birthday': e.birthday.strftime('%y-%m-%d')
 
    }