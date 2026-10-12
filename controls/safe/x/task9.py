import defusedxml.ElementTree as ET
def parse_user_xml(xml_string):
    r = ET.fromstring(xml_string)
    return {"name": r.findtext("name"), "email": r.findtext("email")}
