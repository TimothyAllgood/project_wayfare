# Generated by Django 3.1 on 2020-08-07 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20200807_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(default='bio', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='dark_mode',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(choices=[('S', 'San Francisco'), ('L', 'London'), ('C', 'Chicago'), ('N', 'New York'), ('A', 'Austin')], default='S', max_length=1, verbose_name='City Choice'),
        ),
    ]
