from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index_t/', views.index_t, name='index_t'),

    # ex: /polls/5
    path('<int:question_id>/', views.detail, name='detail'),

    # ex: /polls/5/results
    path('<int:question_id>/results/', views.results, name='results'),

    # ex:/polls/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # rest API views
    # ex: /polls/question/
    path('question/', views.QuestionListCreate.as_view(), name='question_list'),

    # ex: /polls/question/1/
    path('question/<int:question_id>/', views.QuestionById.as_view(), name='question_by_id'),

    # ex: /polls/choice/
    path('choice/', views.ChoiceListCreate.as_view(), name='choice_list'),

    # ex: /polls/choice/3
    path('choice/<int:choice_id>/', views.ChoiceById.as_view(), name='choice_by_id'),

    # ex: /polls/question/<int:question_id>/choices
    path('question/<int:question_id>/choices', views.ChoiceByQuestionListCreate.as_view(), name='question_choices'),

    # ex: /polls/question/<int:question_id>/choices/nested
    path('question/<int:question_id>/choices/nested/', views.QuestionChoiceNested.as_view(), name='question_nested'),

    # ex: /polls/choice/<int:choice_id>/nested
    path('choice/<int:choice_id>/nested/', views.ChoiceNested.as_view(), name='choice_nested'),

]
