# Generated by Django 2.0.7 on 2018-07-29 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180729_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('not-specified', 'Not-specified'), ('female', 'Female')], max_length=80, null=True),
        ),
    ]