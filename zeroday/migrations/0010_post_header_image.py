# Generated by Django 5.0.2 on 2024-04-07 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeroday', '0009_alter_post_body_alter_post_conclusion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='Images/'),
        ),
    ]
