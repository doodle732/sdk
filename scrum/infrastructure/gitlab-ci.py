#!/usr/bin/env python3
import os
import yaml

PROJECT_ROOT = os.path.realpath(os.path.dirname(os.path.realpath(__file__)) + "/../../")

def job_runs_robot_tests(job):
    with open(PROJECT_ROOT + "/.gitlab-ci.yml", "r") as stream:
        yml = yaml.safe_load(stream)
        if job not in yml:
            raise BaseException("Job %s does not exist in gitlab ci file!" % (job))
        # We satisfy this by running robot command on scrum folder
        if "robot scrum" not in yml[job]["script"]:
            raise BaseException("Merge request pipepline should run 'robot scrum'")

def check_job_exists(job):
    with open(PROJECT_ROOT + "/.gitlab-ci.yml", "r") as stream:
        yml = yaml.safe_load(stream)
        # We satisfy this by running robot command on scrum folder
        if job not in yml:
            raise BaseException("Job %s does not exist in gitlab ci file!" % (job))
