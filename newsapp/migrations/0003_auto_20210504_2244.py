# Generated by Django 3.1.7 on 2021-05-04 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0002_auto_20210504_2134'),
    ]

    operations = [
        migrations.CreateModel(
            name='entertain_news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('News_Name', models.TextField()),
                ('News_Info', models.TextField()),
                ('News_Content', models.TextField()),
                ('Destination_Image', models.TextField()),
                ('Date_Published', models.TextField()),
                ('News_Url', models.TextField()),
            ],
            options={
                'db_table': 'entertain',
            },
        ),
        migrations.CreateModel(
            name='general_news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('News_Name', models.TextField()),
                ('News_Info', models.TextField()),
                ('News_Content', models.TextField()),
                ('Destination_Image', models.TextField()),
                ('Date_Published', models.TextField()),
                ('News_Url', models.TextField()),
            ],
            options={
                'db_table': 'general',
            },
        ),
        migrations.CreateModel(
            name='sports_news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('News_Name', models.TextField()),
                ('News_Info', models.TextField()),
                ('News_Content', models.TextField()),
                ('Destination_Image', models.TextField()),
                ('Date_Published', models.TextField()),
                ('News_Url', models.TextField()),
            ],
            options={
                'db_table': 'sports',
            },
        ),
        migrations.CreateModel(
            name='technology_news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('News_Name', models.TextField()),
                ('News_Info', models.TextField()),
                ('News_Content', models.TextField()),
                ('Destination_Image', models.TextField()),
                ('Date_Published', models.TextField()),
                ('News_Url', models.TextField()),
            ],
            options={
                'db_table': 'technology',
            },
        ),
        migrations.RenameModel(
            old_name='News',
            new_name='business_news',
        ),
        migrations.AlterModelTable(
            name='business_news',
            table='business',
        ),
    ]
