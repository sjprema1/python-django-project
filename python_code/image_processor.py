
import logging
import random
import PIL
import mimetypes
from pdf2image import convert_from_path
from django.conf import settings
import os



class PdfProcessor:
    def __init__(self):
        pass

    def pdf_to_image(self, docpath, fileid=None,):
        db_logger = logging.getLogger('db')
        doc_data = {}
        if not fileid:
            fileid = random.randrange(100000, 10000000, 3)

        ext = 'jpeg'
        savepath = os.path.join(settings.BASE_DIR + '/dq_int' + settings.DQ_TEMP_DOC_DIR, 'dq-doc_' + str(fileid))
        os.makedirs(settings.BASE_DIR + '/dq_int' + settings.DQ_TEMP_DOC_DIR, exist_ok=True)
        try:
            pages = convert_from_path(docpath, 500)
            counter = 0
            for page in pages:
                counter = counter + 1

                image_filename = '{}-{}.jpg'.format(savepath, counter)
                image_filename = os.path.join(image_filename)

                page.save(image_filename, "JPEG")
                # print(image_filename)
                img = PIL.Image.open(image_filename)

                width, height = img.size
                filesize = os.stat(image_filename).st_size
                mtiype = mimetypes.guess_type(image_filename)
                contenttype = mtiype[0]

                doc_data[counter] = {
                    'fileid': fileid,
                    'docpath': image_filename,
                    'extension': ext,
                    'mime': contenttype,
                    'height': height,
                    'width': width,
                    'size': filesize,
                }

                img = None
            # print(doc_data)
            return doc_data
        except Exception as e:
            print(e)
            print(str(fileid) + " " + ext)
            db_logger.exception(e)
            db_logger.debug(docpath)
            return False

    def remove_transparency_save_jpeg(self, filename):

        try:
            fname = os.path.join(filename)
            img = PIL.Image.open(fname)
            ext = img.format.lower()

            if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                new_ext = 'jpeg'
                file_det = filename.split('.')
                png_img = img.convert("RGB")
                new_file = file_det[0] + "." + new_ext
                png_img.save(new_file, "JPEG", quality=70)
                return new_file
            else:
                return filename

        except Exception as e:
            print(e)
            return filename

pdf_to_image()



