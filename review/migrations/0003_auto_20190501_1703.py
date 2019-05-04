# Generated by Django 2.1.7 on 2019-05-01 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_auto_20190501_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='department',
            field=models.CharField(choices=[('CSE', 'Computer Science'), ('ISE', 'Information Science'), ('ECE', 'Electronics and Communication'), ('EEE', 'Electrical and Electronics'), ('ME', 'Mechanical'), ('CE', 'Civil'), ('TC', 'Telecommunication'), ('BT', 'Biotechnology')], max_length=2),
        ),
    ]
