# Generated by Django 2.2.2 on 2019-07-04 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190704_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='post_images/'),
        ),
    ]
