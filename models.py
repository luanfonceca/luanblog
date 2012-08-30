# encoding: utf-8
import datetime
from flask import url_for
from luanblog import *
from mongoengine import *


class Post(Document):
    created_at = DateTimeField(default=datetime.datetime.now, required=True)
    title = StringField(max_length=255, required=True)
    slug = StringField(max_length=255, required=True)
    body = StringField(required=True)
    comments = ListField(EmbeddedDocumentField('Comment'))

    def get_absolute_url(self):
        return url_for('post', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.title

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'slug'],
        'ordering': ['-created_at']
    }


class Comment(EmbeddedDocument):
    created_at = DateTimeField(default=datetime.datetime.now, required=True)
    body = StringField(verbose_name="Comment", required=True)
    author = StringField(verbose_name="Name", max_length=255, required=True)

    def __unicode__(self):
        return self.author