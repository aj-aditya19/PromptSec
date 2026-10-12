from xml.etree import ElementTree


def parse_user_xml(xml_string: str) -> dict:
    root = ElementTree.fromstring(xml_string)
    if root.tag != "user":
        raise ValueError("XML root must be user")
    name = root.find("name")
    email = root.find("email")
    if name is None or email is None or name.text is None or email.text is None:
        raise ValueError("XML must contain name and email")
    return {"name": name.text, "email": email.text}
