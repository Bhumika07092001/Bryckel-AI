# Generated by Django 5.0.4 on 2024-04-25 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_rename_name_item_content_item_created_at_item_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='created_At',
        ),
    ]