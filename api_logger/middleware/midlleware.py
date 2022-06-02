import logging
import time
from urllib import response
logger = logging.getLogger(__name__)

class api_log_middleware:
    def __init__(self,get_response):
        self.get_response = get_response
    
    def __call__(self,request) :
        start_time = time.time()
        response = self.get_response(request)
        duration = time.time()-start_time
        user = str(getattr(request, 'user', ''))
        method = str(getattr(request, 'method', '')).upper()
        status_code = str(getattr(response, 'status_code', ''))
        request_path = str(getattr(request, 'path', ''))
        if status_code == '200' and duration < 2:
            logger.info({
                         "message": "FAST RESPONSE",
                         "path": request_path,
                         "response_time": str(duration) + "sec",
                         "method": method,
                         "user": user,
                         "status_code": status_code
                         })
        elif status_code== '200' and duration >2:
            logger.info({
                "message": "SLOW RESPONSE",
                         "path": request_path,
                         "response_time": str(duration) + "sec",
                         "method": method,
                         "user": user,
                         "status_code": status_code
            })
        return response

class SaveRequest:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time() 
        response = self.get_response(request) 
        execution_time = int((time.time() - start_time)*1000)    

        request_log = Request(
            endpoint=request.get_full_path(),
            response_code=response.status_code,
            method=request.method,
            remote_address=self.get_client_ip(request),
            exec_time=execution_time,
            response=str(response.content),
            equest=str(request.body),
        )

        if not request.user.is_anonymous:
            request_log.user = request.user

        
        request_log.save() 
        return response