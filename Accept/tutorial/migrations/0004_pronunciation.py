# Generated by Django 4.2.1 on 2023-05-12 15:28

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0003_writingenglish'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pronunciation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
