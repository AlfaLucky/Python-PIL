from PIL import Image
import os


class PilPractice:

    @staticmethod
    def delete_file(new_name):
        """Delete previously created files"""
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), new_name)
        try:
            os.remove(path)
            print(f'The {new_name} is removed.')
        except FileNotFoundError:
            print(f'The {new_name} is not present, but we will continue')

    @staticmethod
    def open_picture():
        """Original picture"""
        return Image.open('tiger.jpg')

    def halftone_modification(self):
        new_name = "halftone_tiger.jpg"
        self.delete_file(new_name)
        pil_im = self.open_picture()
        halftone = pil_im.convert('L')
        halftone.save(new_name)
