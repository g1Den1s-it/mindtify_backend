from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated

from user.models import User
from home.models import (
    Test,
    Question,
    Choice,
    TextAnswer,
    ResponseTest
)
from home.serializers import (
    TestSerializer,
    QuestionSerializer,
    ChoiceSerializer,
    TakeTestSerializer,
    ResponseTestSerializer
)


# Create your views here.


class HomeView(generics.ListAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()


class TakeTestView(generics.ListCreateAPIView):
    serializer_class = TestSerializer

    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug', None)

        test = get_object_or_404(Test, slug=slug)

        serializer = TakeTestSerializer(test)

        return Response(serializer.data)


class AnswerView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data

        test = get_object_or_404(Test, slug=data['test'])
        user = get_object_or_404(User, username=request.user)

        answer_user = ResponseTest.objects.create(
            user=user,
            test=test,
        )

        for question_id, choose_text in data['question'].items():
            answer_user.question.add(get_object_or_404(Question, id=question_id))
            answer_user.choice.add(get_object_or_404(Choice, text=choose_text))

        answer_user.save()
        return Response(status=status.HTTP_201_CREATED)
