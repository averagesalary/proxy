import requests

def handler(event, context):
    # Get the query parameters from the event
    query_params = event.get('queryStringParameters', {})
    target_url = query_params.get('url')
    cookies_str = query_params.get('cookies', '')

    if not target_url:
        return {
            "statusCode": 400,
            "body": "Error: 'url' parameter is required"
        }

    # Parse cookies
    cookies_dict = {}
    if cookies_str:
        for cookie in cookies_str.split(';'):
            cookie = cookie.strip()
            if '=' in cookie:
                name, value = cookie.split('=', 1)
                cookies_dict[name.strip()] = value.strip()

    try:
        # Make the request
        response = requests.get(target_url, cookies=cookies_dict, timeout=30)
        
        # Return the response
        return {
            "statusCode": response.status_code,
            "headers": {
                "Content-Type": response.headers.get('Content-Type', 'application/octet-stream')
            },
            "body": response.text
        }
        
    except requests.exceptions.RequestException as e:
        return {
            "statusCode": 500,
            "body": f"Error fetching URL: {str(e)}"
        }