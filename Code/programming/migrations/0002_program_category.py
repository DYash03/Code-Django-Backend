# Generated by Django 3.0.5 on 2020-05-29 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programming', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='category',
            field=models.CharField(choices=[('String', 'STRING'), ('Array', 'ARRAY'), ('List', 'LIST'), ('Stack', 'STACK'), ('Queue', 'QUEUE'), ('Linked List', 'LINKED LIST'), ('Tree', 'TREE'), ('Others', 'OTHERS')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]
