# Generated by Django 3.2.8 on 2022-03-18 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_dayhistoryuserinfo_target_kcal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayhistoryuserinfo',
            name='target_kcal',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]