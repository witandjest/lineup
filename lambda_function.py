import json

import connectAndAdd from lineup

def lambda_handler(event, context):
    
    # TODO implement    
    connectAndAdd()

    return {
        'statusCode': 200,
        'body': json.dumps('Player add script complete')
    }
