# -*- coding: utf-8 -*-
import hummus
from tempfile import NamedTemporaryFile
import os


def assert_pdf(filename):
    with open(filename, 'rb') as stream:
        assert stream.read(4) == b'%PDF'


def test_document_file():
    with NamedTemporaryFile(delete=False) as stream:
        # Run through a normal cycle.
        document = hummus.Document(stream.name)
        document.begin()
        document.end()

    # Open and test the file.
    assert_pdf(stream.name)

    # Remove the file.
    os.remove(stream.name)


def test_document_stream():
    with NamedTemporaryFile(delete=False) as stream:
        # Run through a normal cycle.
        document = hummus.Document(stream)
        document.begin()
        document.end()

    # Open and test the file.
    assert_pdf(stream.name)

    # Remove the file.
    os.remove(stream.name)


def test_page_size():
    page = hummus.Page()

    assert page.box.left == 0

    page.box = hummus.Rectangle(0, 0, 800, 1000)

    assert page.box.bottom == 1000


def test_basic_text():
    with NamedTemporaryFile(delete=False) as stream:
        with hummus.Document(stream) as document:
            with document.Page() as page:
                pass

    # Open and test the file.
    assert_pdf(stream.name)

    # Remove the file.
    os.remove(stream.name)
