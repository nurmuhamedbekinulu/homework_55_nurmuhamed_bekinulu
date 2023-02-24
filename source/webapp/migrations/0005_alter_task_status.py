# Generated by Django 4.1.7 on 2023-02-24 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_task_completion_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('new', 'Новая'), ('in process', 'В процессе'), ('done', 'Сделано')], default='new', max_length=200, verbose_name='Статус'),
        ),
    ]
