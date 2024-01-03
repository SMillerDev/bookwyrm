# Generated by Django 3.2.20 on 2023-10-27 11:22

import bookwyrm.models.activitypub_mixin
import bookwyrm.models.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0181_merge_20230806_2302"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="also_known_as",
            field=bookwyrm.models.fields.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name="user",
            name="moved_to",
            field=bookwyrm.models.fields.RemoteIdField(
                max_length=255,
                null=True,
                validators=[bookwyrm.models.fields.validate_remote_id],
            ),
        ),
        migrations.AlterField(
            model_name="notification",
            name="notification_type",
            field=models.CharField(
                choices=[
                    ("FAVORITE", "Favorite"),
                    ("REPLY", "Reply"),
                    ("MENTION", "Mention"),
                    ("TAG", "Tag"),
                    ("FOLLOW", "Follow"),
                    ("FOLLOW_REQUEST", "Follow Request"),
                    ("BOOST", "Boost"),
                    ("IMPORT", "Import"),
                    ("ADD", "Add"),
                    ("REPORT", "Report"),
                    ("LINK_DOMAIN", "Link Domain"),
                    ("INVITE", "Invite"),
                    ("ACCEPT", "Accept"),
                    ("JOIN", "Join"),
                    ("LEAVE", "Leave"),
                    ("REMOVE", "Remove"),
                    ("GROUP_PRIVACY", "Group Privacy"),
                    ("GROUP_NAME", "Group Name"),
                    ("GROUP_DESCRIPTION", "Group Description"),
                    ("MOVE", "Move"),
                ],
                max_length=255,
            ),
        ),
        migrations.CreateModel(
            name="Move",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                (
                    "remote_id",
                    bookwyrm.models.fields.RemoteIdField(
                        max_length=255,
                        null=True,
                        validators=[bookwyrm.models.fields.validate_remote_id],
                    ),
                ),
                ("object", bookwyrm.models.fields.CharField(max_length=255)),
                (
                    "origin",
                    bookwyrm.models.fields.CharField(
                        blank=True, default="", max_length=255, null=True
                    ),
                ),
                (
                    "user",
                    bookwyrm.models.fields.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(bookwyrm.models.activitypub_mixin.ActivityMixin, models.Model),
        ),
        migrations.CreateModel(
            name="MoveUser",
            fields=[
                (
                    "move_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="bookwyrm.move",
                    ),
                ),
                (
                    "target",
                    bookwyrm.models.fields.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="move_target",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("bookwyrm.move",),
        ),
    ]