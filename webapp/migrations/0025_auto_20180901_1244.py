# Generated by Django 2.0.8 on 2018-09-01 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0024_auto_20180901_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='zona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.Zona'),
        ),
    ]
