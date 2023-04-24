# Generated by Django 4.1.7 on 2023-02-24 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Multi_Form_Task_3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tagline', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='StudentData',
        ),
        migrations.DeleteModel(
            name='TeacherData',
        ),
    ]