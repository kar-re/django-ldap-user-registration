# Generated by Django 2.0.6 on 2018-07-17 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dl_user', '0006_userregistrationrecord_ldap_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregistrationrecord',
            name='department',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
