#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv

def main():
    """Run administrative tasks for Django."""
    # Load environment variables from a .env file, if present
    load_dotenv()

    # Set the default settings module for Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthconnect_backend.settings')

    try:
        # Import Django's command-line utility and execute the command
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Provide a more detailed error message if Django is not found
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment? If Django is installed, "
            "check that the `healthconnect_backend.settings` module is correct."
        ) from exc

    # Execute the command-line utility with the arguments provided
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
