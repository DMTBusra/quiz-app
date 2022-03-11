from django.db import models

class Category(models.Model):
    CATEGORY_CHOICES=[
    ("Frontend", 'Frontend'),
    ("Backend", 'Backend'),
    ("Aws", 'Aws'),
    ("Cyber", 'Cyber')
]
    
    name=models.CharField(max_length=10, choices=CATEGORY_CHOICES,blank=True)
    def __str__(self):
        return self.name 
    
class Quiz(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE ,related_name="quizzes")
    title=models.CharField(max_length=30)
    createDate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return  f'{self.category} {self.title}'
class Question(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name="questions")
    question=models.CharField(max_length=20)
    createDate = models.DateTimeField(auto_now_add=True)
    upDatedDate=models.DateTimeField(auto_now=True)
    DIFFICULTIES=[
        ("HARD", 'HARD'),
        ("MEDIUM", 'MEDIUM'),
        ("SOFT", 'SOFT'),
    ]
    dificulty = models.CharField(max_length=15, choices=DIFFICULTIES)
    def __str__(self):
        return  f'{self.quiz} {self.question}'
    
class Answer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE ,related_name="answers")
    upDatedDate=models.DateTimeField(auto_now=True)
    createDate = models.DateTimeField(auto_now_add=True)
    answer_text=models.CharField(max_length=40)
    is_right=models.BooleanField(default=False)
    
    def __str__(self):
        return  f'{self.question} {self.answer_text}'