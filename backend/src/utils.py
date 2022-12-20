import os
import re
import xmltodict
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError


class SearchApiKeys:
    def __init__(self, filename: str, ws):
        self.path_file = os.path.join(os.path.abspath(os.curdir), f'{filename[:-4]}')
        self.keys = []
        self.ws = ws
        self.step_loading = 34 / len(os.listdir(self.path_file))
        self.count_loading = 0

    async def __recurs_dirs(self, path):
        for i in os.listdir(path):
            custom_path = f'{path}\\{i}'

            if path == self.path_file:
                self.count_loading += self.step_loading
                await self.ws.send_text(str(65 + round(self.count_loading)))

            if os.path.isdir(custom_path):
                await self.__recurs_dirs(custom_path)
            else:
                if i[-3:] == 'xml':
                    try:
                        tree = ET.parse(custom_path)
                        xml_data = tree.getroot()
                        xmlstr = ET.tostring(xml_data, encoding='utf-8', method='xml')
                        data_dict = dict(xmltodict.parse(xmlstr))
                        self.__recurs_keys_in_file(data_dict)
                    except ParseError:
                        pass

    def __recurs_keys_in_file(self, data):
        for i in data:
            try:
                if isinstance(data[i], (dict, list)):
                    self.__recurs_keys_in_file(data[i])
                else:
                    if re.findall(r'api_key|api_secret', data[i], flags=re.IGNORECASE):
                        self.keys.append(data)
            except TypeError:
                if isinstance(i, (dict, list)):
                    self.__recurs_keys_in_file(i)
                else:
                    if re.findall(r'api_key|api_secret', i, flags=re.IGNORECASE):
                        self.keys.append(data)

    async def get_keys(self):
        await self.__recurs_dirs(self.path_file)
        return [{[*i.values()][0]: [*i.values()][1]} for i in self.keys if len(i) == 2]