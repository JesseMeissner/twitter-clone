# Generated by Django 4.1.3 on 2022-11-08 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_post_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="static/", verbose_name="Image"
            ),
        ),
    ]
