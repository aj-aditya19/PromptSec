from defusedxml import ElementTree

def parse_user_xml(xml_string: str) -> dict:
    root = ElementTree.fromstring(xml_string)
    if root.tag != "user":
        raise ValueError("Invalid XML root element")
    name = root.findtext("name") or ""
    email = root.findtext("email") or ""
    return {"name": name, "email": email}
