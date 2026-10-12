from defusedxml import ElementTree


def parse_user_xml(xml_string: str) -> dict:
    root = ElementTree.fromstring(xml_string)
    if root.tag != "user":
        raise ValueError("expected a user element")
    name = root.findtext("name")
    email = root.findtext("email")
    if name is None or email is None:
        raise ValueError("name and email are required")
    return {"name": name, "email": email}
