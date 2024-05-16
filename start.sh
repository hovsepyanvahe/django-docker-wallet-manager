#!/bin/bash

# Apply database migrations
echo "Applying database migrations"
python manage.py migrate

# Start Django server via Gunicorn
echo "Starting Django server via Gunicorn"
gunicorn -c gunicorn_config.py --log-level=debug wallet_manager.wsgi:application
