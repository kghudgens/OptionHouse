# Generated by Django 3.1.4 on 2020-12-31 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('optionhouseapp', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
    ]
