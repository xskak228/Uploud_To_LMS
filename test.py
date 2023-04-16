import pytest
from requests import get

link = 'http://localhost:8081/api/v2/jobs'


def return_response(url):
    if "error" in get(link + url).json():
        return False
    elif "message" in get(link + url).json():
        return False
    else:
        return True


class TestResponse:
    def test_GoodList(self):
        assert return_response('') is True

    def test_GoodId(self):
        assert return_response('/1') is True

    def test_BadIdINT(self):
        assert return_response('/999') is False

    def test_BadIdSTR(self):
        assert return_response('/q') is False