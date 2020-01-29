# Generated by Django 3.0.2 on 2020-01-28 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200128_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='seccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Section'),
        ),
        migrations.AlterField(
            model_name='section',
            name='condition',
            field=models.CharField(choices=[('maestro', 'maestro'), ('secundaria', 'estudiante de secundaria'), ('cch', 'estudiante de cch')], default='1', max_length=30),
        ),
    ]