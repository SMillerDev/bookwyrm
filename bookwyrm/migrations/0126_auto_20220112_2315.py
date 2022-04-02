# Generated by Django 3.2.10 on 2022-01-12 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0125_alter_user_preferred_language"),
    ]

    operations = [
        migrations.AlterField(
            model_name="annualgoal",
            name="privacy",
            field=models.CharField(
                choices=[
                    ("public", "Public"),
                    ("unlisted", "Unlisted"),
                    ("followers", "Followers"),
                    ("direct", "Private"),
                ],
                default="public",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="importjob",
            name="privacy",
            field=models.CharField(
                choices=[
                    ("public", "Public"),
                    ("unlisted", "Unlisted"),
                    ("followers", "Followers"),
                    ("direct", "Private"),
                ],
                default="public",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="default_post_privacy",
            field=models.CharField(
                choices=[
                    ("public", "Public"),
                    ("unlisted", "Unlisted"),
                    ("followers", "Followers"),
                    ("direct", "Private"),
                ],
                default="public",
                max_length=255,
            ),
        ),
    ]