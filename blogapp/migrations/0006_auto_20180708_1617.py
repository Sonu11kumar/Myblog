# Generated by Django 2.0.6 on 2018-07-08 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='height_field',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='width_field',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
