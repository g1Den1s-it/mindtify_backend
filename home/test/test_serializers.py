from django.test import TestCase

from home.models import Test, Question
from user.models import User
from home.serializers import (
    TestSerializer,
    QuestionSerializer,
)


class TestSerializerTest(TestCase):
    def setUp(self):
        # models
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

        # serializer
        self.test_serializer = TestSerializer(instance=self.test_model)

    def test_serializer_dat(self):
        data = self.test_serializer.data

        self.assertEquals(data['title'], 'My test')
        self.assertEquals(data['description'], 'test my model test')
        self.assertEquals(data['owner'], self.user.username)


class QuestionSerializerTest(TestCase):
    def setUp(self):
        # models
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
            text='is question?'
        )

        # serializer
        self.question_serializer = QuestionSerializer(instance=self.question)

    def test_question_serializer(self):
        data = self.question_serializer.data

        self.assertEquals(data['text'], 'is question?')
        self.assertEquals(data['test'], self.test_model.id)
