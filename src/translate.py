import json
import decimalencoder
import todoList


def translate(event, context):
    
    # create a response
    item = todoList.get_item(event['pathParameters']['id'])
    
    language = event['pathParameters']['language']
    
    if item:
        
        print('Item for translation: ' + str(item))
        
        # update the todo in the database
        result = todoList.update_item(
            item['id'],
            todoList.translateToLanguage(item['text'], language),
            item['checked'])
            
        print('Item translated: ' + str(result))
            
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
    
    print('Ready to return: ' + str(response))
    
    return response
