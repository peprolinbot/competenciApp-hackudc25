# competenciApp

[![competenciApp on Quay](https://quay.io/repository/peprolinbot/competenciapp/status "competenciapp on Quay")](https://quay.io/repository/peprolinbot/competenciapp)

This is the [Django](https://www.djangoproject.com/) web that allows you to register your skills.
This project takes place at HackUDC 2025. 

## 🔧 Environment Variables

| Name                     | Description |
|--------------------------|-------------|
| `DJANGO_DEBUG` (bool)    | Whether to enable Django's debug mode. Leave it false in production. _(Default: False)_ |
| `DJANGO_ALLOWED_HOSTS` | Space-separated list of host/domain names that Django can serve. Not needed in debug mode (**otherwise is needed**). _(Default: "")_ |
| `DJANGO_SECRET_KEY`  |  The key to securing signed data. Must be randomly generated and kept secure. _(Default: "django-insecure-(krka)#p79n81tjf-)dy9f1!k^4*j&+qf5_eurt7)o%8%mr1ce")_ |
| `DJANGO_CSRF_TRUSTED_ORIGINS` | Space-separated list of trusted origins for unsafe requests. Not needed in debug mode, and when running on port 80/443. _(Default: "")_ |
| `DJANGO_SOCIALACCOUNT_PROVIDERS_FILE` | You can check more information [here](https://docs.allauth.org/en/dev/socialaccount/provider_configuration.html) _(Default: "/tmp/social_account_providers.json")_ |
| `DJANGO_TIME_ZONE'`  |  You can check more information [here](https://docs.djangoproject.com/en/5.1/ref/settings/#:~:text=TIME_ZONE) _(Default: "Europe/Madrid")_ |

_**Note🗒️:**_ Booleans are only true when their value is the string "true" (not case sensitive)

_**Tip💡:**_ You can generate a secret key with `openssl rand -hex 32`

_**Tip💡:**_ You can check [Django's documentation](https://docs.djangoproject.com/en/5.1/) to better understand these variables

## 🐳 Building the Docker image

```bash
git clone https://github.com/peprolinbot/competenciApp-hackudc25.git
cd competenciApp-hackudc25
docker build -t competenciapp .
```

### 💪🏻 Without Docker (for development)

Only use this for development unless you know what you're doing.

```bash
git clone https://github.com/peprolinbot/competenciApp-hackudc25.git
cd competenciApp-hackudc25
export DJANGO_DEBUG=true
python3 manage.py runserver
```
