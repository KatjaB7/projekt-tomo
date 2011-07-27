# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Problem.status'
        db.delete_column('problem_problem', 'status')

        # Renaming field 'Problem.trial' to 'Problem.preamble'
        db.rename_column('problem_problem', 'trial', 'preamble')


    def backwards(self, orm):
        
        # Adding field 'Problem.status'
        db.add_column('problem_problem', 'status', self.gf('django.db.models.fields.CharField')(default='10', max_length=2), keep_default=False)

        # Renaming field 'Problem.preamble' to 'Problem.trial'
        db.rename_column('problem_problem', 'preamble', 'trial')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'problem.collection': {
            'Meta': {'ordering': "['id']", 'object_name': 'Collection'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '70'}),
            'problems': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'collections'", 'symmetrical': 'False', 'to': "orm['problem.Problem']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'10'", 'max_length': '2'})
        },
        'problem.part': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'Part'},
            '_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'answers': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'problem': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'parts'", 'to': "orm['problem.Problem']"}),
            'solution': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'trial': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'problem.problem': {
            'Meta': {'ordering': "['name']", 'object_name': 'Problem'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '70'}),
            'preamble': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'problem.solution': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'Solution'},
            '_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'correct': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'part': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'solutions'", 'to': "orm['problem.Part']"}),
            'start': ('django.db.models.fields.IntegerField', [], {}),
            'submission': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'solutions'", 'to': "orm['problem.Submission']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'solutions'", 'to': "orm['auth.User']"})
        },
        'problem.submission': {
            'Meta': {'ordering': "['-timestamp']", 'object_name': 'Submission'},
            'download_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.TextField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'upload_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'submissions'", 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['problem']
