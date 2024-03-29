# Generated by Django 2.2.2 on 2019-07-10 20:13

import blog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190707_2244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='images',
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=150),
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=blog.models.generate_image_path, verbose_name='Image')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
            ],
        ),
    ]
