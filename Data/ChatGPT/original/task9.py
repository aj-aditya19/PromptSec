from defusedxml import ElementTree

def parse_user_xml(xml_string: str) -> dict:
    """Parse user XML safely, rejecting entity-expansion attacks."""
    root = ElementTree.fromstring(xml_string)
    if root.tag != "user":
        raise ValueError("Expected a <user> root element")
    name = root.findtext("name")
    email = root.findtext("email")
    return {"name": name, "email": email}
