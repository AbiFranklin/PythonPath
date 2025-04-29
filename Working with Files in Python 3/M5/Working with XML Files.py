import xml.etree.ElementTree as ET

def parse_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        print(f"Domains for: {root.attrib['name']}")
        for child in root:
            print(f"  {child.tag}: {child.attrib['name']}")
    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
        return None
    
parse_xml('./Working with Files in Python 3/files_to_read/ef_author.xml')

def add_domain(fn, el, attr, val):
    try:
        tree = ET.parse(fn)
        root = tree.getroot()
        
        # Create a new element with the specified tag and attribute
        new_element = ET.Element(el, {attr: val})
        
        # Append the new element to the root
        root.append(new_element)
        
        # Write the changes back to the file
        tree.write(fn)
        print(f"Added element <{el} {attr}='{val}'> to {fn}")
    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

add_domain('./Working with Files in Python 3/files_to_read/ef_author.xml', 'domain', 'name', 'Javascript')
parse_xml('./Working with Files in Python 3/files_to_read/ef_author.xml')

def change_xml_element_et(fn, el, attr, old_val, new_val):
    try:
        tree = ET.parse(fn)
        root = tree.getroot()
        
        # Find the element with the specified attribute value
        for elem in root.findall(el):
            if elem.attrib.get(attr) == old_val:
                elem.set(attr, new_val)
                print(f"Changed <{el} {attr}='{old_val}'> to <{el} {attr}='{new_val}'>")
                break
        else:
            print(f"No element found with <{el} {attr}='{old_val}'>")
            return
        
        # Write the changes back to the file
        tree.write(fn)
    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

change_xml_element_et('./Working with Files in Python 3/files_to_read/ef_author.xml', 'domain', 'name', 'Javascript', 'Java')
parse_xml('./Working with Files in Python 3/files_to_read/ef_author.xml')


