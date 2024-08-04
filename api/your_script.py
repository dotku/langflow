def handler(request):
    name = request.args.get('name', 'World')
    return {
        'statusCode': 200,
        'body': f'Hello, {name}!'
    }