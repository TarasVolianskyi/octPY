from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Question, Choice


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date', 'author']


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'choice_text', 'votes']


class QuestionNestedSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date', 'author', 'choices']


class ChoiceNestedSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = Choice
        fields = ['id', 'choice_text', 'votes', 'question']