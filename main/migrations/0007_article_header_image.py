# Generated by Django 3.2.5 on 2022-06-19 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20220619_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='header_image',
            field=models.URLField(default='https://images.pexels.com/photos/270404/pexels-photo-270404.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'),
        ),
    ]
