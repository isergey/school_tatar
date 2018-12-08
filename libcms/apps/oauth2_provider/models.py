# coding=utf-8
import uuid
from django.db import models

from django.contrib.auth.models import User


class Application(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(verbose_name=u'Название приложения', max_length=255)
    url = models.URLField(verbose_name=u'URL приложения', max_length=512)
    description = models.TextField(verbose_name=u'Описание', max_length=1024, blank=True)
    skip_authorization = models.BooleanField(verbose_name=u'Пропустить авторизацию', default=False)
    callback = models.URLField(verbose_name=u'Callback URL', max_length=512)
    client_id = models.CharField(verbose_name=u'Идентификатор клиента', max_length=128, db_index=True, unique=True, editable=False)
    client_secret = models.CharField(verbose_name=u'Секретный ключ клиента', max_length=128, db_index=True, editable=False)

    class Meta:
        unique_together = ('owner', 'name')

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.client_id:
            self.client_id = generate_uuid()

        if not self.client_secret:
            self.client_secret = generate_uuid()
        super(Application, self).save(*args, **kwargs)


class AuthCode(models.Model):
    application = models.ForeignKey(Application)
    auth_user = models.ForeignKey(User)
    code = models.CharField(max_length=128, unique=True)
    created = models.DateTimeField(auto_now=True)
    expired = models.DateTimeField()

    class Meta:
        unique_together = ('application', 'code')

    def __unicode__(self):
        return u'%s: %s' % (self.application, self.code)


class AccessToken(models.Model):
    application = models.ForeignKey(Application)
    auth_user = models.ForeignKey(User)
    token = models.CharField(max_length=128, unique=True)
    created = models.DateTimeField(auto_now=True)
    expired = models.DateTimeField(null=True)

    def __unicode__(self):
        return u'%s: %s' % (self.application, self.token)

    class Meta:
        unique_together = ('application', 'auth_user')

def generate_uuid():
    return unicode(uuid.uuid4()).replace(u'-', '')