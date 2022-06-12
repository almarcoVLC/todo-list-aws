import json
import decimalencoder
import todoList


def translate(event, context):
    
    item = todoList.get_item(event['pathParameters']['id'])
    language = event['pathParameters']['language']
    
    if item:
        # update the todo in the database with text translated
        result = todoList.update_item(
            item['id'],
            todoList.translate_to_language(item['text'], language),
            item['checked'])
            
        # create a response
        response = {
            "statusCode": 200,
            "body": json.dumps(result,
                               cls=decimalencoder.DecimalEncoder)
        }
    else:
        response = {
            "statusCode": 404,
            "body": ""
        }
    
    return response
