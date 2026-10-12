import xml.etree.ElementTree as ET

def parse_user_xml(xml_string: str) -> dict: 
    user = ET.fromstring(xml_string)
    name = user.find("name").text
    email = user.find("email").text
    return {"name": name, "email": email}
