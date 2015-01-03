# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('votes', models.IntegerField(default=0)),
                ('votesCons', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=100)),
                ('topic', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=500)),
                ('parent', models.ForeignKey(blank=True, to='main.Comment', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mesh',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('meshFile', models.FileField(upload_to=b'meshes')),
                ('public', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('scriptFile', models.FileField(upload_to=b'scripts')),
                ('public', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profileType', models.CharField(default=b'ST', max_length=2, choices=[(b'ST', b'standard'), (b'AD', b'advanced')])),
                ('usrData', models.OneToOneField(related_name='user_data', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Visualization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('visualizationFile', models.FileField(upload_to=b'visualizations')),
                ('public', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(to='main.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='script',
            name='owner',
            field=models.ForeignKey(to='main.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mesh',
            name='owner',
            field=models.ForeignKey(to='main.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='writter',
            field=models.ForeignKey(to='main.UserProfile'),
            preserve_default=True,
        ),
    ]
