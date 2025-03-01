# Generated by Django 4.2.17 on 2024-12-15 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('langchain_app', '0004_coverletterprompt_recruitjob_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='industry',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='recruitjob',
            name='key_roles',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recruitjob',
            name='related_technologies',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recruitment',
            name='custom_id',
            field=models.CharField(editable=False, max_length=255, null=True, unique=True),
        ),
    ]
