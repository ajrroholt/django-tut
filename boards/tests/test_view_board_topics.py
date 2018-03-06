from django.test import TestCase
from django.urls import resolve
from ..views import TopicListView

class BoardTopicTests(TestCase):
    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1')
        self.assertEquals(view.func.view_class, TopicListView)
