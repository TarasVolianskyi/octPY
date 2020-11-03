from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer, QuestionNestedSerializer, ChoiceNestedSerializer


def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def index_t(request):
    return HttpResponse('Hello, 123')


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return HttpResponse('You are looking at question %s.' % question.question_text)


def results(request, question_id):
    response = 'You are looking at the results of question %s.'
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse('You are voting on question %s. %question_id')


class QuestionListCreate(generics.ListCreateAPIView):
    """
    Outputs all questions from db. Path = 'polls/question/'
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionById(generics.RetrieveUpdateDestroyAPIView):
    """
    Outputs question by question id. Path = 'polls/question/<int:question_id>/'
    """
    serializer_class = QuestionSerializer

    def get_object(self):
        obj = get_object_or_404(Question, pk=self.kwargs.get('question_id'))
        return obj


class ChoiceListCreate(generics.ListCreateAPIView):
    """
    Outputs list of all choices from db. Path = '/polls/choice/'
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class ChoiceById(generics.RetrieveUpdateDestroyAPIView):
    """
    Outputs choice by choice id. Path = 'polls/choice/<int:choice_id>/'
    """
    serializer_class = ChoiceSerializer

    def get_object(self):
        obj = get_object_or_404(Choice, pk=self.kwargs.get('choice_id'))
        return obj


class ChoiceByQuestionListCreate(generics.ListCreateAPIView):
    """
    Outputs list of choices for given question_id. Path = 'polls/<int:question_id>/choices'
    """
    serializer_class = ChoiceSerializer

    def get_queryset(self):
        obj = get_list_or_404(Choice, question=self.kwargs.get('question_id'))
        return obj


class QuestionChoiceNested(generics.RetrieveUpdateDestroyAPIView):
    """
    Outputs question by question_id with all related choices nested.
    Path = '/polls/question/<int:question_id>/choices/nested'
    """
    serializer_class = QuestionNestedSerializer

    def get_object(self):
        return get_object_or_404(Question, pk=self.kwargs.get('question_id'))


class ChoiceNested(generics.RetrieveUpdateDestroyAPIView):
    """
    Outputs choice by choice_id with related question nested. Path = '/polls/choice/<int:choice_id>/nested'
    """
    serializer_class = ChoiceNestedSerializer

    def get_object(self):
        return get_object_or_404(Choice, pk=self.kwargs.get('choice_id'))
