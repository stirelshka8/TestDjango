# Generated by Django 4.2.4 on 2023-08-18 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('invite_code', models.CharField(blank=True, max_length=10, null=True)),
                ('used_invite_codes', models.ManyToManyField(blank=True, related_name='invited_by', to='phone_auth_app.userprofile')),
            ],
        ),
    ]