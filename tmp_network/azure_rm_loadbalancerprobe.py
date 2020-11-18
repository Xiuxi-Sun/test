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
module: azure_rm_loadbalancerprobe
version_added: '2.9'
short_description: Manage Azure LoadBalancerProbe instance.
description:
  - 'Create, update and delete instance of Azure LoadBalancerProbe.'
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
    required: true
    type: str
  state:
    description:
      - Assert the state of the LoadBalancerProbe.
      - >-
        Use C(present) to create or update an LoadBalancerProbe and C(absent) to
        delete it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
'''

RETURN = '''
id:
  description:
    - Resource ID.
  returned: always
  type: str
  sample: null
name:
  description:
    - >-
      The name of the resource that is unique within the set of probes used by
      the load balancer. This name can be used to access the resource.
  returned: always
  type: str
  sample: null
etag:
  description:
    - A unique read-only string that changes whenever the resource is updated.
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
      The protocol of the end point. If 'Tcp' is specified, a received ACK is
      required for the probe to be successful. If 'Http' or 'Https' is
      specified, a 200 OK response from the specifies URI is required for the
      probe to be successful.
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
      allocated timeout period (in seconds) which allows two full probes before
      taking the instance out of rotation. The default value is 15, the minimum
      value is 5.
  returned: always
  type: integer
  sample: null
number_of_probes:
  description:
    - >-
      The number of probes where if no response, will result in stopping further
      traffic from being delivered to the endpoint. This values allows endpoints
      to be taken out of rotation faster or slower than the typical times used
      in Azure.
  returned: always
  type: integer
  sample: null
request_path:
  description:
    - >-
      The URI used for requesting health status from the VM. Path is required if
      a protocol is set to http. Otherwise, it is not allowed. There is no
      default value.
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

from ansible_collections.azure.azcollection.plugins.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.network import NetworkManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMLoadBalancerProbe(AzureRMModuleBaseExt):
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
                type='str',
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.load_balancer_name = None
        self.probe_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMLoadBalancerProbe, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                       supports_check_mode=True,
                                                       supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                self.body[key] = kwargs[key]

        self.inflate_parameters(self.module_arg_spec, self.body, 0)

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01')

        old_response = self.get_resource()

        if not old_response:
            if self.state == 'present':
                self.to_do = Actions.Create
        else:
            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                self.results['modifiers'] = modifiers
                self.results['compare'] = []
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            response = self.create_update_resource()
        elif self.to_do == Actions.Delete:
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            self.delete_resource()
        else:
            self.results['changed'] = False
            response = old_response

        return self.results

    def create_update_resource(self):
        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.load_balancer_probes.create()
            else:
                response = self.mgmt_client.load_balancer_probes.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the LoadBalancerProbe instance.')
            self.fail('Error creating the LoadBalancerProbe instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.load_balancer_probes.delete()
        except CloudError as e:
            self.log('Error attempting to delete the LoadBalancerProbe instance.')
            self.fail('Error deleting the LoadBalancerProbe instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.load_balancer_probes.get(resource_group_name=self.resource_group_name,
                                                                 load_balancer_name=self.load_balancer_name,
                                                                 probe_name=self.probe_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMLoadBalancerProbe()


if __name__ == '__main__':
    main()
