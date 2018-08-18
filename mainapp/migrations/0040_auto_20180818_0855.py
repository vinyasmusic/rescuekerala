# Generated by Django 2.1 on 2018-08-18 03:25

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0039_auto_20180818_0328'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='additional_phone_numbers',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=[], size=None, verbose_name='Additional phone numbers separated by space - അധിക ഫോൺ നമ്പർ സ്പെയ്സ് കൊണ്ട് വേർതിരിച്ചിരിക്കുന്നു'),
        ),
        migrations.AlterField(
            model_name='request',
            name='is_request_for_others',
            field=models.BooleanField(default=False, help_text='If it is enabled, no need to consider lat and lng', verbose_name='Requesting for others - മറ്റൊരാൾക്ക് വേണ്ടി അപേക്ഷിക്കുന്നു  '),
        ),
    ]
