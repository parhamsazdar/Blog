

from django.contrib.auth.models import User
from django.db.models import Count
from django.test import Client, TestCase
from django.urls import reverse

from blog.models import Post, Category, UserInfo


class ViewTest(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_index_view(self):
        # Issue a GET request.
        response = self.client.get(reverse('blog:index'))

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        category = Category.objects.create(name='programing', parent=None)
        user = User.objects.create(username="ali", password="22561342Ps")
        post_1 = Post.objects.create(
            title="test",
            text="متن پرهام برای تست می باشد دوست من",
            user=user,
            category=category,
            active=True, confirm=True
        )
        print(Post.objects.all())



        self.assertEqual(len(response.context['latest_post']), 1)
        self.assertEqual(len(response.context['popular_post']), 1)

    def post_is_confirm_and_active(self):
        category = Category.objects.create(name='programing', parent=None)
        user = User.objects.create(username="ali", password="22561342Ps",first_name="parham",last_name='sazdar')
        user_info=UserInfo.objects.create(user=user,phone=22)
        post_1 = Post.objects.create(
            title="test",
            text="متن پرهام برای تست می باشد دوست من",
            user=user,
            category=category,
            confirm=True,active=True
        )

        response = self.client.get(reverse('blog:post_show',args=(post_1.pk,)))