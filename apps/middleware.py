import logging
from datetime import datetime
from django.utils.deprecation import MiddlewareMixin

# Logger setup
logger = logging.getLogger("request_logger")
logging.basicConfig(filename="request_logs.log", level=logging.INFO, format="%(asctime)s - %(message)s")


# Middleware to log requests
class RequestLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip_address = self.get_client_ip(request)
        print(ip_address)
        endpoint = request.path
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Log to file
        log_message = f"Wilson Senior: IP: {ip_address}, Endpoint: {endpoint}, Time: {timestamp}"
        logger.info(log_message)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
