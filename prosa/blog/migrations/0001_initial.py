# Generated by Django 3.1.6 on 2021-02-12 21:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('excerpt', models.TextField(max_length=500, null=True)),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish_date')),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.TextField(max_length=5000)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-publish_date',),
            },
            managers=[
                ('newmanager', django.db.models.manager.Manager()),
            ],
        ),
    ]
