# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mptt.fields
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32, verbose_name='\u0420\u0430\u0439\u043e\u043d', db_index=True)),
            ],
            options={
                'verbose_name': '\u0420\u0430\u0439\u043e\u043d',
                'managed': False,
                'verbose_name_plural': '\u0420\u0430\u0439\u043e\u043d\u044b',
            },
        ),
        migrations.CreateModel(
            name='InteractionJournal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('records_created', models.IntegerField(default=0, verbose_name='\u0417\u0430\u043f\u0438\u0441\u0435\u0439 \u0441\u043e\u0437\u0434\u0430\u043d\u043e')),
                ('records_updated', models.IntegerField(default=0, verbose_name='\u0417\u0430\u043f\u0438\u0441\u0435\u0439 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u043e')),
                ('records_delete', models.IntegerField(default=0, verbose_name='\u0417\u0430\u043f\u0438\u0441\u0435\u0439 \u0443\u0434\u0430\u043b\u0435\u043d\u043e')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430/\u0432\u0440\u0435\u043c\u044f')),
            ],
            options={
                'verbose_name': '\u0417\u0430\u043f\u0438\u0441\u044c \u0436\u0443\u0440\u043d\u0430\u043b\u0430 \u0432\u0437\u0430\u0438\u043c\u043e\u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0439',
                'managed': False,
                'verbose_name_plural': '\u0417\u0430\u043f\u0438\u0441\u0438 \u0436\u0443\u0440\u043d\u0430\u043b\u0430 \u0432\u0437\u0430\u0438\u043c\u043e\u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0439',
            },
        ),
        migrations.CreateModel(
            name='InternetConnection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_exist', models.CharField(db_index=True, max_length=16, verbose_name='\u041d\u0430\u043b\u0438\u0447\u0438\u0435 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f', choices=[(b'none', '\u043d\u0435\u0442'), (b'gist', '\u0413\u0418\u0421\u0422'), (b'other', '\u043f\u0440\u043e\u0447\u0435\u0435')])),
                ('connection_type', models.CharField(db_index=True, max_length=16, verbose_name='\u0422\u0438\u043f \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f', choices=[(b'adsl', 'ADSL'), (b'vols', '\u0412\u041e\u041b\u0421'), (b'3g4g', '3G-4G')])),
                ('incoming_speed', models.IntegerField(default=0, verbose_name='\u0412\u0445\u043e\u0434\u044f\u0449\u0430\u044f \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c (\u041c\u0431/\u0441\u0435\u043a)')),
                ('outbound_speed', models.IntegerField(default=0, verbose_name='\u0418\u0441\u0445\u043e\u0434\u044f\u0449\u0430\u044f \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c (\u041c\u0431/\u0441\u0435\u043a)')),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hidden', models.BooleanField(default=False, db_index=True, verbose_name=b'\xd0\x9d\xd0\xb5 \xd0\xb2\xd1\x8b\xd0\xb2\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x82 \xd0\xb2 \xd1\x81\xd0\xbf\xd0\xb8\xd1\x81\xd0\xba\xd0\xb5 \xd0\xbd\xd0\xb0 \xd0\xbf\xd0\xbe\xd1\x80\xd1\x82\xd0\xb0\xd0\xbb\xd0\xb5')),
                ('name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('code', models.CharField(db_index=True, unique=True, max_length=32, verbose_name='\u0421\u0438\u0433\u043b\u0430', validators=[django.core.validators.RegexValidator(regex=b'^[/_\\-0-9A-Za-z]+$', message='\u0414\u043e\u043f\u0443\u0441\u043a\u0430\u044e\u0442\u0441\u044f \u0446\u0438\u0444\u0440\u044b, _, -, \u043b\u0430\u0442\u0438\u043d\u0441\u043a\u0438\u0435 \u0431\u0443\u043a\u0432\u044b')])),
                ('school_id', models.CharField(max_length=32, verbose_name='\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0448\u043a\u043e\u043b\u044b', blank=True)),
                ('sigla', models.TextField(help_text='\u041a\u0430\u0436\u0434\u0430\u044f \u0441\u0438\u0433\u043b\u0430 \u043d\u0430 \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u043e\u0439 \u0441\u0442\u0440\u043e\u043a\u0435', max_length=1024, verbose_name='\u0421\u0438\u0433\u043b\u0430 \u0438\u0437 \u043f\u043e\u0434\u043f\u043e\u043b\u044f 999b', db_index=True, blank=True)),
                ('staff_amount', models.IntegerField(verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432')),
                ('default_holder', models.BooleanField(default=False, help_text='\u0415\u0441\u043b\u0438 \u0441\u0438\u0433\u043b\u044b \u043d\u0435 \u0441\u043e\u0432\u043f\u0430\u0434\u0430\u044e\u0442 \u043d\u0438 \u0441 \u043e\u0434\u043d\u0438\u043c \u0444\u0438\u043b\u0438\u0430\u043b\u043e\u043c, \u0442\u043e \u0434\u0435\u0440\u0436\u0430\u0442\u0435\u043b\u0435\u043c \u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u0441\u044f \u044d\u0442\u043e\u0442', verbose_name='\u0414\u0435\u0440\u0436\u0430\u0442\u0435\u043b\u044c \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e')),
                ('republican', models.BooleanField(default=False, db_index=True, verbose_name='\u0420\u0443\u0441\u043f\u0443\u0431\u043b\u0438\u043a\u0430\u043d\u0441\u043a\u0430\u044f \u0431\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0430')),
                ('org_type', models.CharField(default=b'library', max_length=16, verbose_name='\u0422\u0438\u043f \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438', db_index=True, choices=[(b'library', '\u0411\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0430'), (b'school', '\u0428\u043a\u043e\u043b\u0430'), (b'participant', '\u0423\u0447\u0430\u0441\u0442\u043d\u0438\u043a'), (b'external', '\u0412\u043d\u0435\u0448\u043d\u044f\u044f')])),
                ('profile', models.TextField(max_length=10000, verbose_name='\u041f\u0440\u043e\u0444\u0438\u043b\u044c', blank=True)),
                ('phone', models.CharField(max_length=64, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d', blank=True)),
                ('plans', models.TextField(max_length=512, verbose_name='\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0440\u0430\u0431\u043e\u0442\u044b', blank=True)),
                ('postal_address', models.TextField(max_length=512, verbose_name='\u0410\u0434\u0440\u0435\u0441', blank=True)),
                ('http_service', models.URLField(max_length=255, verbose_name='\u0410\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u043d\u044b\u0439 \u0430\u0434\u0440\u0435\u0441 \u0441\u0430\u0439\u0442\u0430', blank=True)),
                ('ext_order_mail', models.EmailField(help_text='\u041d\u0430 \u0442\u043e\u0442 \u0430\u0434\u0440\u0435\u0441 \u0431\u0443\u0434\u0435\u0442 \u0432\u044b\u0441\u044b\u043b\u0430\u0442\u044c\u0441\u044f \u0437\u0430\u044f\u0432\u043a\u0430 \u043d\u0430 \u0431\u0440\u043e\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043e\u0442 \u0447\u0438\u0442\u0430\u0442\u0435\u043b\u044f', max_length=255, verbose_name='\u0410\u0434\u0440\u0435\u0441 \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u043e\u0439 \u043f\u043e\u0447\u0442\u044b \u0434\u043b\u044f \u0437\u0430\u043a\u0430\u0437\u0430', blank=True)),
                ('z_service', models.CharField(help_text='\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0430\u0434\u0440\u0435\u0441 Z \u0441\u0440\u0435\u0432\u0435\u0440\u0430 \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 host:port (\u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440 localhost:210)', max_length=255, verbose_name='\u0410\u0434\u0440\u0435\u0441 Z \u0441\u0435\u0440\u0432\u0435\u0440\u0430', blank=True)),
                ('ill_service', models.EmailField(max_length=255, verbose_name='\u0410\u0434\u0440\u0435\u0441 ILL \u0441\u0435\u0440\u0432\u0438\u0441\u0430', blank=True)),
                ('edd_service', models.EmailField(max_length=255, verbose_name='\u0410\u0434\u0440\u0435\u0441 \u042d\u0414\u0414 \u0441\u0435\u0440\u0432\u0438\u0441\u0430', blank=True)),
                ('mail', models.EmailField(max_length=255, null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441 \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u043e\u0439 \u043f\u043e\u0447\u0442\u044b', blank=True)),
                ('mail_access', models.CharField(max_length=255, verbose_name='\u0410\u0434\u0440\u0435\u0441 \u0441\u0435\u0440\u0432\u0435\u0440\u0430 \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u043e\u0439 \u043f\u043e\u0447\u0442\u044b', blank=True)),
                ('latitude', models.FloatField(db_index=True, null=True, verbose_name='\u0413\u0435\u043e\u0433\u0440\u0430\u0444\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0448\u0438\u0440\u043e\u0442\u0430', blank=True)),
                ('longitude', models.FloatField(db_index=True, null=True, verbose_name='\u0413\u0435\u043e\u0433\u0440\u0430\u0444\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0434\u043e\u043b\u0433\u043e\u0442\u0430', blank=True)),
                ('weight', models.IntegerField(default=100, verbose_name='\u041f\u043e\u0440\u044f\u0434\u043e\u043a \u0432\u044b\u0432\u043e\u0434\u0430 \u0432 \u0441\u043f\u0438\u0441\u043a\u0435', db_index=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
            ],
            options={
                'verbose_name': '\u0411\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0430',
                'verbose_name_plural': '\u0411\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0438',
                'managed': False,
                'permissions': (('add_cbs', 'Can create cbs'), ('change_cbs', 'Can change cbs'), ('delete_cbs', 'Can delete cbs')),
            },
        ),
        migrations.CreateModel(
            name='LibraryContentEditor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': '\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440 \u043a\u043e\u043d\u0442\u0435\u043d\u0442\u0430 \u0426\u0411\u0421',
                'verbose_name_plural': '\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440\u044b \u043a\u043e\u043d\u0442\u0435\u043d\u0442\u0430 \u0426\u0411\u0421',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LibraryType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64, verbose_name='\u0422\u0438\u043f \u0431\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0438')),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OracleConnection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True, verbose_name='\u0410\u043a\u0442\u0438\u0432\u043d\u043e')),
                ('connection_string', models.CharField(max_length=1024, verbose_name='\u0421\u0442\u0440\u043e\u043a\u0430 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f')),
                ('username', models.CharField(max_length=64, verbose_name='\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f', blank=True)),
                ('password', models.CharField(help_text='\u0415\u0441\u043b\u0438 \u043e\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u043f\u0443\u0441\u0442\u044b\u043c, \u0431\u0443\u0434\u0435\u0442 \u0434\u0435\u0439\u0441\u0442\u0432\u043e\u0432\u0430\u0442\u044c \u0441\u0442\u0430\u0440\u044b\u0439', max_length=64, verbose_name='\u041f\u0430\u0440\u043e\u043b\u044c', blank=True)),
                ('schema', models.CharField(max_length=64, verbose_name='\u0421\u0445\u0435\u043c\u0430 \u0434\u0430\u043d\u043d\u044b\u0445')),
                ('bib_databases', models.TextField(help_text='\u0418\u043c\u044f \u0431\u0430\u0437\u044b \u0441 \u043d\u043e\u0432\u043e\u0439 \u0441\u0442\u0440\u043e\u043a\u0438', max_length=1024, verbose_name='\u0421\u043f\u0438\u0441\u043e\u043a \u0431\u0438\u0431\u043b\u0438\u043e\u0433\u0440\u0430\u0444\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u0431\u0430\u0437 \u0434\u0430\u043d\u043d\u044b\u0445')),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserLibraryPosition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430',
                'managed': False,
                'verbose_name_plural': '\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u0438 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432',
            },
        ),
        migrations.CreateModel(
            name='WiFiPoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mac', models.CharField(max_length=17, validators=[django.core.validators.MinLengthValidator(limit_value=17)], help_text='\u041f\u0440\u0438\u043c\u0435\u0440: 84:80:2d:2b:be:b0', unique=True, verbose_name='MAC \u0430\u0434\u0440\u0435\u0441', db_index=True)),
                ('status', models.CharField(default=b'enabled', max_length=16, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441', db_index=True, choices=[(b'enabled', '\u0430\u043a\u0442\u0438\u0432\u043d\u0430'), (b'disabled', '\u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u0430')])),
                ('comments', models.TextField(max_length=10240, verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438', blank=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserLibrary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('middle_name', models.CharField(max_length=255, verbose_name='\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e')),
                ('birth_date', models.DateField(help_text=b'\xd0\xa4\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0\xd1\x82 \xd0\xb4\xd0\xb4.\xd0\xbc\xd0\xbc.\xd0\xb3\xd0\xb3\xd0\xb3\xd0\xb3', null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f', blank=True)),
                ('is_staff', models.BooleanField(default=False, verbose_name='\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b')),
                ('phone', models.CharField(max_length=32, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('disabled_person', models.BooleanField(default=False, verbose_name='\u041d\u0430\u043b\u0438\u0447\u0438\u0435 \u0438\u043d\u0432\u0430\u043b\u0438\u0434\u043d\u043e\u0441\u0442\u0438')),
                ('has_instructions_for_disabled', models.BooleanField(default=False, verbose_name='\u041f\u0440\u043e\u0448\u0435\u043b \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u0435 \u043f\u043e \u0443\u0441\u043b\u0443\u0433\u0430\u043c \u0438\u043d\u0432\u0430\u043b\u0438\u0434\u043d\u043e\u0441\u0442\u0438')),
                ('education', models.CharField(blank=True, max_length=64, verbose_name='\u041e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u0435', choices=[(b'vysshee', '\u0432\u044b\u0441\u0448\u0435\u0435'), (b'vysshee_bibl', '\u0432\u044b\u0441\u0448\u0435\u0435 \u0431\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u0447\u043d\u043e\u0435'), (b'srednee_prof', '\u043d\u0430\u0447\u0430\u043b\u044c\u043d\u043e\u0435 \u0438\u043b\u0438 \u0441\u0440\u0435\u0434\u043d\u0435\u0435 \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0435'), (b'srednee_prof_bibl', '\u043d\u0430\u0447\u0430\u043b\u044c\u043d\u043e\u0435 \u0438\u043b\u0438 \u0441\u0440\u0435\u0434\u043d\u0435\u0435 \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0435 \u0431\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u0447\u043d\u043e\u0435')])),
                ('work_experience', models.CharField(blank=True, max_length=64, verbose_name='\u0421\u0442\u0430\u0436 \u0440\u0430\u0431\u043e\u0442\u044b', choices=[(b'0_3', '\u043e\u0442 0 \u0434\u043e 3 \u043b\u0435\u0442'), (b'3_10', '\u043e\u0442 3 \u0434\u043e 10 \u043b\u0435\u0442'), (b'10', '\u0441\u0432\u044b\u0448\u0435 10')])),
                ('descendants_rights', models.BooleanField(default=False, verbose_name='\u041c\u043e\u0436\u0435\u0442 \u0443\u043f\u0440\u0430\u0432\u043b\u044f\u0442\u044c \u0434\u043e\u0447\u0435\u0440\u043d\u0438\u043c\u0438 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f\u043c\u0438')),
                ('is_active', models.BooleanField(default=True, help_text='\u0410\u043a\u0442\u0438\u0432\u0438\u0437\u0430\u0446\u0438\u044f \u043f\u043e\u043b\u043d\u043e\u043c\u043e\u0447\u0438\u0439 \u0440\u043e\u043b\u0435\u0439', verbose_name='\u0410\u043a\u0442\u0438\u0432\u0435\u043d')),
                ('department', mptt.fields.TreeForeignKey(verbose_name='\u041e\u0442\u0434\u0435\u043b', to='participants.Department')),
                ('library', models.ForeignKey(to='participants.Library')),
                ('position', models.ForeignKey(verbose_name='\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c', to='participants.UserLibraryPosition')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438',
                'verbose_name_plural': '\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0439',
            },
        ),
        migrations.AlterUniqueTogether(
            name='userlibrary',
            unique_together=set([('library', 'user')]),
        ),
    ]
