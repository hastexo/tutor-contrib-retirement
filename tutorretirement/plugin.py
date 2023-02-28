from .__about__ import __version__
from glob import glob
import os
import pkg_resources
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
        "DOCKER_IMAGE": "{{ DOCKER_REGISTRY }}retirement:{{ RETIREMENT_VERSION }}",  # noqa: E501
        "EDX_OAUTH2_CLIENT_ID": "retirement_service_worker",
        "COOL_OFF_DAYS": 30,
        "TUBULAR_VERSION": "{{ OPENEDX_COMMON_VERSION }}",
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
        command=f"bash -e run_retirement_pipeline.sh {cool_off_days}"
    )


# Add the "templates" folder as a template root
hooks.Filters.ENV_TEMPLATE_ROOTS.add_item(
    pkg_resources.resource_filename("tutorretirement", "templates")
)
# Render the "build" and "apps" folders
hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
    [
        ("retirement/build", "plugins"),
        ("retirement/apps", "plugins"),
    ],
)
# Load patches from files
for path in glob(
    os.path.join(
        pkg_resources.resource_filename("tutorretirement", "patches"),
        "*",
    )
):
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
path = pkg_resources.resource_filename(
    "tutorretirement", os.path.join(
        "templates", "retirement", "tasks", "lms", "init")
)
with open(path, encoding="utf-8") as task_file:
    init_task = task_file.read()
    hooks.Filters.CLI_DO_INIT_TASKS.add_item(("lms", init_task))
