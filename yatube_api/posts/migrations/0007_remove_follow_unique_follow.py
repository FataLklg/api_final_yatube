# Generated by Django 3.2.14 on 2022-07-28 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_follow_unique_follow'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_follow',
        ),
    ]
