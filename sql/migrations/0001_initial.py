# Generated by Django 3.1.13 on 2021-11-29 11:35

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mirage.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuditEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(verbose_name='用户ID')),
                ('user_name', models.CharField(max_length=255, null=True, verbose_name='用户名称')),
                ('action', models.CharField(max_length=255, verbose_name='动作')),
                ('ip', models.GenericIPAddressField(null=True, verbose_name='IP')),
                ('action_time', models.DateTimeField(auto_now_add=True, verbose_name='操作时间')),
            ],
            options={
                'verbose_name': '审计日志',
                'verbose_name_plural': '审计日志',
                'db_table': 'audit_log',
                'managed': True,
            },
        ),
    ]
