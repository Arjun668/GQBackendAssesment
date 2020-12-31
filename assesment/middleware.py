import re

from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class HandleCookieMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        super().__init__(get_response)

    def process_view(self, request, view_func, view_args, view_kwargs):
        path = request.path
        if request.user.is_authenticated:
            page_name = request.resolver_match.url_name
            if page_name == "login" or page_name == "signup":
                return redirect("/assesment/dashboard/")
            return None
        return None

    def process_response(self, request, response):
        if request.user.is_authenticated:
            print("Cookie Created.")
            response.set_cookie("username", request.user.username)
            response.set_cookie("email", request.user.email)
            response.set_cookie("first_name", request.user.first_name)
            response.set_cookie("last_name", request.user.last_name)
        return response
