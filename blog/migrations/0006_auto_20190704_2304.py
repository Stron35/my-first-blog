# Generated by Django 2.2.2 on 2019-07-04 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190704_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ImageField(blank=True, default='', upload_to='media/post_images/'),
            preserve_default=False,
        ),
    ]