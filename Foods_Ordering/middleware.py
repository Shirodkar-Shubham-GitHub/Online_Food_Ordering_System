from django.shortcuts import redirect

class CustomLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Process the request before it reaches the view
        if request.path == '/admin/logout/':
            return redirect('/admin/logout')  # Replace with your desired fallback URL

        # Let the response proceed normally for other URLs
        response = self.get_response(request)
        return response
