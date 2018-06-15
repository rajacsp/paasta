#!/usr/bin/env python
# Copyright 2015-2016 Yelp Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
PaaSTA service list (instances) etc.
"""
from pyramid.view import view_config

from paasta_tools.api import settings
from paasta_tools.utils import get_service_instance_list
from paasta_tools.utils import get_services_for_cluster
from paasta_tools.utils import list_all_instances_for_service


@view_config(route_name='service.list', request_method='GET', renderer='json')
def list_instances(request):
    service = request.swagger_data.get('service')
    instances = list_all_instances_for_service(service, clusters=[settings.cluster])
    return {'instances': list(instances)}


@view_config(route_name='service.cluster', request_method='GET', renderer='json')
def list_services_for_cluster(request):
    result = []
    services_for_cluster = get_services_for_cluster(cluster=[settings.cluster])
    for service_name in services_for_cluster:
        all_service_instances = get_service_instance_list(service=service_name)
        result.extend(all_service_instances)

    return {'services': result}
