# Generated by Django 4.0.4 on 2022-07-05 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0002_alter_designslid_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='designslid',
            name='id',
        ),
        migrations.AddField(
            model_name='designslid',
            name='design_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
