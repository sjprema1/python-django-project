import img2pdf
import os
from datetime import time
import PIL
from zipfile import ZipFile
class PdfProcessor:
    def __init__(self):
        pass

    def create_pdf_from_images(self,dataset, pdf_file_path):
        # creating images
        image_files = []
        # non_transparent_files = []
        try:
            for image_path, data in dataset.items():
                with open(image_path, 'wb') as f:
                    f.write(data)
                    filename = self.remove_transparency_save_jpeg(image_path)
                    image_files.append(image_path)
                    # non_transparent_files.append(fname)

            # create pdf file
            with open(pdf_file_path, "wb") as f:
                f.write(img2pdf.convert(image_files))
        except Exception as e:
            print(str(e))
            raise Exception(e)

        time.sleep(1)
        print('Deleting temp docs:')
        self.clear_temp_stored_documents(image_files)
        # self.clear_temp_stored_documents(non_transparent_files)
        print('All temp docs deleted')
        return True

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

create_pdf_from_images()