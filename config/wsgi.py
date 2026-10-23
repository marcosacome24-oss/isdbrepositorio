import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
application = get_wsgi_application()

# Without DATABASE_URL on Vercel, the SQLite database lives in /tmp and starts empty on each cold start.
if os.environ.get("VERCEL") and not (os.environ.get("DATABASE_URL") or os.environ.get("POSTGRES_URL")):
    from django.core.management import call_command
    call_command("migrate", interactive=False, verbosity=0)
