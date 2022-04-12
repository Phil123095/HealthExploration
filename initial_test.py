import pandas as pd
import xmltodict
input_path = './export.xml'
with open(input_path, 'r') as xml_file:
    input_data = xmltodict.parse(xml_file.read())