# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import participant_news.models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('show_avatar', models.BooleanField(default=False, verbose_name='\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u0430\u0432\u0430\u0442\u0430\u0440\u043a\u0443')),
                ('create_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f', db_index=True)),
                ('order', models.IntegerField(default=0, help_text='\u041d\u043e\u0432\u043e\u0441\u0442\u0438 \u0441\u043e\u0440\u0442\u0438\u0440\u0443\u044e\u0442\u0441\u044f \u043f\u043e \u043f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442\u0443, \u0434\u0430\u043b\u0435\u0435 - \u043f\u043e \u0434\u0430\u0442\u0435 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f. 0 - \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e.', verbose_name='\u041f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442', db_index=True)),
                ('publicated', models.BooleanField(default=True, db_index=True, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d\u043e?')),
                ('avatar_img_name', models.CharField(max_length=512, blank=True)),
                ('lang', models.CharField(default=(b'ru', b'Russian'), choices=[(b'ru', b'Russian'), (b'en', b'English'), (b'tt', b'Tatar')], max_length=2, help_text='\u041d\u043e\u0432\u043e\u0441\u0442\u044c \u043d\u0430 \u0441\u0430\u0439\u0442\u0435 \u043f\u043e\u044f\u0432\u0438\u0442\u0441\u044f \u043f\u0440\u0438 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0435\u043c \u044f\u0437\u044b\u043a\u0435', verbose_name='\u042f\u0437\u044b\u043a', db_index=True)),
                ('title', models.CharField(max_length=512, verbose_name='\u0417\u0430\u0433\u043b\u0430\u0432\u0438\u0435')),
                ('teaser', models.CharField(help_text='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0441\u0442\u0438', max_length=512, verbose_name='\u0422\u0438\u0437\u0435\u0440')),
                ('content', models.TextField(verbose_name='\u0421\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0441\u0442\u0438')),
                ('library', models.ForeignKey(related_name='participants_library', to='participants.Library')),
            ],
            options={
                'ordering': ['order', '-create_date'],
            },
        ),
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=participant_news.models.get_image_file_name, max_length=255, verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0444\u043e\u0442\u043e\u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u043e\u0432 \u043d\u043e\u0432\u043e\u0441\u0442\u0438')),
                ('order', models.IntegerField(default=0, verbose_name='\u041f\u043e\u0440\u044f\u0434\u043e\u043a')),
                ('is_show', models.BooleanField(default=True, verbose_name='\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u0444\u043e\u0442\u043e')),
                ('title', models.CharField(max_length=1024, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u043e\u0442\u043e', blank=True)),
                ('description', models.TextField(max_length=100000, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0444\u043e\u0442\u043e', blank=True)),
                ('news', models.ForeignKey(to='participant_news.News')),
            ],
            options={
                'ordering': ['-order'],
            },
        ),
    ]
