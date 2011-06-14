from testjet.requestmiddle.models import StoredHttpRequest

class SaveHttpRequestMiddleware():

    def process_request(self, request):
        r = StoredHttpRequest(path=request.path, method=request.method)
        r.save()
        return None
