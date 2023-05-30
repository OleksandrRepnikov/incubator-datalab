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

variable "project_name" {}

variable "sbn" {}

variable "project_tag" {}

variable "endpoint_tag" {}

variable "user_tag" {}

variable "custom_tag" {}

variable "notebook_name" {}

variable "region" {}

variable "product" {}

variable "ami" {}

variable "instance_type" {}

variable "ssh_key" {}

variable "initial_user" {}

variable "subnet_id" {}

variable "nb-sg_id" {}

variable "resource_group" {}

variable "ami_publisher" {
  type = "map"
  default = {
    debian = "Canonical"
    redhat = "RedHat"
    custom = ""
  }
}

variable "ami_offer" {
  type = "map"
  default = {
    debian = "UbuntuServer"
    redhat = "RHEL"
    custom = ""
  }
}

variable "ami_sku" {
  type = "map"
  default = {
    debian = "16.04-LTS"
    redhat = "7.3"
    custom = ""
  }
}

variable "ami_version" {
  type = "map"
  default = {
    debian = "16.04.201907290"
    redhat = "7.3.2017090800"
    custom = ""
  }
}

variable "custom_ami" {}

variable "os_env" {}