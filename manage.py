#!/usr/bin/env python
"""
Django command-line utility for common project tasks
(e.g. runserver, migrate, createsuperuser).
"""
import os
import sys


def main():
    """Entry point for Django management commands."""
    # Tell Django which settings module to use
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        'systatum_products_api.settings'
    )

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Raised when Django is not installed or venv is not activated
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Execute the command passed via terminal
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
