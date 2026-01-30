
import zipfile
import os
import shutil

INPUT_POTX = "/Users/davidarthurs/Projects/AISDLC/00_Introduction/Into_CleanDeck.potx"
OUTPUT_PPTX = "/Users/davidarthurs/Projects/AISDLC/00_Introduction/Into_CleanDeck_Fixed.pptx"

def convert_potx():
    if os.path.exists(OUTPUT_PPTX):
        os.remove(OUTPUT_PPTX)
        
    # Copy potx to new pptx (zip file)
    shutil.copyfile(INPUT_POTX, OUTPUT_PPTX)
    
    # We need to modify files *inside* the zip. 
    # Python's zipfile doesn't support easy inplace edit. 
    # We have to allow read/write or create a new one.
    
    # Strategy: Read all files, replace content in memory, write to new zip.
    
    temp_zip = OUTPUT_PPTX + ".temp"
    
    with zipfile.ZipFile(INPUT_POTX, 'r') as zin:
        with zipfile.ZipFile(temp_zip, 'w') as zout:
            for item in zin.infolist():
                data = zin.read(item.filename)
                
                # Check if this file is Content_Types or .rels (usually text/xml)
                if item.filename.endswith(".xml") or item.filename.endswith(".rels"):
                    try:
                        text_data = data.decode('utf-8')
                        # Replace content type
                        new_text = text_data.replace(
                            "application/vnd.openxmlformats-officedocument.presentationml.template.main+xml",
                            "application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"
                        )
                        if new_text != text_data:
                            print(f"Patched {item.filename}")
                            data = new_text.encode('utf-8')
                    except:
                        pass # Binary or other encoding
                
                zout.writestr(item, data)
    
    # Move temp back
    shutil.move(temp_zip, OUTPUT_PPTX)
    print(f"Converted {INPUT_POTX} -> {OUTPUT_PPTX}")

if __name__ == "__main__":
    convert_potx()
