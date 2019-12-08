from unittest import TestCase
import vcr

from .utils import VCR_STORAGE
from ..client import MetroRail
from .. import responses
from ...tests.utils import API_KEY

class TestMetroRail(TestCase):
    def setUp(self):
        self.metroRail = MetroRail(API_KEY)

    @vcr.use_cassette(VCR_STORAGE.format('lines'))
    def test_lines(self):
        response = self.metroRail.lines()
        self.assertIsInstance(response, responses.Lines)
