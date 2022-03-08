from .__about__ import __version__
from glob import glob
import os
import pkg_resources
import click
from tutor import config as tutor_config
from tutor.commands.local import local as local_command_group


templates = pkg_resources.resource_filename(
    "tutorretirement", "templates"
)

config = {
    "add": {
        "EDX_OAUTH2_CLIENT_SECRET": "{{ 32|random_string }}",
    },
    "defaults": {
        "VERSION": __version__,
        "DOCKER_IMAGE": "{{ DOCKER_REGISTRY }}retirement:{{ RETIREMENT_VERSION }}",  # noqa: E501
        "EDX_OAUTH2_CLIENT_ID": "retirement_service_worker",
        "COOL_OFF_DAYS": 30,
        "TUBULAR_VERSION": "{{ OPENEDX_COMMON_VERSION }}",
        "K8S_CRONJOB_SCHEDULE": "0 0 * * *",
    },
}

hooks = {
    "build-image": {
        "retirement": "{{ RETIREMENT_DOCKER_IMAGE }}",
    },
    "remote-image": {
        "retirement": "{{ RETIREMENT_DOCKER_IMAGE }}",
    },
    "init": ["lms"]
}


@local_command_group.command(help="Run the retirement pipeline")
@click.pass_obj
def retire_users(context):
    config = tutor_config.load(context.root)
    job_runner = context.job_runner(config)
    cool_off_days = config["RETIREMENT_COOL_OFF_DAYS"]
    job_runner.run_job(
        service="retirement",
        command=f"bash -e run_retirement_pipeline.sh {cool_off_days}"
    )


def patches():
    all_patches = {}
    patches_dir = pkg_resources.resource_filename(
        "tutorretirement", "patches"
    )
    for path in glob(os.path.join(patches_dir, "*")):
        with open(path) as patch_file:
            name = os.path.basename(path)
            content = patch_file.read()
            all_patches[name] = content
    return all_patches
