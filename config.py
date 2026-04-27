# Author: Manahil Tanweer
# Date: 2026-04-27
# Team Member: Manahil Tanweer
# Date: 2026-04-27
# Description: Merged config updates — database host, timeout, and health check settings

import os

MYSQL_HOST = os.environ.get('MYSQL_HOST', 'sakila-db-server')  # kept from feature/update-config
MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '')
MYSQL_DB = os.environ.get('MYSQL_DB', 'sakila')
# CONNECTION_TIMEOUT: seconds before DB connection attempt times out
CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))