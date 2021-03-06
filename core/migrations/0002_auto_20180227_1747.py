# Generated by Django 2.0.1 on 2018-02-27 17:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
            ],
        ),
        migrations.AddField(
            model_name='bet',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Category'),
        ),
        migrations.AlterUniqueTogether(
            name='bet',
            unique_together={('user', 'category')},
        ),
    ]
