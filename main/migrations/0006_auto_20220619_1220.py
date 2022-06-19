# Generated by Django 3.2.5 on 2022-06-19 11:20

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_merge_20220617_1156'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date_created']},
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('Javascript', 'Javascript'), ('Python', 'Python'), ('CSS', 'CSS'), ('HTML', 'HTML')], max_length=10),
        ),
    ]
