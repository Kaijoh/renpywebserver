# Generated by Django 4.1.5 on 2023-03-22 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='score',
            old_name='PlayerName',
            new_name='player_name',
        ),
        migrations.RemoveField(
            model_name='score',
            name='PlayerScore',
        ),
        migrations.AddField(
            model_name='score',
            name='player_score',
            field=models.IntegerField(default=0),
        ),
    ]
