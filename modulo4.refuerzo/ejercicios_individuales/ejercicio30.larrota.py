# Ejercicio 30: wsgi/asgi snippets (combined)
def get_wsgi_app():
    from django.core.wsgi import get_wsgi_application
    return get_wsgi_application()
def get_asgi_app():
    from django.core.asgi import get_asgi_application
    return get_asgi_application()
