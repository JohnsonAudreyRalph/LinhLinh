# Generated by Django 4.2.2 on 2023-11-14 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student_Management', '0013_alter_k56dvt_image_alter_new_act_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='k56dvt',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='model_file',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='model_post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='new_act',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
