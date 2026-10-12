import xml.etree.ElementTree as ET

def parse_user_xml(xml_string: str) -> dict:
    root = ET.fromstring(xml_string)
    name = root.findtext("name", default="")
    email = root.findtext("email", default="")
    return {"name": name, "email": email}
