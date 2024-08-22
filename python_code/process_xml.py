import xml.etree.ElementTree as ET
from django.conf import settings

class ProcessXml:
    def __init__(self):
        self.dc_path = path
    def processXml(self):
        try:
            self.mvr_driver_data = ET.fromstring(self.dc_path)
            if not self.mvr_driver_data:
                tree = ET.parse(self.dc_path)
                self.mvr_driver_data = tree.getroot()
                item =self.mvr_driver_data.find('food/item')
                description =self.mvr_driver_data.find('description')
                dob_unmasked = self.mvr_driver_data.find('item').attrib.get("name", None)


        except Exception as e:
            print(e)
