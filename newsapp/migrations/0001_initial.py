# Generated by Django 3.1.7 on 2021-05-04 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('News_Name', models.TextField()),
                ('News_Info', models.TextField()),
                ('News_Content', models.TextField()),
                ('Destination_Image', models.ImageField(upload_to='images/')),
                ('Date_Published', models.TextField()),
                ('News_Url', models.TextField()),
            ],
            options={
                'db_table': 'news1',
            },
        ),
    ]
