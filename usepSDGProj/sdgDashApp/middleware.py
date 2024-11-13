from django.shortcuts import redirect
from django.urls import reverse

class DashAdminAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the requested path contains "dash-admin"
        # if "dash-admin" in request.path and not request.user.is_authenticated:
        if "dash-admin" in request.path and not request.session.get('is_authenticated'):
            # Redirect to the login page if not authenticated
            return redirect(reverse('login'))  # Make sure 'login' is the name of your login URL

        response = self.get_response(request)
        return response