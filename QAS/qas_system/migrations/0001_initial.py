# Generated by Django 3.0.5 on 2020-04-13 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='科目名称')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30, verbose_name='用户名')),
                ('password', models.CharField(max_length=30, verbose_name='密码')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_title', models.CharField(max_length=30, verbose_name='标题')),
                ('question_text', models.TextField(verbose_name='具体描述')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='提问日期')),
                ('page_views', models.IntegerField(default=0, verbose_name='浏览量')),
                ('good_num', models.IntegerField(default=0, verbose_name='点赞量')),
                ('question_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qas_system.Subject', verbose_name='科目')),
                ('questioner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qas_system.User', verbose_name='提问者')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(verbose_name='评论内容')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='评论时间')),
                ('good_num', models.IntegerField(default=0, verbose_name='点赞量')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qas_system.Question', verbose_name='问题')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qas_system.User', verbose_name='评论者')),
            ],
        ),
    ]
