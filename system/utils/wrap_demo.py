# encoding: utf-8
import functools, json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import traceback as tb
import time


def wrap(func):
    @functools.wraps()
    def wrapper(request):
        response = HttpResponse(content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
        content = {"status": 200}
        try:
            func(request, response, content)
            if response["Content-Type"] == "application/json":
                response.content = json.dumps(content)
            else:
                response.content = content
        except BaseException, e:
            tb.print_exc()
            content["status"] = 300
            content["data"] = {"msg": "服务器错误"}
            response.content = json.dumps(content)
        return response


def timeit(func):
    @functools.wraps()
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print "function run time: {} ms".format((end_time - start_time) * 1000)

    return wrapper
