# Generated by Django 3.0.5 on 2020-07-02 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200702_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titles',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='title', to='api.Categories'),
        ),
    ]