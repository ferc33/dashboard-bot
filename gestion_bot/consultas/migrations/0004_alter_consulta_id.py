# Generated by Django 5.1 on 2024-08-22 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0003_consulta_airtable_id_alter_consulta_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
