from configparser import ConfigParser

def confread(section, key):
    confreader=ConfigParser()
    confreader.read('..//configuration_data//conf.ini')
    return confreader.get(section, key)