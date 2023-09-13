from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics

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
