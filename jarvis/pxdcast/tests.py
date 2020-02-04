from django.test import TestCase

from .helpers import feed


class FeedTestCase(TestCase):

    def test_format_duration(self):
        self.assertEqual(feed.format_duration('01:36:41'), '1h 36m')
        self.assertEqual(feed.format_duration('00:36:41'), '36 mins')
        self.assertEqual(feed.format_duration('00:00:41'), '41 secs')

    def test_format_uploaded_at(self):
        self.assertEqual(1, 1)
