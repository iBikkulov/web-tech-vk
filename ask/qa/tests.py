from django.test import TestCase, Client
from django.urls import reverse

from .models import Question
from .forms import AskForm, AnswerForm


class QuestionViewTests(TestCase):

    def test_get_invalid_question(self):
        """If question_id is invalid return 404."""
        question_id = 0
        response = self.client.get(reverse('question', args=(question_id,)))
        self.assertEqual(response.status_code, 404)

    def test_get_valid_question(self):
        """If question_id is valid return 200."""
        question = Question.objects.create(title='title1', text='text1')
        response = self.client.get(reverse('question', args=(question.id,)))
        self.assertEqual(response.status_code, 200)


class AnswerFormTests(TestCase):

    def test_valid_data(self):
        question = Question.objects.create(title='title1', text='text1')
        form = AnswerForm(data={
            'text': 'text1',
            'question': question.id
        })
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        """Empty form data raises ValidationError."""
        form = AnswerForm(data={})
        self.assertFalse(form.is_valid())


class AskFormTests(TestCase):

    def test_valid_data(self):
        form = AskForm(data={
            'title': 'title1',
            'text': 'text1'
        })
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        """Empty form data raises ValidationError."""
        form = AskForm(data={})
        self.assertFalse(form.is_valid())