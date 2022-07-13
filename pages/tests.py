from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class PageTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_uses_correct_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "pages/index.html")
        self.assertTemplateUsed(response, "base.html")

    def test_about_page_uses_correct_template(self):
        response = self.client.get("/about/")
        self.assertTemplateUsed(response, "pages/about.html")
        self.assertTemplateUsed(response, "base.html")

    def test_home_page_contains_string(self):
        response = self.client.get("/")
        self.assertContains(response, "Hello, World!")

    def test_about_page_contains_string(self):
        response = self.client.get("/about/")
        self.assertContains(response, "About the developer")

    def test_home_page_reverse_lookup(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/index.html")

    def test_about_page_reverse_lookup(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/about.html")
