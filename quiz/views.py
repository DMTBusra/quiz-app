from .models import Category,Quiz,Question
from .serializers import  CategorySerializer, QuestionSerializer, QuizSerializer
from rest_framework import generics
class QuizList(generics.ListAPIView):
    queryset=Category.objects.all()
    serializer_class =CategorySerializer
    
    
class QuizRead(generics.ListAPIView):
    queryset=Quiz.objects.all()
    serializer_class=QuizSerializer
    
    def get_queryset(self):
        category=self.kwargs["category"].capitalize()
        return Quiz.objects.filter(category__name=category)
class AnswerRead(generics.ListAPIView):
    queryset=Question.objects.all()
    serializer_class=QuestionSerializer
    
    def get_queryset(self):
        quiz=self.kwargs["quiz"].capitalize()
        return Question.objects.filter(quiz__title=quiz)
    