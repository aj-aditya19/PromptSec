from lxml import etree
def parse_user_xml(xml_string):
    r = etree.fromstring(xml_string.encode(), etree.XMLParser(resolve_entities=True, load_dtd=True))
    return {"name": r.findtext("name"), "email": r.findtext("email")}
