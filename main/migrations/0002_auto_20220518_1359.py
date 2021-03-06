# Generated by Django 2.2.12 on 2022-05-18 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=255, verbose_name='Email почта'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='number_of_telephone',
            field=models.CharField(max_length=255, verbose_name='Number Phone'),
        ),
    ]
