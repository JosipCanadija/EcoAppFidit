# Generated by Django 4.2.7 on 2024-03-01 17:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EcoActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eco_name', models.CharField(max_length=50)),
                ('eco_summary', models.TextField()),
                ('eco_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=20)),
                ('org_lastname', models.CharField(max_length=20)),
                ('org_contact', models.EmailField(max_length=254)),
                ('org_companyID', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('user_lastname', models.CharField(max_length=20)),
                ('user_id', models.CharField(max_length=8)),
                ('user_acitiv', models.ManyToManyField(to='main.ecoactivity')),
            ],
        ),
        migrations.RemoveField(
            model_name='userecoaction',
            name='eco_action',
        ),
        migrations.RemoveField(
            model_name='userecoaction',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.CreateModel(
            name='GroupAssistant',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.user')),
                ('ass_task', models.CharField(max_length=30)),
                ('ass_done', models.BooleanField(default=False)),
                ('mentor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.organizer')),
            ],
        ),
        migrations.DeleteModel(
            name='EcoAction',
        ),
        migrations.DeleteModel(
            name='UserEcoAction',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.AddField(
            model_name='ecoactivity',
            name='eco_author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.organizer'),
        ),
    ]
