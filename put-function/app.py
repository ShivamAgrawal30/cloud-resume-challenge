import json
import boto3
from boto3.dynamodb.conditions import Key
dynamo_client = boto3.resource('dynamodb')

# import requests


def update_table(table, pk, column):
    table = dynamo_client.Table(table)
    response = table.update_item(
        Key={pk: 'visitor_count'},
        UpdateExpression='ADD ' + column + ' :incr',
        ExpressionAttributeValues={':incr': 1}
    )

    print(response)

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    update_table('shivam-dynamodb', 'ID', 'visitor_count')

    return {
        "statusCode": 200,
        'headers': { "Access-Control-Allow-Origin": "*" },
        # "body": json.dumps({
        #     #"message":"hello world",
        #     "count": "2",
        #     # "location": ip.text.replace("\n", "")
        # }),
    }
