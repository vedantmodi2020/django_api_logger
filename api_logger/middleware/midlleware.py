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