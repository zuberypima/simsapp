# Generated by Django 4.1.7 on 2023-04-10 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='programreg',
            name='type',
            field=models.CharField(choices=[('BC', 'DEGREE'), ('OD', 'DIPLOMA')], default=0.001235788433020267, max_length=200),
            preserve_default=False,
        ),
    ]