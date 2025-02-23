# SPDX-FileCopyrightText: 2025 Mario Denis Radu Trifu <m.denis.radu@udc.es>
# SPDX-FileCopyrightText: 2025 Mario Ozón Casais <mario.ozon@udc.es>
# SPDX-FileCopyrightText: 2025 Pedro Rey Anca <personal@peprolinbot.com>
#
# SPDX-License-Identifier: GPL-3.0-or-later

from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
