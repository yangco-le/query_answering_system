# Generated by Django 3.0.5 on 2020-05-09 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qas_system', '0016_tipoff_tipoff_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='collect_question',
            field=models.ManyToManyField(to='qas_system.Question'),
        ),
    ]
