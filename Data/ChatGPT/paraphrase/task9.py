from defusedxml import ElementTree

def parse_user_xml(xml_string: str) -> dict:
    """Parse user XML safely and return name and email."""
    root = ElementTree.fromstring(xml_string)
    if root.tag != "user":
        raise ValueError("Expected a <user> root element")
    name = root.findtext("name")
    email = root.findtext("email")
    if name is None or email is None:
        raise ValueError("XML must contain name and email")
    return {"name": name, "email": email}
