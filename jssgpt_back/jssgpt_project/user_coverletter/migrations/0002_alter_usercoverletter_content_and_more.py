# Generated by Django 4.2.17 on 2024-12-22 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_experience', '0003_alter_rawexperience_user'),
        ('user_coverletter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercoverletter',
            name='content',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.RemoveField(
            model_name='usercoverletter',
            name='recommended_starexperience',
        ),
        migrations.AddField(
            model_name='usercoverletter',
            name='recommended_starexperience',
            field=models.ManyToManyField(blank=True, related_name='recommended_cover_letters', to='user_experience.starexperience'),
        ),
    ]
