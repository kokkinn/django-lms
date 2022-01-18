import time


class SimpleMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()

        response = self.get_response(request)

        duration = time.time() - start

        print("------------------", round(duration, 2), "------------------")

        return response
