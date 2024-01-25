
import pytest
import book_downloader
#import TUL_knihovna_opac_downloader as TUL_dwnldr


@pytest.mark.parametrize("url, file_number", [
    ("https://knihovna-opac.tul.cz/media-viewer?rootDirectory=1079617#!?file=567471", 567471),
    ("https://knihovna-opac.tul.cz/media-viewer?rootDirectory=207986#!?file=69494", 69494)
])
def test_parse_file_number_from_url(url, file_number):
    assert book_downloader.parse_file_number_from_url(url) == file_number

@pytest.mark.parametrize("url, book_number", [
    ("https://knihovna-opac.tul.cz/media-viewer?rootDirectory=1079617#!?file=567471", 1079617),
    ("https://knihovna-opac.tul.cz/media-viewer?rootDirectory=207986#!?file=69494", 207986)
])
def test_parse_book_number_from_url(url, book_number):
    assert book_downloader.parse_book_number_from_url(url) == book_number