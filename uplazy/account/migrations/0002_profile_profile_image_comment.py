# Generated by Django 5.0.6 on 2024-05-23 11:00

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='profile-photo.jpg', null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('content', models.TextField(blank=True, max_length=500, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('artisan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='account.profile')),
                ('commenter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.profile')),
            ],
        ),
    ]
