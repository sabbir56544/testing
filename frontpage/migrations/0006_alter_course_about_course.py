# Generated by Django 3.2.7 on 2021-09-09 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0005_auto_20210910_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='about_course',
            field=models.TextField(blank=True, null=True),
        ),
    ]
