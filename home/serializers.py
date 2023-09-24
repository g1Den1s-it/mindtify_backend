from rest_framework import serializers

from home.models import (
    Test,
    Question,
    Choice,
    ResponseTest
)


class TestSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()

    class Meta:
        model = Test
        fields = ('id', 'title', 'slug', 'owner', 'description')

    def get_owner(self, obj):
        return obj.owner.username if obj.owner else None


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'question', 'text', 'is_correct')


class QuestionSerializer(serializers.ModelSerializer):
    choice = ChoiceSerializer(many=True, read_only=True, source='choice_set')

    class Meta:
        model = Question
        fields = ('id', 'test', 'text', 'choice')


class TakeTestSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=True, read_only=True, source='question_set')

    class Meta:
        model = Test
        fields = ('id', 'title', 'slug', 'description', 'question')


class ResponseTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponseTest
        fields = ('id', 'user', 'test', 'question', 'choice', 'text_answer')
