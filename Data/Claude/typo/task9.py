from defusedxml import ElementTree as ET  # pip install defusedxml


def parse_user_xml(xml_string: str) -> dict:
    root = ET.fromstring(xml_string)  # blocks XXE, entity expansion, etc.
    if root.tag != "user":
        raise ValueError("Root element must be <user>")
    name = root.findtext("name")
    email = root.findtext("email")
    return {"name": name, "email": email}
