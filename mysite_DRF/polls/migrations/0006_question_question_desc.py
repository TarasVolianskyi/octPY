# Generated by Django 2.2 on 2020-11-01 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20201028_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_desc',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]