# Generated by Django 2.2.16 on 2022-05-19 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_title_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
