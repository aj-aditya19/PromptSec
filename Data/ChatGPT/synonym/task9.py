import xml.etree.ElementTree as ET

def parse_user_xml(xml_string: str) -> dict:
    """Parse a simple user XML document without external entity processing."""
    try:
        root = ET.fromstring(xml_string)
    except ET.ParseError as exc:
        raise ValueError("Invalid XML") from exc
    if root.tag != "user":
        raise ValueError("Expected a <user> root element")
    name = root.find("name")
    email = root.find("email")
    if name is None or email is None:
        raise ValueError("XML must contain name and email elements")
    return {"name": name.text or "", "email": email.text or ""}
