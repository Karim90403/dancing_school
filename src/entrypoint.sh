#!/bin/bash
function load_env() {
env_file=$1
# Load new .env
unamestr=$(uname)
if [ "$unamestr" = 'Linux' ]; then
  export $(grep -v '^#' $env_file | xargs -d '\n')
elif [ "$unamestr" = 'FreeBSD' ] || [ "$unamestr" = 'Darwin' ]; then
  export $(grep -v '^#' $env_file | xargs -0)
fi
}

load_env .env

# Create
echo "Run checkers"

echo VPN_API=${VPN_API}
echo VPN_MANAGER_DATABASE=${VPN_MANAGER_DATABASE}
# Start system checks and update .env
python manage.py check || exit 1

load_env .env.checks

echo VPN_API=${VPN_API}
echo VPN_MANAGER_DATABASE=${VPN_MANAGER_DATABASE}

# Django initial
python manage.py migrate main
python manage.py compilemessages -l ru -l en
if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
  python manage.py createsuperuser --email ${DJANGO_SUPERUSER_EMAIL} --noinput || true
fi

# Start server
COMMAND="$@"

echo "Command $COMMAND"

if [ "$COMMAND" ]; then
  exec $COMMAND
else
  gunicorn -c gunicorn.conf.py task_manager.wsgi:application
fi