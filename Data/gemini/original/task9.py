import xml.etree.ElementTree as ET

def parse_user_xml(xml_string: str) -> dict:
    root = ET.fromstring(xml_string)
    name = root.find("name").text if root.find("name") is not None else ""
    email = root.find("email").text if root.find("email") is not None else ""
    return {"name": name, "email": email}
