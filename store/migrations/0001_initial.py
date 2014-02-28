# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table(u'store_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'store', ['Author'])

        # Adding model 'Book'
        db.create_table(u'store_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'store', ['Book'])

        # Adding model 'Genre'
        db.create_table(u'store_genre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'store', ['Genre'])


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table(u'store_author')

        # Deleting model 'Book'
        db.delete_table(u'store_book')

        # Deleting model 'Genre'
        db.delete_table(u'store_genre')


    models = {
        u'store.author': {
            'Meta': {'object_name': 'Author'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'store.book': {
            'Meta': {'object_name': 'Book'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'store.genre': {
            'Meta': {'object_name': 'Genre'},
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['store']