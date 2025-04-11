from .__about__ import __version__
from glob import glob
import os
# When Tutor drops support for Python 3.8, we'll need to update this to:
# from importlib import resources as importlib_resources
# See: https://github.com/overhangio/tutor/issues/966#issuecomment-1938681102
import importlib_resources
import click
from tutor import hooks
from tutor import config as tutor_config
from tutor.commands.local import local as local_command_group


config = {
    "unique": {
        "EDX_OAUTH2_CLIENT_SECRET": "{{ 32|random_string }}",
    },
    "defaults": {
        "VERSION": __version__,
        "BASE_IMAGE": "docker.io/python:3.11",
        "DOCKER_IMAGE": "{{ DOCKER_REGISTRY }}retirement:{{ RETIREMENT_VERSION }}",  # noqa: E501
        "EDX_OAUTH2_CLIENT_ID": "retirement_service_worker",
        "COOL_OFF_DAYS": 30,
        "K8S_CRONJOB_HISTORYLIMIT_FAILURE": 1,
        "K8S_CRONJOB_HISTORYLIMIT_SUCCESS": 3,
        "K8S_CRONJOB_SCHEDULE": "0 0 * * *",
    },
}

hooks.Filters.IMAGES_BUILD.add_item((
    "retirement",
    ("plugins", "retirement", "build", "retirement"),
    "{{ RETIREMENT_DOCKER_IMAGE }}",
    (),
))
hooks.Filters.IMAGES_PULL.add_item((
    "retirement",
    "{{ RETIREMENT_DOCKER_IMAGE }}",
))
hooks.Filters.IMAGES_PUSH.add_item((
    "retirement",
    "{{ RETIREMENT_DOCKER_IMAGE }}",
))


@local_command_group.command(help="Run the retirement pipeline")
@click.pass_obj
def retire_users(context):
    config = tutor_config.load(context.root)
    job_runner = context.job_runner(config)
    cool_off_days = config["RETIREMENT_COOL_OFF_DAYS"]
    job_runner.run_task(
        service="retirement",
        command="bash -e scripts/user_retirement/run_retirement_pipeline.sh "
                f"{cool_off_days}"
    )


# Add the "templates" folder as a template root
hooks.Filters.ENV_TEMPLATE_ROOTS.add_item(
    str(importlib_resources.files("tutorretirement") / "templates")
)
# Render the "build" and "apps" folders
hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
    [
        ("retirement/build", "plugins"),
        ("retirement/apps", "plugins"),
    ],
)
# Load patches from files
for path in glob(str(
        importlib_resources.files("tutorretirement") / "patches" / "*")):

    with open(path, encoding="utf-8") as patch_file:
        hooks.Filters.ENV_PATCHES.add_item(
            (os.path.basename(path), patch_file.read())
        )
# Add configuration entries
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [
        (f"RETIREMENT_{key}", value)
        for key, value in config.get("defaults", {}).items()
    ]
)
hooks.Filters.CONFIG_UNIQUE.add_items(
    [
        (f"RETIREMENT_{key}", value)
        for key, value in config.get("unique", {}).items()
    ]
)
hooks.Filters.CONFIG_OVERRIDES.add_items(
    list(config.get("overrides", {}).items())
)

# Add init task
path = str(importlib_resources.files(
    "tutorretirement") / os.path.join(
        "templates", "retirement", "tasks", "lms", "init")
)
with open(path, encoding="utf-8") as task_file:
    init_task = task_file.read()
    hooks.Filters.CLI_DO_INIT_TASKS.add_item(("lms", init_task))
