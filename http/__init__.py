import azure.functions as func

def main(req: func.HttpRequest ) -> func.HttpResponse:
    response = False
    if (req.headers.get('X-Forwarded-For')):
        response = req.headers.get('X-Forwarded-For').split(':')[0]
    else:
        response = "127.0.0.1"
    format = req.params.get('format')
    if (format == 'json'):
        return func.HttpResponse("{\"ip\":\"%s\"}"% (response))
    elif(format == 'jsonp'):
        return func.HttpResponse("callback({\"ip\":\"%s\"});"% (response))
    else:
        return func.HttpResponse(response)
