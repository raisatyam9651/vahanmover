import os
import glob
import datetime
import xml.etree.ElementTree as ET

def update_sitemap(sitemap_path, base_url="https://vahanmover.com"):
    # Register namespace to avoid 'ns0' prefixes
    ET.register_namespace('', "http://www.sitemaps.org/schemas/sitemap/0.9")
    
    try:
        tree = ET.parse(sitemap_path)
        root = tree.getroot()
    except Exception as e:
        print(f"Error parsing sitemap: {e}")
        return

    # Namespace map
    ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    
    # Get existing locations
    existing_urls = set()
    for url in root.findall('sm:url', ns):
        loc = url.find('sm:loc', ns)
        if loc is not None:
            existing_urls.add(loc.text.strip())
            
    # Find generated files
    # Bike pages
    bike_pages = glob.glob("bike-transport-*-noida.php")
    # Car pages
    car_pages = glob.glob("car-transport-*-noida.php")
    
    # Also include the main Noida pages if not present (though they likely are)
    all_pages = bike_pages + car_pages
    
    today = datetime.date.today().isoformat()
    added_count = 0
    
    for page in all_pages:
        page_url = f"{base_url}/{page}"
        
        if page_url not in existing_urls:
            # Create new url element
            url_elem = ET.SubElement(root, "url")
            
            loc_elem = ET.SubElement(url_elem, "loc")
            loc_elem.text = page_url
            
            lastmod_elem = ET.SubElement(url_elem, "lastmod")
            lastmod_elem.text = today
            
            changefreq_elem = ET.SubElement(url_elem, "changefreq")
            changefreq_elem.text = "monthly"
            
            priority_elem = ET.SubElement(url_elem, "priority")
            priority_elem.text = "0.7"
            
            added_count += 1
            print(f"Added: {page}")
    
    if added_count > 0:
        # Indent not strictly supported by ElementTree until Python 3.9+, 
        # but we can try basic write.
        # To get pretty print, we can use minidom or just let it be standard XML.
        # Let's write it back.
        tree.write(sitemap_path, encoding='UTF-8', xml_declaration=True)
        print(f"\nSuccessfully added {added_count} new pages to sitemap.")
    else:
        print("\nNo new pages to add.")

if __name__ == "__main__":
    update_sitemap("sitemap.xml")
