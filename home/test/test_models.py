from django.test import TestCase

from user.models import User
from home.models import Test, Question


class TestModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='Den1s',
            email='test@test.com',
            password='Q1w2e3r4t5y6_'
        )

        self.test_model = Test.objects.create(
            title='My test',
            description='test my model test',
            owner=self.user
        )

    def test_create_model_test(self):
        self.assertEquals(self.test_model.owner, self.user)
        self.assertEquals(self.test_model.title, 'My test')
        self.assertEquals(self.test_model.description, 'test my model test')


class TestModelQuestion(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='Den1s',
            email='test@test.com',
            password='Q1w2e3r4t5y6_'
        )

        self.test_model = Test.objects.create(
            title='My test',
            description='test my model test',
            owner=self.user
        )

        self.question = Question.objects.create(
            test=self.test_model,
            text='is my question?'
        )

    def test_create_question(self):
        self.assertEquals(self.question.test, self.test_model)
        self.assertEquals(self.question.text, 'is my question?')


