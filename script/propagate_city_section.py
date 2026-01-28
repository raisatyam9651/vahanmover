import os
import re

# Logic configuration
SECTION_HTML = """    <!-- Car Transport By City Section -->
    <section style="padding: 80px 0; background: rgba(255,255,255,0.02); position: relative;">
        <div class="container">
            <div style="text-align: center; margin-bottom: 60px;">
                <h2 style="font-size: 3rem; margin-bottom: 15px; font-weight: 700;">Car Transport <span
                        style="color: var(--color-primary);">By City</span></h2>
                <p style="color: var(--color-text-dim); font-size: 1.1rem; max-width: 700px; margin: 0 auto;">We offer
                    secure car transport services in all major cities across India.</p>
            </div>

            <div class="glass-card" style="padding: 50px; max-width: 1200px; margin: 0 auto;">
                <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 30px;">
                    <!-- Column 1 -->
                    <ul style="list-style: none; padding: 0;">
                        <li
                            style="padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; align-items: flex-start; gap: 10px;">
                            <i class="fa-solid fa-location-dot"
                                style="color: var(--color-primary); font-size: 0.8rem; margin-top: 5px; flex-shrink: 0;"></i>
                            <a href="#"
                                style="color: var(--color-text-white); font-size: 1rem; text-decoration: none; transition: 0.3s;">Car
                                Transport in Delhi</a>
                        </li>
                        <li
                            style="padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; align-items: flex-start; gap: 10px;">
                            <i class="fa-solid fa-location-dot"
                                style="color: var(--color-primary); font-size: 0.8rem; margin-top: 5px; flex-shrink: 0;"></i>
                            <a href="#"
                                style="color: var(--color-text-white); font-size: 1rem; text-decoration: none; transition: 0.3s;">Car
                                Transport in Mumbai</a>
                        </li>
                        <li
                            style="padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; align-items: flex-start; gap: 10px;">
                            <i class="fa-solid fa-location-dot"
                                style="color: var(--color-primary); font-size: 0.8rem; margin-top: 5px; flex-shrink: 0;"></i>
                            <a href="#"
                                style="color: var(--color-text-white); font-size: 1rem; text-decoration: none; transition: 0.3s;">Car
                                Transport in Bangalore</a>
                        </li>
                        <li
                            style="padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; align-items: flex-start; gap: 10px;">
                            <i class="fa-solid fa-location-dot"
                                style="color: var(--color-primary); font-size: 0.8rem; margin-top: 5px; flex-shrink: 0;"></i>
                            <a href="#"
                                style="color: var(--color-text-white); font-size: 1rem; text-decoration: none; transition: 0.3s;">Car
                                Transport in Hyderabad</a>
                        </li>
                        <li
                            style="padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; align-items: flex-start; gap: 10px;">
                            <i class="fa-solid fa-location-dot"
                                style="color: var(--color-primary); font-size: 0.8rem; margin-top: 5px; flex-shrink: 0;"></i>
                            <a href="#"
                                style="color: var(--color-text-white); font-size: 1rem; text-decoration: none; transition: 0.3s;">Car
                                Transport in Chennai</a>
                        </li>
                        <li
                            style="padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; align-items: flex-start; gap: 10px;">
                            <i class="fa-solid fa-location-dot"
                                style="color: var(--color-primary); font-size: 0.8rem; margin-top: 5px; flex-shrink: 0;"></i>
                            <a href="#"
                                style="color: var(--color-text-white); font-size: 1rem; text-decoration: none; transition: 0.3s;">Car
                                Transport in Kolkata</a>
                        </li>
                    </ul>

                    <!-- Column 2 -->
                    <ul style="list-style: none; padding: 0;">
                        <li
                            style="padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; align-items: flex-start; gap: 10px;">
                            <i class="fa-solid fa-location-dot"
                                style="color: var(--color-primary); font-size: 0.8rem; margin-top: 5px; flex-shrink: 0;"></i>
                            <a href="#"
                                style="color: var(--color-text-white); font-size: 1rem; text-decoration: none; transition: 0.3s;">Car
                                Transport in Pune</a>
                        </li>
                        <li
                            style="padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; align-items: flex-start; gap: 10px;">
                            <i class="fa-solid fa-location-dot"
                                style="color: var(--color-primary); font-size: 0.8rem; margin-top: 5px; flex-shrink: 0;"></i>
                            <a href="#"
                                style="color: var(--color-text-white); font-size: 1rem; text-decoration: none; transition: 0.3s;">Car
                                Transport in Ahmedabad</a>
                        </li>
                        <li
                            style="padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; align-items: flex-start; gap: 10px;">
                            <i class="fa-solid fa-location-dot"
                                style="color: var(--color-primary); font-size: 0.8rem; margin-top: 5px; flex-shrink: 0;"></i>
                            <a href="#"
                                style="color: var(--color-text-white); font-size: 1rem; text-decoration: none; transition: 0.3s;">Car
                                Transport in Jaipur</a>
                        </li>
                        <li
                            style="padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; align-items: flex-start; gap: 10px;">
                            <i class="fa-solid fa-location-dot"
                                style="color: var(--color-primary); font-size: 0.8rem; margin-top: 5px; flex-shrink: 0;"></i>
                            <a href="#"
                                style="color: var(--color-text-white); font-size: 1rem; text-decoration: none; transition: 0.3s;">Car
                                Transport in Chandigarh</a>
                        </li>
                        <li
                            style="padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; align-items: flex-start; gap: 10px;">
                            <i class="fa-solid fa-location-dot"
                                style="color: var(--color-primary); font-size: 0.8rem; margin-top: 5px; flex-shrink: 0;"></i>
                            <a href="#"
                                style="color: var(--color-text-white); font-size: 1rem; text-decoration: none; transition: 0.3s;">Car
                                Transport in Lucknow</a>
                        </li>
                        <li
                            style="padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; align-items: flex-start; gap: 10px;">
                            <i class="fa-solid fa-location-dot"
                                style="color: var(--color-primary); font-size: 0.8rem; margin-top: 5px; flex-shrink: 0;"></i>
                            <a href="#"
                                style="color: var(--color-text-white); font-size: 1rem; text-decoration: none; transition: 0.3s;">Car
                                Transport in Surat</a>
                        </li>
                    </ul>

                    <!-- Column 3 -->
                    <ul style="list-style: none; padding: 0;">
                        <li
                            style="padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; align-items: flex-start; gap: 10px;">
                            <i class="fa-solid fa-location-dot"
                                style="color: var(--color-primary); font-size: 0.8rem; margin-top: 5px; flex-shrink: 0;"></i>
                            <a href="#"
                                style="color: var(--color-text-white); font-size: 1rem; text-decoration: none; transition: 0.3s;">Car
                                Transport in Indore</a>
                        </li>
                        <li
                            style="padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; align-items: flex-start; gap: 10px;">
                            <i class="fa-solid fa-location-dot"
                                style="color: var(--color-primary); font-size: 0.8rem; margin-top: 5px; flex-shrink: 0;"></i>
                            <a href="#"
                                style="color: var(--color-text-white); font-size: 1rem; text-decoration: none; transition: 0.3s;">Car
                                Transport in Patna</a>
                        </li>
                        <li
                            style="padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; align-items: flex-start; gap: 10px;">
                            <i class="fa-solid fa-location-dot"
                                style="color: var(--color-primary); font-size: 0.8rem; margin-top: 5px; flex-shrink: 0;"></i>
                            <a href="#"
                                style="color: var(--color-text-white); font-size: 1rem; text-decoration: none; transition: 0.3s;">Car
                                Transport in Nagpur</a>
                        </li>
                        <li
                            style="padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; align-items: flex-start; gap: 10px;">
                            <i class="fa-solid fa-location-dot"
                                style="color: var(--color-primary); font-size: 0.8rem; margin-top: 5px; flex-shrink: 0;"></i>
                            <a href="#"
                                style="color: var(--color-text-white); font-size: 1rem; text-decoration: none; transition: 0.3s;">Car
                                Transport in Bhopal</a>
                        </li>
                        <li
                            style="padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; align-items: flex-start; gap: 10px;">
                            <i class="fa-solid fa-location-dot"
                                style="color: var(--color-primary); font-size: 0.8rem; margin-top: 5px; flex-shrink: 0;"></i>
                            <a href="#"
                                style="color: var(--color-text-white); font-size: 1rem; text-decoration: none; transition: 0.3s;">Car
                                Transport in Vadodara</a>
                        </li>
                        <li
                            style="padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; align-items: flex-start; gap: 10px;">
                            <i class="fa-solid fa-location-dot"
                                style="color: var(--color-primary); font-size: 0.8rem; margin-top: 5px; flex-shrink: 0;"></i>
                            <a href="#"
                                style="color: var(--color-text-white); font-size: 1rem; text-decoration: none; transition: 0.3s;">Car
                                Transport in Ludhiana</a>
                        </li>
                    </ul>

                    <!-- Column 4 -->
                    <ul style="list-style: none; padding: 0;">
                        <li
                            style="padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; align-items: flex-start; gap: 10px;">
                            <i class="fa-solid fa-location-dot"
                                style="color: var(--color-primary); font-size: 0.8rem; margin-top: 5px; flex-shrink: 0;"></i>
                            <a href="#"
                                style="color: var(--color-text-white); font-size: 1rem; text-decoration: none; transition: 0.3s;">Car
                                Transport in Kochi</a>
                        </li>
                        <li
                            style="padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; align-items: flex-start; gap: 10px;">
                            <i class="fa-solid fa-location-dot"
                                style="color: var(--color-primary); font-size: 0.8rem; margin-top: 5px; flex-shrink: 0;"></i>
                            <a href="#"
                                style="color: var(--color-text-white); font-size: 1rem; text-decoration: none; transition: 0.3s;">Car
                                Transport in Visakhapatnam</a>
                        </li>
                        <li
                            style="padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; align-items: flex-start; gap: 10px;">
                            <i class="fa-solid fa-location-dot"
                                style="color: var(--color-primary); font-size: 0.8rem; margin-top: 5px; flex-shrink: 0;"></i>
                            <a href="#"
                                style="color: var(--color-text-white); font-size: 1rem; text-decoration: none; transition: 0.3s;">Car
                                Transport in Agra</a>
                        </li>
                        <li
                            style="padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; align-items: flex-start; gap: 10px;">
                            <i class="fa-solid fa-location-dot"
                                style="color: var(--color-primary); font-size: 0.8rem; margin-top: 5px; flex-shrink: 0;"></i>
                            <a href="#"
                                style="color: var(--color-text-white); font-size: 1rem; text-decoration: none; transition: 0.3s;">Car
                                Transport in Nashik</a>
                        </li>
                        <li
                            style="padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; align-items: flex-start; gap: 10px;">
                            <i class="fa-solid fa-location-dot"
                                style="color: var(--color-primary); font-size: 0.8rem; margin-top: 5px; flex-shrink: 0;"></i>
                            <a href="#"
                                style="color: var(--color-text-white); font-size: 1rem; text-decoration: none; transition: 0.3s;">Car
                                Transport in Raipur</a>
                        </li>
                        <li
                            style="padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; align-items: flex-start; gap: 10px;">
                            <i class="fa-solid fa-location-dot"
                                style="color: var(--color-primary); font-size: 0.8rem; margin-top: 5px; flex-shrink: 0;"></i>
                            <a href="#"
                                style="color: var(--color-text-white); font-size: 1rem; text-decoration: none; transition: 0.3s;">Car
                                Transport in Bhubaneswar</a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </section>
"""

def update_file(filepath):
    """
    Inserts the section into the given file after the Contact Form section.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if already inserted
        if "Car Transport in Delhi" in content and "Car Transport By City" in content:
            print(f"Skipping {filepath}: Section already exists.")
            return

        # Find insertion point:
        # Looking for the closing section tag of the Contact Form.
        # The Contact Form section typically has "Request a Free Quote"
        
        # We'll look for the end of the contact form section.
        # It usually ends right before the Footer include OR the State-wise section.
        
        # Pattern:
        # </section>
        # (whitespace)
        # <?php include 'includes/footer.php'; ?>
        
        # OR
        
        # </section>
        # (whitespace)
        # <!-- State-wise Bike Transport Section ... -->
        
        # Let's try to find "Request a Free Quote" and then the next </section>
        
        # Regex to find the "Request a Free Quote" header potentially spanning lines/tags
        # We need to find the start of the section that *contains* this text.
        # But our logic was: find text, then find closing </section>.
        
        # Let's verify we are in the right section.
        # The section starts with <section ...> ... Request a Free Quote ... </section>
        
        # Simpler approach: Find "id=\"contactForm\"" as that is unique and inside the section.
        contact_form_match = re.search(r'id=["\']contactForm["\']', content)
        
        if not contact_form_match:
            # Fallback to text if ID missing
             quote_match = re.search(r'Request a\s+(?:<span[^>]*>)?Free Quote', content, re.DOTALL | re.IGNORECASE)
             if not quote_match:
                 print(f"Skipping {filepath}: Contact form/text not found.")
                 return
             # Approximate position
             start_search_pos = quote_match.end()
        else:
             start_search_pos = contact_form_match.end()

        # Find the closing </section> of the *container* section.
        # The form is inside a div, inside a container div, inside the section.
        # This is tricky with regex. 
        # Structure:
        # <section> 
        #    ... Free Quote ...
        #    <div ...> <form id="contactForm"> ... </form> </div>
        # </section>
        
        # So we need the third </section> after the header? Or just look for the </section> that is immediately followed by footer/end of file.
        
        # Robust logic: Find `<?php include 'includes/footer.php'; ?>` and insert BEFORE it, but ensuring we are outside the last section.
        # Check if the text before footer is `</section>`.
        
        footer_match = re.search(r'<\?php\s+include\s+[\'"]includes/footer\.php[\'"];\s*\?>', content)
        if not footer_match:
             print(f"Skipping {filepath}: Footer include not found.")
             return
             
        # Look backwards from footer to find the last closing </section>
        # Or just insert before the footer?
        # The file structure is <section>...</section> \n <?php include...
        # So inserting before the footer match is safe IF we verify we aren't breaking a section.
        
        # Let's check the text immediately preceding the footer (ignoring whitespace).
        footer_start = footer_match.start()
        pre_footer_chunk = content[max(0, footer_start-20):footer_start]
        
        if '</section>' in pre_footer_chunk or '</div>' in pre_footer_chunk or '</body>' in pre_footer_chunk: 
             # Seems safe to insert before footer
             # But wait, original request said "after Request a Free Quote section".
             # If "Request a Free Quote" is the *last* section, then inserting before footer is correct.
             # If there are other sections after it (like existing footer stuff?), we might displace them.
             
             # Let's verify "Request a Free Quote" is indeed the last major section.
             # In `car-transport-andhra-pradesh.php`, it IS the last section.
             
             new_content = content[:footer_start] + "\n" + SECTION_HTML + "\n\n    " + content[footer_start:]
             
             with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
             print(f"Updated {filepath}")
             return

        print(f"Skipping {filepath}: undetermined insertion point before footer.")
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

def main():
    # If running from project root (Shifter/), the script is in script/ and target is .
    # If running from script/, target is ../
    
    current_dir = os.getcwd()
    if os.path.basename(current_dir) == 'script':
         directory = "../"
    else:
         directory = "./"
    
    print(f"Scanning directory: {os.path.abspath(directory)}")
    
    # Files to process
    files = [f for f in os.listdir(directory) if f.startswith('car-transport-') and f.endswith('.php')]
    
    print(f"Found {len(files)} target files.")
    
    for filename in files:
        if filename == 'car-transport-service.php':
            continue
            
        filepath = os.path.join(directory, filename)
        update_file(filepath)

if __name__ == "__main__":
    main()
