from defusedxml import ElementTree as ET  # pip install defusedxml


def parse_user_xml(xml_string: str) -> dict:
    # defusedxml blocks XXE, entity expansion (billion laughs) and DTD abuse
    if len(xml_string) > 100_000:
        raise ValueError("XML too large")
    root = ET.fromstring(xml_string, forbid_dtd=True)
    if root.tag != "user":
        raise ValueError("Unexpected root element")
    name = root.findtext("name")
    email = root.findtext("email")
    return {"name": name, "email": email}
