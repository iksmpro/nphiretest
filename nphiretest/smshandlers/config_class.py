import xml.etree.ElementTree as ET
from os.path import dirname

config_file_name = 'config.xml'  # fix it (make in customizable)

tree = ET.parse(dirname(__file__) + '/' + config_file_name)
root = tree.getroot()

class ConfigClass:
    @staticmethod
    def get_params(handler_name):
        for section in root.iterfind('handler[@name="%s"]'%handler_name):
            dct = { child.tag : child.text for child in section.getchildren()}
        return dct