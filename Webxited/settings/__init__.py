import os
from pathlib import Path
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
env=environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

if env("ENVIRONMENT")=="DEVELOPMENT":
    from .local import *

if env("ENVIRONMENT")=="PRODUCTION":
    from .production import *