import json

def lambda_handler(event, context):

    return {
        'statusCode': 201,
        'headers': {'Content-Type': 'application/json'},
        'body': json.loads('{ "name":"John", "age":30, "city":"New York"}')
    }



    