# Generated by Django 4.1 on 2022-08-23 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_email_creation_date_alter_email_email_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='email_score',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
