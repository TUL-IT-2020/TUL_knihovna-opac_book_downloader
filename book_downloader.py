# By Pytel
"""
Tento program stáhne knihu z internetu a uloží ji do souboru.
"""

import os
import re
import img2pdf
import requests
from TUL_knihovna_opac_downloader import *

def get_picture_from_url(url):
    """ Get picture from url. """
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        return None

def save_picture_to_file(picture, filename):
    """ Save picture to file. """
    with open(filename, 'wb') as f:
        f.write(picture)

def get_save_as_name_from_url(url):
    """ Get save as name from url. """
    response = requests.get(url)
    if response.status_code == 200:
        return re.findall(r'filename="(.*)"', response.headers['Content-Disposition'])[0]
    else:
        return None

def get_number_of_pages_from_url(url):
    """ 
    Get value of element with class="input-group-addon ng-binding"
    """
    response = requests.get(url)
    if response.status_code == 200:
        return re.findall(r'class="input-group-addon ng-binding">(.*) / (.*)</span>', response.text)
    else:
        return None

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

def parse_file_number_from_url(url):
    """ Parse file number from url. 
    # https://knihovna-opac.tul.cz/files/567467?height=60 => 567467
    """
    return int(re.findall(r'files/(.*)\?', url)[0])

def jpgs_to_one_pdf(path, book_name: str = "book.pdf"):
    """ Convert jpg to pdf. """
    # get all jpg files in folder
    files = os.listdir(path)
    files = [file for file in files if file.endswith(".jpg")]

    # convert jpg to pdf
    with open(book_name, "wb") as pdf_file:
        pdf_file.write(img2pdf.convert(
            [os.path.join(os.sep, path, file) for file in files]
            ))


book_url = "https://knihovna-opac.tul.cz/media-viewer?rootDirectory=1079617&origin=https%3A%2F%2Fknihovna-opac.tul.cz%2Frecords%2Fdadfa210-84b1-48ea-95a1-4cfc3f4c42fb#!?file=567467"
raw_picture_url = "https://knihovna-opac.tul.cz/files/567467?height=60"
file_number = 443996

book_url = "https://knihovna-opac.tul.cz/media-viewer?rootDirectory=1079617"
file_path_url = "https://knihovna-opac.tul.cz/files/"
first_page_number = 567467
number_of_pages = 617
folder = "data"

def read_instructions():
    """ Read instructions. """
    # načtení url
    while True:
        book_url = input("Zadejte URL: ")
        if test_url(book_url):
            break
        else:
            print("Špatná url!")

    # získání počtu stránek
    while True:
        number_of_pages = input("Zadejte počet stránek: ")
        if number_of_pages.isdigit():
            number_of_pages = int(number_of_pages)
            if number_of_pages > 0:
                break
        else:
            print("Špatný počet!")
    
    # první stránka
    while True:
        first_page_url = input("Zadejte url první stránky: ")
        if test_url(first_page_url):
            break
        else:
            print("Špatná url!")

    first_page_number = parse_file_number_from_url(first_page_url)
    return book_url, number_of_pages, first_page_number


def main():
    """ Main function. """
    print("Tento program stáhne knihu z internetové knihovny TUL a uloží ji do souboru.")
    
    book_url, number_of_pages, first_page_number = read_instructions()

    path = os.path.join(os.getcwd(), folder)
    # vytvoření složky
    print("Vytvářím složku...")
    if not os.path.exists(path):
        os.makedirs(folder)
    # vyčištění složky
    else:
        for file in os.listdir(path):
            os.remove(os.path.join(folder, file))    

    # stáhnutí hnihy a uložení do souboru .jpg
    print("Stahuji knihu...")
    pictures = []
    for i in range(number_of_pages):
        picture_url = file_path_url + str(first_page_number + i)
        picture = get_picture_from_url(picture_url)
        picture_name = get_save_as_name_from_url(picture_url)
        picture_path = os.path.join(path, picture_name)
        save_picture_to_file(picture, picture_path)
        pictures.append(picture_path)

    # convert jpg to pdf
    print("Konvertuji do pdf...")
    with open("book.pdf", "wb") as pdf_file:
        # convert jpg to pdf
        pdf_file.write(img2pdf.convert(pictures))
    
    print("Hotovo!")

if __name__ == '__main__':
    main()
    #save_page_to_file(download_url(book_url), "book.html")
    #print(get_number_of_pages_from_url(book_url))
