#!/usr/bin/python

# *****************************************************************************
#
# Copyright (c) 2016, EPAM SYSTEMS INC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# ******************************************************************************

import os
import sys
import logging
import traceback
from dlab.fab import *
from dlab.meta_lib import *
from dlab.actions_lib import *
from fabric.api import *
import multiprocessing


def reupload_key(instance_name):
    reupload_config['instance_private_ip'] = False
    if os.environ['conf_cloud_provider'] == 'aws':
        reupload_config['instance_ips'] = get_instance_ip_address('Name', instance_name)
        reupload_config['instance_private_ip'] = reupload_config['instance_ips']['Private']
    elif os.environ['conf_cloud_provider'] == 'azure':
        reupload_config['instance_private_ip'] = get_instance_ip_address(os.environ['conf_service_base_name'],
                                                                  instance_name)
    elif os.environ['conf_cloud_provider'] == 'gcp':
        reupload_config['instance_private_ip'] = get_private_ip_address(instance_name)
    params = "--user {} --hostname {} --keyfile '{}' --additional_config '{}'".format(
        reupload_config['os_user'], reupload_config['instance_private_ip'], reupload_config['keyfile'],
        json.dumps(reupload_config['additional_config']))
    try:
        # Run script to manage git credentials
        local("~/scripts/{}.py {}".format('install_user_key', params))
    except:
        traceback.print_exc()
        raise Exception


if __name__ == "__main__":
    local_log_filename = "{}_{}_{}.log".format(os.environ['conf_resource'], os.environ['edge_user_name'],
                                               os.environ['request_id'])
    local_log_filepath = "/logs/" + os.environ['conf_resource'] + "/" + local_log_filename
    logging.basicConfig(format='%(levelname)-8s [%(asctime)s]  %(message)s',
                        level=logging.DEBUG,
                        filename=local_log_filepath)

    try:
        create_aws_config_files()
        logging.info('[REUPLOADING USER SSH KEY]')
        print('[REUPLOADING USER SSH KEY]')
        reupload_config = dict()
        reupload_config['os_user'] = os.environ['conf_os_user']
        reupload_config['service_base_name'] = os.environ['conf_service_base_name']
        reupload_config['edge_user_name'] = os.environ['edge_user_name']

        reupload_config['tag_name'] = reupload_config['service_base_name'] + '-Tag'
        reupload_config['keyfile'] = '{}{}.pem'.format(os.environ['conf_key_dir'], os.environ['conf_key_name'])
        reupload_config['resource_id'] = os.environ['list_instances_names']
        reupload_config['additional_config'] = {"user_keyname": reupload_config['edge_user_name'],
                                                "user_keydir": os.environ['conf_key_dir']}
        if os.environ['conf_cloud_provider'] == 'aws':
            try:
                reupload_key(reupload_config['resource_id'])
            except Exception as err:
                traceback.print_exc()
                raise Exception
    except Exception as err:
        append_result("Failed to reupload user ssh key.", str(err))
        sys.exit(1)

    with open("/root/result.json", 'w') as result:
        res = {"Action": "Reupload user ssh key"}
        result.write(json.dumps(res))