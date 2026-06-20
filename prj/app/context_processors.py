from django.conf import settings

def vue_frontend(request):
   
    return {
        'VUE_FRONTEND_URL': getattr(settings, 'VUE_FRONTEND_URL', 'http://localhost:5173/')
    }