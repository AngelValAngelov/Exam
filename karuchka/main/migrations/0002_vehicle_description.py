# Generated by Django 4.0.3 on 2022-04-20 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]