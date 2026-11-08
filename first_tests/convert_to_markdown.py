import os;
from docling.document_converter import DocumentConverter as DC
from first_tests.config import INPUTS_ORIGINAL_DIR, INPUTS_MARKDOWNBIS_DIR

input_path = INPUTS_ORIGINAL_DIR
input_path_markdown = INPUTS_MARKDOWNBIS_DIR
converter = DC()    

for folder in os.listdir(input_path):
    print(f"Processing folder: {folder}...")
    if not os.path.isdir(os.path.join(input_path_markdown, folder)):
        os.makedirs(os.path.join(input_path_markdown, folder))
        print(f"=> Created folder: {folder} in {input_path_markdown}")
    else:
        print(f"=> Folder {folder} already exists in {input_path_markdown}, skipping creation.")
    for input_file in os.listdir(os.path.join(input_path, folder)):
        print(f"Found file: {input_file}...")
        _, extension = os.path.splitext(input_file)
        output_file_name = input_file.replace(extension, '.md')
        if not os.path.isfile(os.path.join(input_path_markdown, folder, output_file_name)):
            print(f"=> Converting {input_file} to {output_file_name}")
            try:
                markdown = converter.convert(os.path.join(input_path, folder, input_file)).document.export_to_markdown()
                with open(os.path.join(input_path_markdown, folder, output_file_name), "w+", encoding="utf-8") as output_file:
                    output_file.write(markdown)
                print(f"=> Conversion complete: {output_file_name}")
            except Exception as e:
                print(f"=> Error occurred while converting {input_file}")
                print(f"=> Error {type(e).__name__} : {e}")
        else:
            print(f"=> File {output_file_name} already exists, skipping conversion.")