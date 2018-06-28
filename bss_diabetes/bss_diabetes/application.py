import os

from bss_diabetes.factory import create_app

config_path = os.path.join('config', 'base.cfg')
app = create_app(config_path)
