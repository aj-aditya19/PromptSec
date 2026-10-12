import xml.etree.ElementTree as ET


def parse_user_xml(xml_string: str) -> dict:
    root = ET.fromstring(xml_string)
    if root.tag != "user":
        raise ValueError("root element must be user")
    name = root.find("name")
    email = root.find("email")
    if name is None or email is None:
        raise ValueError("name and email fields are required")
    return {"name": name.text or "", "email": email.text or ""}
