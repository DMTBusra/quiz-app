from django.urls import path
from .views import AnswerRead, QuizList,QuizRead,AnswerRead
urlpatterns =[
     path("",QuizList.as_view(),name="quizlist"),
     
     path("<category>/",QuizRead.as_view(),name="quizread"),
     path("<category>/<quiz>/",AnswerRead.as_view(),name="answerread"),
    ]
