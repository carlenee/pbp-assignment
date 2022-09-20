from django.test import TestCase, Client
from django.urls import reverse
# Create your tests here.
class MyWatchListViewTest(TestCase):

    def test_view_url_html_exists_at_desired_location(self):
        self.client = Client()
        response = self.client.get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)
    
    def test_view_url_xml_exists_at_desired_location(self):
        self.client = Client()
        response = self.client.get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_json_exists_at_desired_location(self):
        self.client = Client()
        response = self.client.get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name_html(self):
        self.client = Client()
        response = self.client.get(reverse('mywatchlist:show_mywatchlist'))
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name_xml(self):
        self.client = Client()
        response = self.client.get(reverse('mywatchlist:show_xml'))
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name_json(self):
        self.client = Client()
        response = self.client.get(reverse('mywatchlist:show_json'))
        self.assertEqual(response.status_code, 200)