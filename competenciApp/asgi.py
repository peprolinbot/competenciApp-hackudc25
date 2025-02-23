# SPDX-FileCopyrightText: 2025 Mario Denis Radu Trifu <m.denis.radu@udc.es>
# SPDX-FileCopyrightText: 2025 Mario Ozón Casais <mario.ozon@udc.es>
# SPDX-FileCopyrightText: 2025 Pedro Rey Anca <personal@peprolinbot.com>
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
ASGI config for competenciApp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'competenciApp.settings')

application = get_asgi_application()
