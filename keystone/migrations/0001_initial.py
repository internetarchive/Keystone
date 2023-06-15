# Generated by Django 4.2.2 on 2023-06-15 05:49

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "role",
                    models.CharField(
                        choices=[("ADMIN", "Admin"), ("USER", "User")],
                        default="USER",
                        max_length=16,
                    ),
                ),
            ],
            options={
                "permissions": [("change_role", "Can change user roles")],
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("max_users", models.PositiveIntegerField(default=1)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="ArchQuota",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("object_id", models.PositiveBigIntegerField()),
                ("quota_input_bytes", models.PositiveBigIntegerField()),
                ("quota_output_bytes", models.PositiveBigIntegerField()),
                ("quota_download_bytes", models.PositiveBigIntegerField()),
                ("quota_dom", models.PositiveSmallIntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Collection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "collection_type",
                    models.CharField(
                        choices=[
                            ("AIT", "AIT"),
                            ("SPECIAL", "Special"),
                            ("CUSTOM", "Custom"),
                        ],
                        max_length=16,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="JobComplete",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("input_bytes", models.PositiveBigIntegerField()),
                ("output_bytes", models.PositiveBigIntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="JobStart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("estimated_input_bytes", models.PositiveBigIntegerField()),
                ("parameters", models.JSONField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="JobType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("version", models.CharField(max_length=255)),
                ("can_run", models.BooleanField()),
                ("can_publish", models.BooleanField()),
                ("input_quota_eligible", models.BooleanField()),
                ("output_quota_eligible", models.BooleanField()),
                ("download_quota_eligible", models.BooleanField()),
                ("display_name", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="keystone.account",
                    ),
                ),
            ],
            options={
                "permissions": [
                    ("manage_membership", "Can add or remove members from teams")
                ],
            },
        ),
        migrations.AddConstraint(
            model_name="jobtype",
            constraint=models.UniqueConstraint(
                fields=("name", "version"), name="unique_name_version"
            ),
        ),
        migrations.AddField(
            model_name="jobstart",
            name="job_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="keystone.jobtype"
            ),
        ),
        migrations.AddField(
            model_name="jobstart",
            name="quotas",
            field=models.ManyToManyField(to="keystone.archquota"),
        ),
        migrations.AddField(
            model_name="jobstart",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="jobcomplete",
            name="job_start",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="keystone.jobstart"
            ),
        ),
        migrations.AddField(
            model_name="collection",
            name="accounts",
            field=models.ManyToManyField(to="keystone.account"),
        ),
        migrations.AddField(
            model_name="collection",
            name="teams",
            field=models.ManyToManyField(to="keystone.team"),
        ),
        migrations.AddField(
            model_name="collection",
            name="users",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name="archquota",
            name="content_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="account",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="keystone.account"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                related_name="user_set",
                related_query_name="user",
                to="auth.group",
                verbose_name="groups",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="teams",
            field=models.ManyToManyField(
                blank=True, related_name="members", to="keystone.team"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
        migrations.AddConstraint(
            model_name="collection",
            constraint=models.CheckConstraint(
                check=models.Q(
                    ("collection_type", "AIT"),
                    ("collection_type", "SPECIAL"),
                    ("collection_type", "CUSTOM"),
                    _connector="OR",
                ),
                name="check_valid_collection_type",
            ),
        ),
        migrations.AddIndex(
            model_name="archquota",
            index=models.Index(
                fields=["content_type", "object_id"],
                name="keystone_ar_content_1122e5_idx",
            ),
        ),
        migrations.AddConstraint(
            model_name="user",
            constraint=models.CheckConstraint(
                check=models.Q(("role", "ADMIN"), ("role", "USER"), _connector="OR"),
                name="check_valid_role",
            ),
        ),
    ]
