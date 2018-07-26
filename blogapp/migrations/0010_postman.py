# Generated by Django 2.0.6 on 2018-07-19 23:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogapp', '0009_auto_20180720_0139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=1000)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('draft', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='', width_field='width_field')),
                ('height_field', models.IntegerField(default=0, null=True)),
                ('width_field', models.IntegerField(default=0, null=True)),
                ('publish', models.DateField(null=True)),
                ('read_time', models.IntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
