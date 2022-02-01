import zipfile

def unzip_files(input_path,output_path):
    with zipfile.ZipFile(input_path, 'r') as zip_ref:
        zip_ref.extractall(output_path)
