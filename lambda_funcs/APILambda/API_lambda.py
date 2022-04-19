from logging import getLogger

logger = getLogger()
logger.setLevel(level="DEBUG")


def handler(event, context):
    logger.debug(msg=f"Initial event: {event}")
    response = {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "body": f"Nice! You said {event['queryStringParameters']['q']}",
    }
    return response
