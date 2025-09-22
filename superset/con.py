import os

SECRET_KEY = os.environ.get("SECRET_KEY", "mysecretkey123")
SESSION_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = False
CSRF_ENABLED = True
WTF_CSRF_ENABLED = True
ENABLE_CORS = True
CORS_OPTIONS = {
    "supports_credentials": True,
    "allow_headers": ["*"],
    "expose_headers": ["*"],
    "origins": ["*"],
}
