# Generated by Django 4.1 on 2022-08-23 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_email_email_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='valid_email',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
    ]