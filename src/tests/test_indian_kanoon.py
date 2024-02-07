import pytest
from src.kanoon import IndianKanoon


def test_indian_kanoon_search():
    kanoon = IndianKanoon()
    assert kanoon.search("freedom of speech") is not None


def test_indian_kanoon_doc():
    kanoon = IndianKanoon()
    assert kanoon.doc("123") is not None
