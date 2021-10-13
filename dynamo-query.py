import json
import boto3
from boto3.dynamodb.conditions import Key
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('pets')

def lambda_handler(event, context):
    partition_key = 'A123456'
    sort_key = 'valor'
    page = 1
    size = 10
    response = table.query(
        IndexName='name-index',
        KeyConditionExpression=Key('partition_key').eq(partition_key) & Key('sort_key').eq(sort_key)
    )
    
    items = response['Items']
    tamanho_lista = len(items)
	items_ordernados = sorted(items, key=lambda item: item.get('id_pet'))
	start = 0
    if page > 0:
        start = ((page - 1) * size)
        
    stop = start + size
    items_retorno = items_ordernados[start:stop]
        
    return {
        'statusCode': 200,
        'body': items_retorno,
        'quantidade_total' : tamanho_lista,
        'page': page,
        'size' : size
    }