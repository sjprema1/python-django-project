import os
from zipfile import ZipFile
import logging
from django.conf import settings

def create_zipfile(self, pdf_file, zip_path):
    db_logger = logging.getLogger('db')
    zipfile_name = os.path.join(settings.ZIP_DIR)
    zipfil_name = os.path.join(settings.ZIP_DIR + zip_path + ".zip")
    if not os.path.isdir(zipfile_name):
        os.makedirs(zipfile_name, 755)
    os.chmod(zipfile_name, 755)

    try:
        with ZipFile(zipfil_name, 'w') as myzip:
            for filename in pdf_file:
                myzip.write(filename, os.path.basename(filename))
            return zipfil_name
    except Exception as e:
        print(e)
        db_logger.exception(e)
        return False