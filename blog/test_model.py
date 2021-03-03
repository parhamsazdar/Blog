from django.test import TestCase
from blog.models import *
from blog.stop_word import stemmer


class PostTestCase(TestCase):
    def test_there_is_no_repeted_word_model_word_after_create_post(self):
        user = User.objects.create(username="ali", password="22561342Ps")
        category = Category.objects.create(name='programing', parent=None)
        post_1 = Post.objects.create(
            title="test",
            text="متن پرهام برای تست می باشد دوست من",
            user=user,
            category=category
        )
        self.post_2 = Post.objects.create(
            title="test",
            text="متن پرهام برای تست می باشد دوست من",
            user=user,
            category=category
        )
        word_count = Word.objects.filter(word__exact=stemmer('دوست')).count()
        self.assertEqual(word_count, 1)

    def confirm_deafulte_false_and_active_true(self):
        category = Category.objects.create(name='programing', parent=None)
        user = User.objects.create(username="ali", password="22561342Ps")
        self.post_1 = Post.objects.create(
            title="test",
            text="متن پرهام برای تست می باشد دوست من",
            user=user,
            category=category
        )
        self.assertEqual(self.post_1.confirm, False)
        self.assertEqual(self.post_1.active, False)





class CommentTestCase(TestCase):
    def comment_should_belong_to_post(self):
        user = User.objects.create(username="ali", password="22561342Ps")
        try:
            # we dont give a post to our comment.
            comment = Comments.objects.create(text="test comment", user=user)
        except:
            pass
