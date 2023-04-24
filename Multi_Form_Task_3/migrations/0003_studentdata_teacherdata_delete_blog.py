# Generated by Django 4.1.7 on 2023-02-24 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Multi_Form_Task_3', '0002_blog_delete_studentdata_delete_teacherdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('standard', models.CharField(max_length=100)),
                ('section', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ClassTeacherOF', models.CharField(max_length=100)),
                ('Salary', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]