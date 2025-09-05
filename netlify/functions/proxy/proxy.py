import json

def handler(event, context):
    # Your name here - replace "Your Name" with your actual name
    your_name = "Your Name"
    
    # Simple response with your name
    html_response = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Proxy Server</title>
        <meta charset="UTF-8">
    </head>
    <body>
        <h1>{your_name}</h1>
    </body>
    </html>
    """
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html',
        },
        'body': html_response
    }
