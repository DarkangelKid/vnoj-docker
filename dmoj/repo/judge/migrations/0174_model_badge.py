# Generated by Django 2.2.24 on 2022-03-29 16:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0173_add_view_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='badge name')),
                ('mini', models.URLField(blank=True, verbose_name='mini badge URL')),
                ('full_size', models.URLField(blank=True, verbose_name='full size badge URL')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='badges',
            field=models.ManyToManyField(blank=True, related_name='users', to='judge.Badge', verbose_name='badges'),
        ),
        migrations.AddField(
            model_name='profile',
            name='display_badge',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='judge.Badge', verbose_name='display badge'),
        ),
    ]
