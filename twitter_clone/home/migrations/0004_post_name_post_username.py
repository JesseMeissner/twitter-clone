# Generated by Django 4.1.3 on 2022-11-08 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_post_name_remove_post_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(db_index=True, default='Anonymous', max_length=40, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='post',
            name='username',
            field=models.CharField(db_index=True, default='Anonymous', max_length=30, verbose_name='Username'),
        ),
    ]