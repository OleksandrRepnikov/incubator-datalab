#!/usr/bin/python3

# *****************************************************************************
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# ******************************************************************************

from fabric import *
from patchwork.files import exists
from datalab.fab import *
import argparse
import sys
import time
import traceback

parser = argparse.ArgumentParser()
parser.add_argument('--hostname', type=str, default='')
parser.add_argument('--keyfile', type=str, default='')
parser.add_argument('--initial_user', type=str, default='')
parser.add_argument('--os_user', type=str, default='')
parser.add_argument('--sudo_group', type=str, default='')
args = parser.parse_args()


def ensure_ssh_user(initial_user, os_user, sudo_group, conn):
    print('ensure_ssh_user function')
    if not exists('/home/{}/.ssh_user_ensured'.format(initial_user)):
        print('ensure_ssh_user function2')
        conn.sudo('useradd -m -G {1} -s /bin/bash {0}'.format(os_user, sudo_group))
        conn.sudo('echo "{} ALL = NOPASSWD:ALL" >> /etc/sudoers'.format(os_user))
        conn.sudo('mkdir /home/{}/.ssh'.format(os_user))
        conn.sudo('chown -R {0}:{0} /home/{1}/.ssh/'.format(initial_user, os_user))
        conn.sudo('cat /home/{0}/.ssh/authorized_keys > /home/{1}/.ssh/authorized_keys'.format(initial_user, os_user))
        conn.sudo('chown -R {0}:{0} /home/{0}/.ssh/'.format(os_user))
        conn.sudo('chmod 700 /home/{0}/.ssh'.format(os_user))
        conn.sudo('chmod 600 /home/{0}/.ssh/authorized_keys'.format(os_user))
        conn.sudo('mkdir /home/{}/.ensure_dir'.format(os_user))
        conn.sudo('touch /home/{}/.ssh_user_ensured'.format(initial_user))

def init_datalab_connection(hostname, username, keyfile):
    try:
        global conn
        attempt = 0
        while attempt < 10:
            print('connection attempt {}'.format(attempt))
            with Connection(host = hostname, user = username, connect_kwargs={'key_filename': keyfile}) as conn:
                try:
                    conn.run('ls')
                    return conn
                except Exception as ex:
                    traceback.print_exc()
                    attempt += 1
                    time.sleep(10)
    except:
        traceback.print_exc()
        sys.exit(1)



if __name__ == "__main__":
    print("Configure connections")
    init_datalab_connection(args.hostname, args.initial_user, args.keyfile)
    conn.run('pwd; hostname; ls -lah')
    print("Creating ssh user: {}".format(args.os_user))
    try:
        ensure_ssh_user(args.initial_user, args.os_user, args.sudo_group, conn)
    except Exception as err:
        print('Failed to create ssh user', str(err))
        sys.exit(1)
    datalab.fab.close_connection()
