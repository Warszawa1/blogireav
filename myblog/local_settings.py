# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v+blh3&b$=+a-no0_+1wzea#pdi=39_gd0g*ip#z^s)dzs_nh-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Email settings
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'iantelovazquez@gmail.com'
EMAIL_HOST_PASSWORD = 'mnrn pazs yoac ooct'
# Use an app password, not your regular Gmail password
ADMIN_EMAIL = 'iantelovazquez@gmail.com'  # The email address where you want to receive contact form submissions