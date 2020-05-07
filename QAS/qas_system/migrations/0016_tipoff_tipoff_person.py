# Generated by Django 3.0.5 on 2020-05-07 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qas_system', '0015_remove_tipoff_tipoff_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipoff',
            name='tipoff_person',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tipoffs', to='qas_system.User', verbose_name='举报者'),
            preserve_default=False,
        ),
    ]