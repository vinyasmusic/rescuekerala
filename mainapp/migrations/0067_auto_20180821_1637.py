# Generated by Django 2.1 on 2018-08-21 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0066_merge_20180821_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectioncenter',
            name='contacts',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Contacts - മൊബൈൽ'),
        ),
        migrations.AlterField(
            model_name='collectioncenter',
            name='district',
            field=models.CharField(blank=True, choices=[('alp', 'Alappuzha - ആലപ്പുഴ'), ('ekm', 'Ernakulam - എറണാകുളം'), ('idk', 'Idukki - ഇടുക്കി'), ('knr', 'Kannur - കണ്ണൂർ'), ('ksr', 'Kasaragod - കാസർഗോഡ്'), ('kol', 'Kollam - കൊല്ലം'), ('ktm', 'Kottayam - കോട്ടയം'), ('koz', 'Kozhikode - കോഴിക്കോട്'), ('mpm', 'Malappuram - മലപ്പുറം'), ('pkd', 'Palakkad - പാലക്കാട്'), ('ptm', 'Pathanamthitta - പത്തനംതിട്ട'), ('tvm', 'Thiruvananthapuram - തിരുവനന്തപുരം'), ('tcr', 'Thrissur - തൃശ്ശൂർ'), ('wnd', 'Wayanad - വയനാട്')], max_length=15, null=True, verbose_name='Ceter District - ജില്ല'),
        ),
        migrations.AlterField(
            model_name='collectioncenter',
            name='lsg_name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='LSG Name - സ്വയംഭരണ സ്ഥാപനത്തിന്റെ പേര്'),
        ),
        migrations.AlterField(
            model_name='collectioncenter',
            name='lsg_type',
            field=models.SmallIntegerField(blank=True, choices=[(0, 'Corporation'), (1, 'Municipality'), (2, 'Grama Panchayath')], null=True, verbose_name='LSG Type - തദ്ദേശ സ്വയംഭരണ സ്ഥാപനം'),
        ),
    ]
