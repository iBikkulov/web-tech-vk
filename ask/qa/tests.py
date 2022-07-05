from django.test import TestCase, Client
from django.urls import reverse

from .models import Question, User


def create_test_user_if_not_exist():
    try:
        test_user = User.objects.get(username='test_user')
    except User.DoesNotExist:
        test_user = User.objects.create_user(username='test_user')
    return test_user


def create_question(title, text):
    """
    Create a question with the given 'title' and 'text';
    Author of the question is 'test_user'.
    """
    author = create_test_user_if_not_exist()
    return Question.objects.create(title=title, text=text, author=author)


class QuestionViewTests(TestCase):

    def test_get_invalid_question(self):
        """If question_id is invalid return 404"""
        question_id = 0
        response = self.client.get(reverse('question', args=(question_id,)))
        self.assertEqual(response.status_code, 404)

    def test_get_valid_question(self):
        """If question_id is valid return 200"""
        question = create_question(title='test title', text='test text')
        response = self.client.get(reverse('question', args=(question.id,)))
        self.assertEqual(response.status_code, 200)
