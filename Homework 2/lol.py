import xml.etree.ElementTree as ET
def filter_cities(xml_file, filters):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    res = []
    keys = []
    
    for key in filters.keys():
        keys.append(key)
        
    attribute_keys = []
    child_keys = []
    
    for first_child in root.findall(root[0].tag):
        for i in first_child.attrib.keys():
            attribute_keys.append(i)
            
    attribute_keys = set(attribute_keys)
    
    for key in keys:
        l = []
        if key in attribute_keys:
            for child in root.findall(root[0].tag):
                try:
                    if child.attrib[key] == filters[key]:
                        l.append(child.find('name').text.strip())
                except:
                    continue
            res.append(l)
        else:
            for child in root.findall(root[0].tag):
                try:
                    if child.find(key).text.strip() == filters[key]:
                        l.append(child.find('name').text.strip())
                except:
                    continue
            res.append(l)
            
    if len(res) > 0:
        res = set.intersection(*map(set,res))
        if len(res) > 0:
            return list(res)
        else:
            return []
    else:
        return []
    
    pass


filters = {
    "class": "A",
    "country": "USA",
}
print(filter_cities("city.xml", filters))