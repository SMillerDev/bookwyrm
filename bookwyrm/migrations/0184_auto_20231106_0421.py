# Generated by Django 3.2.20 on 2023-11-06 04:21

from django.db import migrations
from bookwyrm.models import User


def update_deleted_users(apps, schema_editor):
    """Find all the users who are deleted, not just inactive, and set deleted"""
    users = apps.get_model("bookwyrm", "User")
    db_alias = schema_editor.connection.alias
    users.objects.using(db_alias).filter(
        is_active=False,
        deactivation_reason__in=[
            "self_deletion",
            "moderator_deletion",
        ],
    ).update(is_deleted=True)

    # differente rules for remote users
    users.objects.using(db_alias).filter(is_active=False, local=False,).exclude(
        deactivation_reason="moderator_deactivation",
    ).update(is_deleted=True)


def erase_deleted_user_data(apps, schema_editor):
    """Retroactively clear user data"""
    for user in User.objects.filter(is_deleted=True):
        user.erase_user_data()
        user.save(
            broadcast=False,
            update_fields=["email", "avatar", "preview_image", "summary", "name"],
        )
        user.erase_user_statuses(broadcast=False)


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0183_auto_20231105_1607"),
    ]

    operations = [
        migrations.RunPython(
            update_deleted_users, reverse_code=migrations.RunPython.noop
        ),
        migrations.RunPython(
            erase_deleted_user_data, reverse_code=migrations.RunPython.noop
        ),
    ]
