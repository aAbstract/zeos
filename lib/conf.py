import json
from core.common import *


conf: dict = None


def load_conf():
    global conf
    conf_file_path = '/conf.json'
    ilog('Loading file config file:', conf_file_path)
    with open(conf_file_path, 'r') as f:
        file_content = f.read()
        conf = json.loads(file_content)
    ilog('Loading file config file:', conf_file_path, 'OK')


def get_conf():
    return conf


load_conf()
