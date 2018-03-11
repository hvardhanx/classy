from django.contrib.auth import get_user_model
from courses.models import Subject, Course
from django.test import TestCase

User = get_user_model()


class TestCoursesApi(TestCase):
    def setUp(self):
        user = User.objects.create(username='test', email='test@test.com')
        user.save()
        subject = Subject.objects.create(title='Computer Science', slug='computer-science')
        course = Course.objects.create(owner=user, subject=subject, title='Computer Networks', slug='computer-network',
                                       overview='Learn about networking')

    def test_home_view(self):
        response = self.client.get('/')
        self.assertContains(response, "Computer Science")
        self.assertContains(response, "Computer Networks")
        self.assertEqual(response.status_code, 200)
