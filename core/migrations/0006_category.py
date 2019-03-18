# Generated by Django 2.1.7 on 2019-03-18 16:11

from django.db import migrations, models
import slugger.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190315_1724'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slugger', slugger.fields.AutoSlugField(blank=True, null=True, populate_from='title', unique=True)),
            ],
        ),
    ]
