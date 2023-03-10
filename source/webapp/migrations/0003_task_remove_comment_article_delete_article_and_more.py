# Generated by Django 4.1.6 on 2023-02-23 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('description', models.TextField(max_length=3000, verbose_name='Описание')),
                ('status', models.CharField(max_length=200, verbose_name='Статус')),
                ('completion_date', models.DateField(auto_now=True, verbose_name='Выполнить до')),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='article',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
