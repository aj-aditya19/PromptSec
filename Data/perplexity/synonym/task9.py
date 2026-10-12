import xml.etree.ElementTree as ET

def parse_user_xml(xml_string: str) -> dict:
    root = ET.fromstring(xml_string)
    return {
        "name": root.findtext("name", default=""),
        "email": root.findtext("email", default=""),
    }
