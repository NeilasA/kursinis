# Generated by Django 3.1.5 on 2021-01-17 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_auto_20210117_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('active', 'active'), ('raised', 'raised'), ('archived', 'archived')], default='active', max_length=20),
        ),
    ]
