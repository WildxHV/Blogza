# Generated by Django 3.2.5 on 2022-01-27 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_alter_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]