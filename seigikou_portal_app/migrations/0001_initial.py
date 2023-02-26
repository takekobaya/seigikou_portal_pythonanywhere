# Generated by Django 3.1.2 on 2022-02-04 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bumon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Bumon',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventcode', models.CharField(blank=True, max_length=7, null=True)),
                ('day', models.DateField()),
                ('starttime', models.TimeField()),
                ('endtime', models.TimeField()),
                ('location', models.CharField(blank=True, max_length=20, null=True)),
                ('name', models.CharField(max_length=50)),
                ('public', models.CharField(blank=True, max_length=20, null=True)),
                ('contents', models.TextField(blank=True, max_length=512, null=True)),
                ('question_url', models.URLField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'Event',
            },
        ),
        migrations.CreateModel(
            name='Kaiin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Kaiin',
            },
        ),
        migrations.CreateModel(
            name='Mlmemb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Mlmemb',
            },
        ),
        migrations.CreateModel(
            name='Shikaku',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Shikaku',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membercode', models.CharField(blank=True, max_length=4, null=True)),
                ('name', models.CharField(max_length=20)),
                ('honbu', models.CharField(blank=True, max_length=20, null=True)),
                ('pref', models.CharField(blank=True, max_length=20, null=True)),
                ('company', models.CharField(blank=True, max_length=20, null=True)),
                ('senmon', models.CharField(blank=True, max_length=50, null=True)),
                ('bukai', models.CharField(blank=True, max_length=20, null=True)),
                ('other', models.CharField(blank=True, max_length=256, null=True)),
                ('bumon', models.ManyToManyField(blank=True, related_name='bumon', to='seigikou_portal_app.Bumon')),
                ('kaiin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='kaiin', to='seigikou_portal_app.kaiin')),
                ('mlmemb', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='mlmemb', to='seigikou_portal_app.mlmemb')),
                ('shikaku', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='seigikou_portal_app.shikaku')),
            ],
            options={
                'db_table': 'Member',
            },
        ),
        migrations.CreateModel(
            name='Kouen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kouencode', models.CharField(blank=True, max_length=7, null=True)),
                ('name', models.CharField(max_length=256)),
                ('youshi', models.TextField(blank=True, max_length=512, null=True)),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='kouen', to='seigikou_portal_app.event')),
                ('koushi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Member', to='seigikou_portal_app.member')),
            ],
            options={
                'db_table': 'Kouen',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='member',
            field=models.ManyToManyField(blank=True, related_name='Members', to='seigikou_portal_app.Member'),
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('account_image', models.ImageField(blank=True, upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]