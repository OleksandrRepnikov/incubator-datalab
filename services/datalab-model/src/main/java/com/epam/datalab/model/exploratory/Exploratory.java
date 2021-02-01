/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

package com.epam.datalab.model.exploratory;

import com.epam.datalab.dto.aws.computational.ClusterConfig;
import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Builder;
import lombok.Data;

import java.util.List;

@Data
@Builder
public class Exploratory {
    private final String name;
    private final String dockerImage;
    private final String version;
    private final String templateName;
    private final String shape;
    private final String imageName;
    private final String endpoint;
    private final String project;
    private final String exploratoryTag;
    private final List<ClusterConfig> clusterConfig;
    private Boolean enabledGPU;
    private String masterGPUType;
    private String slaveGPUType;
    private String masterGPUCount;
    private String slaveGPUCount;
}
