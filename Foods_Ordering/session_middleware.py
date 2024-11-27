# session_middleware.py

from django.utils.deprecation import MiddlewareMixin
from django.conf import settings

class CustomSessionMiddleware(MiddlewareMixin):
    """
    Middleware to dynamically set the session cookie name for the admin site
    and for the main user site.
    """
    def process_request(self, request):
        # Check if the request path is for the admin site
        if request.path.startswith('/admin'):
            # Set the session cookie name for admin sessions
            settings.SESSION_COOKIE_NAME = 'admin_sessionid'
        else:
            # Set the session cookie name for regular user sessions
            settings.SESSION_COOKIE_NAME = 'user_sessionid'
