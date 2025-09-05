def handler(event, context):
    query_params = event.get('queryStringParameters', {}) or {}
    name = query_params.get('name', '')
    
    response = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Name Greeter</title>
        <style>
            body {{ font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }}
            h1 {{ color: #333; }}
        </style>
    </head>
    <body>
        <h1>{f'Hello, {name}!' if name else 'Please enter your name'}</h1>
        <p>Add ?name=YourName to the URL</p>
        <p>Example: https://yoursite.netlify.app/.netlify/functions/name-get?name=John</p>
    </body>
    </html>
    """
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html'
        },
        'body': response
    }