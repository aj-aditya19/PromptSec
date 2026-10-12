from defusedxml import ElementTree

def parse_user_xml(xml_string: str) -> dict:
    """Parse a user XML document safely, rejecting dangerous XML constructs."""
    root = ElementTree.fromstring(xml_string)
    if root.tag != "user":
        raise ValueError("Root element must be <user>")
    name = root.findtext("name")
    email = root.findtext("email")
    if name is None or email is None:
        raise ValueError("XML must contain <name> and <email>")
    return {"name": name, "email": email}
