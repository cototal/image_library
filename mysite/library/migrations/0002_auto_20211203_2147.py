# Generated by Django 3.2.9 on 2021-12-04 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='category',
            field=models.CharField(db_index=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='image',
            name='path',
            field=models.CharField(db_index=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='imagetag',
            name='name',
            field=models.CharField(db_index=True, max_length=250),
        ),
    ]