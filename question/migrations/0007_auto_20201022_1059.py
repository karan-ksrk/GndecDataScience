# Generated by Django 3.1.2 on 2020-10-22 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0006_question_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]