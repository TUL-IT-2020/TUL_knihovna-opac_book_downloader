import os
import re
import img2pdf
import requests
#import TUL_knihovna_opac_downloader as TUL_dwnldr

def save_picture_to_file(picture, filename):
    """ Save picture to file. """
    with open(filename, 'wb') as f:
        f.write(picture)

def download_url(url):
    """ Download url. """
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def save_page_to_file(page, filename):
    """ Save page to file. """
    with open(filename, 'w') as file:
        file.write(page)

def test_url(url):
    """ Test url. """
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False

class TUL_dwnldr:

    def __init__(self, book_url):
        self.folder = "data"
        self.file_path_url = "https://knihovna-opac.tul.cz/files/"

    def get_picture_from_url(self, url):
        """ Get picture from url. """
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            return None

    def get_save_as_name_from_url(self, url):
        """ Get save as name from url. """
        response = requests.get(url)
        if response.status_code == 200:
            return re.findall(r'filename="(.*)"', response.headers['Content-Disposition'])[0]
        else:
            return None

    def save_all_pictures(self, number_of_pages, first_page_number):
        pictures = []
        for i in range(number_of_pages):
            picture_url = self.file_path_url + str(first_page_number + i)
            picture = self.get_picture_from_url(picture_url)
            picture_name = self.get_save_as_name_from_url(picture_url)
            picture_path = os.path.join(self.download_path, picture_name)
            save_picture_to_file(picture, picture_path)
            pictures.append(picture_path)
        return pictures
    
    def get_number_of_pages_from_url(url):
        """ 
        Get value of element with class="input-group-addon ng-binding"
        """
        response = requests.get(url)
        if response.status_code == 200:
            return re.findall(r'class="input-group-addon ng-binding">(.*) / (.*)</span>', response.text)
        else:
            return None

    def parse_file_number_from_url(url):
        """ Parse file number from url. 
        # https://knihovna-opac.tul.cz/files/567467?height=60 => 567467
        """
        return int(re.findall(r'files/(.*)\?', url)[0])

    def prepare_download_folder(self):
        self.download_path = os.path.join(os.getcwd(), self.folder)
        # vytvoření složky
        print("Vytvářím složku...")
        if not os.path.exists(self.download_path):
            os.makedirs(self.folder)
        # vyčištění složky
        else:
            for file in os.listdir(self.download_path):
                os.remove(os.path.join(self.folder, file))
    
    def download_book(
            self, book_url, 
            number_of_pages: int = -1, 
            first_page_number: int = -1, 
            book_name: str = "book.pdf"
        ):
        """ Download book. """
        self.book_url = book_url
        self.prepare_download_folder()

        if number_of_pages == -1:
            # TODO: get number of pages
            #number_of_pages = self.get_number_of_pages_from_url(self.book_url)
            raise NotImplementedError("number_of_pages is not implemented yet.")
        if first_page_number == -1:
            raise NotImplementedError("first_page_number is not implemented yet.")
            #first_picture_url = self.get_first_picture_url(self.book_url)
            #first_page_number = self.parse_file_number_from_url(first_picture_url)

        # save all pictures
        pictures = self.save_all_pictures(number_of_pages, first_page_number)

        # convert jpg to pdf
        with open(book_name, "wb") as pdf_file:
            # convert jpg to pdf
            pdf_file.write(img2pdf.convert(pictures))