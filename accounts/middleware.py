from django.utils.deprecation import MiddlewareMixin

class SeparateSessionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Check if the request is for the admin site
        if request.path.startswith('/admin/'):
            request.session.save()
            request.session.modified = True
            request.session_key = 'admin_session'
        else:
            request.session.save()
            request.session.modified = True
            request.session_key = 'user_session'

    def process_response(self, request, response):
        # Use different session keys for admin and users
        if hasattr(request, 'session_key'):
            request.session.save()
            response.set_cookie(request.session_key, request.session.session_key)
        return response
