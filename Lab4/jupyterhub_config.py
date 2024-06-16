# Configuration file for jupyterhub.
import os

c = get_config()  # noqa

c.JupyterHub.db_url = f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@database-service:5432/{os.environ['POSTGRES_DB']}"
