# Generated by Django 2.0.1 on 2018-02-11 07:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('att_app', '0002_auto_20180211_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_attendance',
            name='st_id',
            field=models.ForeignKey(limit_choices_to={'is_staff': False}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='student_details',
            name='st_id',
            field=models.ForeignKey(limit_choices_to={'is_staff': False}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='teacher_details',
            name='t_id',
            field=models.ForeignKey(limit_choices_to={'is_staff': False}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
