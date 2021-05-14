# Generated by Django 3.1.6 on 2021-05-13 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('data', models.JSONField(null=True)),
            ],
            options={
                'ordering': ['-last_modified'],
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('sample', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='result', serialize=False, to='analysis.sample')),
                ('settings', models.JSONField(null=True)),
                ('radar_chart_params', models.JSONField(null=True)),
                ('parameters', models.JSONField(null=True)),
                ('nn_histogram', models.TextField(blank=True, help_text='html representation of the nn histogram plot')),
                ('poincare_plot', models.TextField(blank=True, help_text='html representation of the poincare plot')),
                ('lomb_plot', models.TextField(blank=True, help_text='html representation of the lomb plot')),
                ('dfa_plot', models.TextField(blank=True, help_text='html representation of dfa plot')),
                ('tachogram_plot', models.TextField(blank=True, help_text='html representation of tachogram plot')),
                ('fft_plot', models.TextField(blank=True, help_text='html representation of the fft plot')),
                ('radar_plot', models.TextField(blank=True, help_text='html radar plot representation of comparison between two samples')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='John Doe', max_length=150)),
                ('gender', models.CharField(blank=True, choices=[('male', 'M'), ('female', 'F')], default='male', max_length=20)),
                ('age', models.PositiveIntegerField(blank=True, default=18)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='sample',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='samples', to='analysis.subject'),
        ),
    ]
