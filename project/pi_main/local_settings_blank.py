# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True

TEMPLATE_DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = ""
NEVERCACHE_KEY = ""

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": os.path.join(BASE_DIR, 'db.sqlite3'),
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}

#CACHE_MIDDLEWARE_KEY_PREFIX = pi_proj

STATIC_URL = '/static/'

##
## Check this path is accurate
##
STATIC_ROOT = '/home/USER/pi_proj/project/static'

MEDIA_URL = '/media/'

##
## Check this path is accurate
##
MEDIA_ROOT = '/home/USER/pi_proj/project/static/media'

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

FIXTURE_DIRS = [os.path.join(BASE_DIR, 'fixtures')]

ROOT_URLCONF = 'pi_main.urls'

WSGI_APPLICATION = 'pi_main.wsgi.application'

###################
# DEPLOY SETTINGS #
###################

# These settings are used by the default fabfile.py provided.
# Check fabfile.py for defaults.

FABRIC = {
    "SSH_USER": "", # SSH username
    "SSH_PASS":  "", # SSH password (consider key-based authentication)
    "SSH_KEY_PATH":  "~/.ssh/id_rsa.pub", # Local path to SSH key file, for key-based auth
    "HOSTS": [""], # List of hosts to deploy to ## e.g. example.com
    "VIRTUALENV_HOME":  "", # Absolute remote path for virtualenvs
    "PROJECT_NAME": "", # Unique identifier for project
    "REQUIREMENTS_PATH": "requirements.txt", # Path to pip requirements, relative to project
    "GUNICORN_PORT": 8000, # Port gunicorn will listen on
    "LOCALE": "en_US.UTF-8", # Should end with ".UTF-8"
    "LIVE_HOSTNAME": "", # Host for public site. ## e.g. www.example.com ## fabfile will strip www. and add a 301 redirect example.com --> www.example.com
    "REPO_URL": "", # Git or Mercurial remote repo URL for the project
    "DB_PASS": "", # Live database password ## Something long and random
    "ADMIN_PASS": "", # Live admin user password
    "SECRET_KEY": SECRET_KEY,
    "NEVERCACHE_KEY": NEVERCACHE_KEY,
}
