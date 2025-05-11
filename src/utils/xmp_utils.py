from PIL import Image
import xml.etree.ElementTree as ET

def get_image_rating(image_path):
    try:
        image = Image.open(image_path)
        xmp_data = image.info.get("xmp")
        if xmp_data:
            # Decode the XMP data from bytes to string
            xmp_str = xmp_data.decode("utf-8")
            
            # Parse the XMP data as XML
            root = ET.fromstring(xmp_str)
            
            # Find the xmp:Rating attribute in the XML
            for description in root.findall(".//{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description"):
                rating = description.attrib.get("{http://ns.adobe.com/xap/1.0/}Rating")
                if rating:
                    return int(rating)
    except Exception as e:
        print(f"Error reading XMP metadata from {image_path}: {e}")
    return 0

def get_image_label(image_path):
    try:
        image = Image.open(image_path)
        xmp_data = image.info.get("xmp")
        if xmp_data:
            # Decode the XMP data from bytes to string
            xmp_str = xmp_data.decode("utf-8")
            
            # Parse the XMP data as XML
            root = ET.fromstring(xmp_str)
            
            # Find the xmp:Label attribute in the XML
            for description in root.findall(".//{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description"):
                label = description.attrib.get("{http://ns.adobe.com/xap/1.0/}Label")
                if label:
                    return label
    except Exception as e:
        print(f"Error reading XMP metadata from {image_path}: {e}")
    return None

