def handler(event, context):
    """
    Minimal Lambda handler for API Portal
    """
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': '{"message": "API Portal is running"}'
    }
