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

package com.epam.datalab.backendapi.resources.dto;

import com.epam.datalab.dto.exploratory.ImageSharingStatus;
import com.epam.datalab.dto.exploratory.ImageStatus;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.NonNull;


import java.util.Set;

@Data
@NoArgsConstructor
@JsonIgnoreProperties(ignoreUnknown = true)
public class ImageFilterFormData {
    @NonNull
    private Set<String> imageNames;
    @NonNull
    private Set<ImageStatus> statuses;
    @NonNull
    private Set<String> endpoints;
    @NonNull
    private Set<String> templateNames;
    @NonNull
    private Set<ImageSharingStatus> sharingStatuses;
}
