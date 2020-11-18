#!/usr/bin/python
#
# Copyright (c) 2020 GuopengLin, (@t-glin)
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = '''
---
module: azure_rm_loadbalancerprobe_info
version_added: '2.9'
short_description: Get LoadBalancerProbe info.
description:
  - Get info of LoadBalancerProbe.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  load_balancer_name:
    description:
      - The name of the load balancer.
    required: true
    type: str
  probe_name:
    description:
      - The name of the probe.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: LoadBalancerProbeList
      azure_rm_loadbalancerprobe_info: 
        load_balancer_name: lb
        resource_group_name: testrg
        

    - name: LoadBalancerProbeGet
      azure_rm_loadbalancerprobe_info: 
        load_balancer_name: lb
        probe_name: probe1
        resource_group_name: testrg
        

'''

RETURN = '''
load_balancer_probes:
  description: >-
    A list of dict results where the key is the name of the LoadBalancerProbe
    and the values are the facts for that LoadBalancerProbe.
  returned: always
  type: complex
  contains:
    value:
      description:
        - A list of probes in a load balancer.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - >-
              The name of the resource that is unique within the set of probes
              used by the load balancer. This name can be used to access the
              resource.
          returned: always
          type: str
          sample: null
        load_balancing_rules:
          description:
            - The load balancer rules that use this probe.
          returned: always
          type: list
          sample: null
          contains:
            id:
              description:
                - Resource ID.
              returned: always
              type: str
              sample: null
        protocol:
          description:
            - >-
              The protocol of the end point. If 'Tcp' is specified, a received
              ACK is required for the probe to be successful. If 'Http' or
              'Https' is specified, a 200 OK response from the specifies URI is
              required for the probe to be successful.
          returned: always
          type: str
          sample: null
        port:
          description:
            - >-
              The port for communicating the probe. Possible values range from 1
              to 65535, inclusive.
          returned: always
          type: integer
          sample: null
        interval_in_seconds:
          description:
            - >-
              The interval, in seconds, for how frequently to probe the endpoint
              for health status. Typically, the interval is slightly less than
              half the allocated timeout period (in seconds) which allows two
              full probes before taking the instance out of rotation. The
              default value is 15, the minimum value is 5.
          returned: always
          type: integer
          sample: null
        number_of_probes:
          description:
            - >-
              The number of probes where if no response, will result in stopping
              further traffic from being delivered to the endpoint. This values
              allows endpoints to be taken out of rotation faster or slower than
              the typical times used in Azure.
          returned: always
          type: integer
          sample: null
        request_path:
          description:
            - >-
              The URI used for requesting health status from the VM. Path is
              required if a protocol is set to http. Otherwise, it is not
              allowed. There is no default value.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - The URL to get the next set of results.
      returned: always
      type: str
      sample: null
    id:
      description:
        - Resource ID.
      returned: always
      type: str
      sample: null
    name:
      description:
        - >-
          The name of the resource that is unique within the set of probes used
          by the load balancer. This name can be used to access the resource.
      returned: always
      type: str
      sample: null
    etag:
      description:
        - >-
          A unique read-only string that changes whenever the resource is
          updated.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Type of the resource.
      returned: always
      type: str
      sample: null
    load_balancing_rules:
      description:
        - The load balancer rules that use this probe.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - Resource ID.
          returned: always
          type: str
          sample: null
    protocol:
      description:
        - >-
          The protocol of the end point. If 'Tcp' is specified, a received ACK
          is required for the probe to be successful. If 'Http' or 'Https' is
          specified, a 200 OK response from the specifies URI is required for
          the probe to be successful.
      returned: always
      type: str
      sample: null
    port:
      description:
        - >-
          The port for communicating the probe. Possible values range from 1 to
          65535, inclusive.
      returned: always
      type: integer
      sample: null
    interval_in_seconds:
      description:
        - >-
          The interval, in seconds, for how frequently to probe the endpoint for
          health status. Typically, the interval is slightly less than half the
          allocated timeout period (in seconds) which allows two full probes
          before taking the instance out of rotation. The default value is 15,
          the minimum value is 5.
      returned: always
      type: integer
      sample: null
    number_of_probes:
      description:
        - >-
          The number of probes where if no response, will result in stopping
          further traffic from being delivered to the endpoint. This values
          allows endpoints to be taken out of rotation faster or slower than the
          typical times used in Azure.
      returned: always
      type: integer
      sample: null
    request_path:
      description:
        - >-
          The URI used for requesting health status from the VM. Path is
          required if a protocol is set to http. Otherwise, it is not allowed.
          There is no default value.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - The provisioning state of the probe resource.
      returned: always
      type: str
      sample: null

'''

from ansible_collections.azure.azcollection.plugins.module_utils.azure_rm_common_ext import AzureRMModuleBase
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.network import NetworkManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMLoadBalancerProbeInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            load_balancer_name=dict(
                type='str',
                required=True
            ),
            probe_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.load_balancer_name = None
        self.probe_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-07-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMLoadBalancerProbeInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01')

        if (self.resource_group_name is not None and
            self.load_balancer_name is not None and
            self.probe_name is not None):
            self.results['load_balancer_probes'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.load_balancer_name is not None):
            self.results['load_balancer_probes'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.load_balancer_probes.get(resource_group_name=self.resource_group_name,
                                                                 load_balancer_name=self.load_balancer_name,
                                                                 probe_name=self.probe_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.load_balancer_probes.list(resource_group_name=self.resource_group_name,
                                                                  load_balancer_name=self.load_balancer_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def format_item(self, item):
        if hasattr(item, 'as_dict'):
            return [item.as_dict()]
        else:
            result = []
            items = list(item)
            for tmp in items:
                result.append(tmp.as_dict())
            return result


def main():
    AzureRMLoadBalancerProbeInfo()


if __name__ == '__main__':
    main()
