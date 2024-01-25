# By Pytel
"""
Tento program stáhne knihu z internetu a uloží ji do souboru.
"""

import os
import re
import img2pdf
from colors import *
from TUL_knihovna_opac_downloader import *

def parse_book_number_from_url(url):
    """ Parse book number from url.
    https://knihovna-opac.tul.cz/media-viewer?rootDirectory=207986#!?file=69494 => 207986
    """
    return int(re.findall(r'rootDirectory=(.*)#!?', url)[0])

def parse_file_number_from_url(url):
    """ Parse file number from url. 
    https://knihovna-opac.tul.cz/media-viewer?rootDirectory=207986#!?file=69494 => 69494
    """
    return int(re.findall(r'file=(.*)', url)[0])

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

DEBUG = True

book_url = "https://knihovna-opac.tul.cz/media-viewer?rootDirectory=1079617"
first_page_number = 567467
number_of_pages = 617

book_url = "https://knihovna-opac.tul.cz/media-viewer?rootDirectory=207986"
book_number = 207986
first_page_number = 445748
number_of_pages = 117

def read_instructions():
    """ Read instructions. """
    # načtení url
    while True:
        book_url = input("Zadejte URL: ")
        if test_url(book_url):
            break
        else:
            print(Red + "Špatná url!" + NC)

    # získání počtu stránek
    while True:
        number_of_pages = input("Zadejte počet stránek: ")
        if number_of_pages.isdigit():
            number_of_pages = int(number_of_pages)
            if number_of_pages > 0:
                break
        else:
            print(Red + "Špatný počet!" + NC)
    
    # první stránka
    while True:
        first_page_url = input("Zadejte url první stránky: ")
        if test_url(first_page_url):
            break
        else:
            print(Red + "Špatná url!" + NC)

    first_page_file_number = parse_file_number_from_url(first_page_url)
    return book_url, number_of_pages, first_page_file_number

def main():
    """ Main function. """
    print("Tento program stáhne knihu z internetové knihovny TUL a uloží ji do souboru.")
    
    book_url, number_of_pages, first_page_number = read_instructions()
    if DEBUG:
        print(
            "book_url:", book_url,"\n",
            "number_of_pages:", number_of_pages,"\n",
            "first_page_number:", first_page_number)

    book_downloader = TUL_dwnldr()
    book_downloader.download_book(book_url, number_of_pages, first_page_number)
    
    print(Green + "Hotovo!" + NC)

if __name__ == '__main__':
    main()

    # TODO:
    #save_page_to_file(download_url(book_url), "book.html")
    #print(get_number_of_pages_from_url(book_url))
