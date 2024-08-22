import os
from zipfile import ZipFile
import logging
from django.conf import settings
from pypdf import PdfReader

def mergepdf_to_pdf(self, pdfs, savepath):
    merger = PdfMerger()
    db_logger = logging.getLogger('db')
    zipfile_name = os.path.join(settings.DOC_DWNLD_SHARED_DIR)
    savepath = os.path.join(settings.DOC_DWNLD_SHARED_DIR + savepath + ".pdf")
    try:
        if not os.path.isdir(zipfile_name):
            os.makedirs(zipfile_name, 755)
        os.chmod(zipfile_name, 755)

        for pdf in pdfs:
            merger.append(pdf)
        merger.write(savepath)
        merger.close()
        return savepath
    except Exception as e:
        print(e)
        db_logger.exception(e)
        return False