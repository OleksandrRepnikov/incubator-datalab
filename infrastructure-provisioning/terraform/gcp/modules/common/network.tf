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

resource "google_compute_subnetwork" "subnet" {
  name          = "${var.project_tag}-subnet"
  ip_cidr_range = "${var.cidr_range}"
  region        = "${var.region}"
  network       = "${var.vpc_name}"
}

resource "google_compute_firewall" "fw_ingress" {
  name    = "${var.fw_ingress}"
  network = "${var.vpc_name}"
  allow {
    protocol = "all"
  }
  target_tags   = ["${var.network_tag}"]
  source_ranges = ["${var.cidr_range}", "${var.traefik_cidr}"]
}

resource "google_compute_firewall" "fw_egress_public" {
  name      = "${var.fw_egress_public}"
  network   = "${var.vpc_name}"
  direction = "EGRESS"
  allow {
    protocol = "tcp"
    ports    = ["443"]
  }
  target_tags        = ["${var.network_tag}"]
  destination_ranges = ["0.0.0.0/0"]
}

resource "google_compute_firewall" "fw_egress_private" {
  name      = "${var.fw_egress_private}"
  network   = "${var.vpc_name}"
  direction = "EGRESS"
  allow {
    protocol = "all"
  }
  target_tags        = ["${var.network_tag}"]
  destination_ranges = ["${var.cidr_range}", "${var.traefik_cidr}"]
}