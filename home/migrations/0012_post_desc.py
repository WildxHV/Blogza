# Generated by Django 3.2.5 on 2022-01-20 07:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_post_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='desc',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
