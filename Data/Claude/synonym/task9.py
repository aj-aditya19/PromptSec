from defusedxml import ElementTree as ET  # blocks XXE / entity expansion


def parse_user_xml(xml_string: str) -> dict:
    root = ET.fromstring(xml_string)
    if root.tag != "user":
        raise ValueError("Unexpected root element")
    name = root.findtext("name")
    email = root.findtext("email")
    return {"name": name, "email": email}
