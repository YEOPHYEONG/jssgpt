# Generated by Django 4.2.17 on 2024-12-14 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('langchain_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('industry', models.CharField(blank=True, max_length=255, null=True)),
                ('vision', models.TextField(blank=True, null=True)),
                ('mission', models.TextField(blank=True, null=True)),
                ('core_values', models.TextField(blank=True, null=True)),
                ('recent_achievements', models.TextField(blank=True, null=True)),
                ('key_issues', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('responsibilities', models.TextField(blank=True, null=True)),
                ('required_skills', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recruitment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='langchain_app.company')),
            ],
        ),
        migrations.DeleteModel(
            name='GeneratedData',
        ),
        migrations.AddField(
            model_name='jobinfo',
            name='recruitment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='langchain_app.recruitment'),
        ),
    ]
