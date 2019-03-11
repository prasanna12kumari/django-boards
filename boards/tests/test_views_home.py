from django.urls import reverse,resolve
from django.test import TestCase
from ..views import BoardListView
from ..models import Board

# Create your tests here.
class HomeTests(TestCase):

	def setUp(self):
		self.board = Board.objects.create(name = 'Django',description = 'This is a Django discussion board')
		url = reverse('home')		
		self.response = self.client.get(url)
		
	def test_home_view_status_code(self):
				
		self.assertEquals(self.response.status_code,200)
		
	def test_home_url_resolves_home_view(self):
		view = resolve('/')		
		self.assertEquals(view.func.view_class,BoardListView)
	
	def test_home_view_contains_links_to_topics_page(self):
	
		board_topics_url = reverse('board_topics',kwargs = {'pk': self.board.pk})		
		self.assertContains(self.response,'href="{0}"'.format(board_topics_url))