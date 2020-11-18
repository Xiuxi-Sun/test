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
module: azure_rm_loadbalancerloadbalancingrule
version_added: '2.9'
short_description: Manage Azure LoadBalancerLoadBalancingRule instance.
description:
  - 'Create, update and delete instance of Azure LoadBalancerLoadBalancingRule.'
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
  load_balancing_rule_name:
    description:
      - The name of the load balancing rule.
    required: true
    type: str
  state:
    description:
      - Assert the state of the LoadBalancerLoadBalancingRule.
      - >-
        Use C(present) to create or update an LoadBalancerLoadBalancingRule and
        C(absent) to delete it.
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
      The name of the resource that is unique within the set of load balancing
      rules used by the load balancer. This name can be used to access the
      resource.
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
frontend_ip_configuration:
  description:
    - A reference to frontend IP addresses.
  returned: always
  type: dict
  sample: null
  contains:
    id:
      description:
        - Resource ID.
      returned: always
      type: str
      sample: null
backend_address_pool:
  description:
    - >-
      A reference to a pool of DIPs. Inbound traffic is randomly load balanced
      across IPs in the backend IPs.
  returned: always
  type: dict
  sample: null
  contains:
    id:
      description:
        - Resource ID.
      returned: always
      type: str
      sample: null
probe:
  description:
    - The reference to the load balancer probe used by the load balancing rule.
  returned: always
  type: dict
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
    - The reference to the transport protocol used by the load balancing rule.
  returned: always
  type: str
  sample: null
load_distribution:
  description:
    - The load distribution policy for this rule.
  returned: always
  type: str
  sample: null
frontend_port:
  description:
    - >-
      The port for the external endpoint. Port numbers for each rule must be
      unique within the Load Balancer. Acceptable values are between 0 and
      65534. Note that value 0 enables "Any Port".
  returned: always
  type: integer
  sample: null
backend_port:
  description:
    - >-
      The port used for internal connections on the endpoint. Acceptable values
      are between 0 and 65535. Note that value 0 enables "Any Port".
  returned: always
  type: integer
  sample: null
idle_timeout_in_minutes:
  description:
    - >-
      The timeout for the TCP idle connection. The value can be set between 4
      and 30 minutes. The default value is 4 minutes. This element is only used
      when the protocol is set to TCP.
  returned: always
  type: integer
  sample: null
enable_floating_ip:
  description:
    - >-
      Configures a virtual machine's endpoint for the floating IP capability
      required to configure a SQL AlwaysOn Availability Group. This setting is
      required when using the SQL AlwaysOn Availability Groups in SQL server.
      This setting can't be changed after you create the endpoint.
  returned: always
  type: bool
  sample: null
enable_tcp_reset:
  description:
    - >-
      Receive bidirectional TCP Reset on TCP flow idle timeout or unexpected
      connection termination. This element is only used when the protocol is set
      to TCP.
  returned: always
  type: bool
  sample: null
disable_outbound_snat:
  description:
    - >-
      Configures SNAT for the VMs in the backend pool to use the publicIP
      address specified in the frontend of the load balancing rule.
  returned: always
  type: bool
  sample: null
provisioning_state:
  description:
    - The provisioning state of the load balancing rule resource.
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


class AzureRMLoadBalancerLoadBalancingRule(AzureRMModuleBaseExt):
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
            load_balancing_rule_name=dict(
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
        self.load_balancing_rule_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMLoadBalancerLoadBalancingRule, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                response = self.mgmt_client.load_balancer_load_balancing_rules.create()
            else:
                response = self.mgmt_client.load_balancer_load_balancing_rules.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the LoadBalancerLoadBalancingRule instance.')
            self.fail('Error creating the LoadBalancerLoadBalancingRule instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.load_balancer_load_balancing_rules.delete()
        except CloudError as e:
            self.log('Error attempting to delete the LoadBalancerLoadBalancingRule instance.')
            self.fail('Error deleting the LoadBalancerLoadBalancingRule instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.load_balancer_load_balancing_rules.get(resource_group_name=self.resource_group_name,
                                                                               load_balancer_name=self.load_balancer_name,
                                                                               load_balancing_rule_name=self.load_balancing_rule_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMLoadBalancerLoadBalancingRule()


if __name__ == '__main__':
    main()
