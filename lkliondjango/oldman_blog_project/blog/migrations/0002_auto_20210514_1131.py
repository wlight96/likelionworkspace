# Generated by Django 3.2.2 on 2021-05-14 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notice',
            name='student_code',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
