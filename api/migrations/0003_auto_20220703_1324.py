# Generated by Django 3.2 on 2022-07-03 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_personaldata_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldata',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
