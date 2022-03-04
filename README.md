User Retirement Tutor plugin
===================================

This is an **experimental** plugin for
[Tutor](https://docs.tutor.overhang.io) that enables the [user retirement 
feature](https://edx.readthedocs.io/projects/edx-installing-configuring-and-running/en/latest/configuration/user_retire/driver_setup.html) in Open edX.

Installation
------------

    pip install git+https://github.com/hastexo/tutor-contrib-retirement

Usage
-----

To enable this plugin, run:

    tutor plugins enable retirement


Before starting Tutor, build the docker image:

    tutor images build retirement


Configuration
-------------

* `RETIREMENT_EDX_OAUTH2_CLIENT_ID` (default `"retirement_service_worker"`)
* `RETIREMENT_COOL_OFF_DAYS` (default `30`)
* `RETIREMENT_K8S_CRONJOB_SCHEDULE` (default `"0 0 * * *"`, once a day at 
  midnight)

These values can be modified with `tutor config save --set
PARAM_NAME=VALUE` commands.
