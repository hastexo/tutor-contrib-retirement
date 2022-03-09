User Retirement Tutor plugin
===================================

This is an **experimental** plugin for
[Tutor](https://docs.tutor.overhang.io) that enables the [user retirement 
feature](https://edx.readthedocs.io/projects/edx-installing-configuring-and-running/en/latest/configuration/user_retire/index.html) in Open edX.

Installation
------------

    pip install git+https://github.com/hastexo/tutor-contrib-retirement@v0.0.0

Usage
-----

To enable this plugin, run:

    tutor plugins enable retirement

Before starting Tutor, build the docker image:

    tutor images build retirement

After enabling this plugin, you need to restart your Tutor deployment with
`tutor local quickstart` or `tutor k8s quickstart`. This ensures that the 
retirement service worker is registered as an OAuth2 client in LMS and that the 
retirement pipeline stages are correctly populated in LMS.

To run the retirement pipeline in the Tutor local deployment:

    tutor local retire-users

This will start the `retirement-job` service and run the retirement pipeline 
as described [here](https://edx.readthedocs.io/projects/edx-installing-configuring-and-running/en/latest/configuration/user_retire/driver_setup.html).
If you want to run this command periodically in a local deployment, you can 
invoke this command from a cron job on your host. 

For a Kubernetes deployment, this plugin defines a [CronJob](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/) 
which runs the retirement pipeline according to the schedule defined in 
the `RETIREMENT_K8S_CRONJOB_SCHEDULE` configuration parameter.
You can also tweak the [history
limits](https://kubernetes.io/docs/tasks/job/automated-tasks-with-cron-jobs/#jobs-history-limits)
for the CronJob.

Configuration
-------------

* `RETIREMENT_EDX_OAUTH2_CLIENT_ID` (default `"retirement_service_worker"`)
* `RETIREMENT_COOL_OFF_DAYS` (default `30`)
* `RETIREMENT_K8S_CRONJOB_HISTORYLIMIT_FAILURE` (default `1`)
* `RETIREMENT_K8S_CRONJOB_HISTORYLIMIT_SUCCESS` (default `3`)
* `RETIREMENT_K8S_CRONJOB_SCHEDULE` (default `"0 0 * * *"`, once a day at 
  midnight)

These values can be modified with `tutor config save --set
PARAM_NAME=VALUE` commands.
