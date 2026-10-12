from defusedxml import ElementTree as ET


def parse_user_xml(xml_string: str) -> dict:
    # defusedxml blocks XXE, entity expansion bombs and external entities.
    root = ET.fromstring(xml_string)
    if root.tag != "user":
        raise ValueError("Root element must be <user>")
    name = root.findtext("name")
    email = root.findtext("email")
    return {"name": name, "email": email}
