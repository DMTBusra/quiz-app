# Generated by Django 4.0.2 on 2022-03-11 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('Frontend', 'Frontend'), ('Backend', 'Backend'), ('Aws', 'Aws'), ('Cyber', 'Cyber')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to='quiz.category')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=20)),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('upDatedDate', models.DateTimeField(auto_now=True)),
                ('dificulty', models.CharField(choices=[('HARD', 'HARD'), ('MEDIUM', 'MEDIUM'), ('SOFT', 'SOFT')], max_length=15)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='quiz.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upDatedDate', models.DateTimeField(auto_now=True)),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('answer_text', models.CharField(max_length=40)),
                ('is_right', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='quiz.question')),
            ],
        ),
    ]
