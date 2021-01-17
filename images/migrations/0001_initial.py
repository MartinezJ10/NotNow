# Generated by Django 3.1.1 on 2020-11-30 21:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import images.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('alt', models.TextField(null=True)),
                ('image', models.ImageField(default='posts/default.jpg', upload_to=images.models.user_directory_path)),
                ('slug', models.SlugField(max_length=250, unique_for_date='created')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('active', 'Active'), ('deactivated', 'Deactivated')], default='active', max_length=11)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='images.category')),
            ],
        ),
    ]
