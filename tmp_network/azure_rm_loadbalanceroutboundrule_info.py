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
module: azure_rm_loadbalanceroutboundrule_info
version_added: '2.9'
short_description: Get LoadBalancerOutboundRule info.
description:
  - Get info of LoadBalancerOutboundRule.
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
  outbound_rule_name:
    description:
      - The name of the outbound rule.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: LoadBalancerOutboundRuleList
      azure_rm_loadbalanceroutboundrule_info: 
        load_balancer_name: lb1
        resource_group_name: testrg
        

    - name: LoadBalancerOutboundRuleGet
      azure_rm_loadbalanceroutboundrule_info: 
        load_balancer_name: lb1
        outbound_rule_name: rule1
        resource_group_name: testrg
        

'''

RETURN = '''
load_balancer_outbound_rules:
  description: >-
    A list of dict results where the key is the name of the
    LoadBalancerOutboundRule and the values are the facts for that
    LoadBalancerOutboundRule.
  returned: always
  type: complex
  contains:
    value:
      description:
        - A list of outbound rules in a load balancer.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - >-
              The name of the resource that is unique within the set of outbound
              rules used by the load balancer. This name can be used to access
              the resource.
          returned: always
          type: str
          sample: null
        allocated_outbound_ports:
          description:
            - The number of outbound ports to be used for NAT.
          returned: always
          type: integer
          sample: null
        frontend_ip_configurations:
          description:
            - The Frontend IP addresses of the load balancer.
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
        backend_address_pool:
          description:
            - >-
              A reference to a pool of DIPs. Outbound traffic is randomly load
              balanced across IPs in the backend IPs.
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
            - The protocol for the outbound rule in load balancer.
          returned: always
          type: str
          sample: null
        enable_tcp_reset:
          description:
            - >-
              Receive bidirectional TCP Reset on TCP flow idle timeout or
              unexpected connection termination. This element is only used when
              the protocol is set to TCP.
          returned: always
          type: bool
          sample: null
        idle_timeout_in_minutes:
          description:
            - The timeout for the TCP idle connection.
          returned: always
          type: integer
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
          The name of the resource that is unique within the set of outbound
          rules used by the load balancer. This name can be used to access the
          resource.
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
    allocated_outbound_ports:
      description:
        - The number of outbound ports to be used for NAT.
      returned: always
      type: integer
      sample: null
    frontend_ip_configurations:
      description:
        - The Frontend IP addresses of the load balancer.
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
    backend_address_pool:
      description:
        - >-
          A reference to a pool of DIPs. Outbound traffic is randomly load
          balanced across IPs in the backend IPs.
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
    provisioning_state:
      description:
        - The provisioning state of the outbound rule resource.
      returned: always
      type: str
      sample: null
    protocol:
      description:
        - The protocol for the outbound rule in load balancer.
      returned: always
      type: str
      sample: null
    enable_tcp_reset:
      description:
        - >-
          Receive bidirectional TCP Reset on TCP flow idle timeout or unexpected
          connection termination. This element is only used when the protocol is
          set to TCP.
      returned: always
      type: bool
      sample: null
    idle_timeout_in_minutes:
      description:
        - The timeout for the TCP idle connection.
      returned: always
      type: integer
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


class AzureRMLoadBalancerOutboundRuleInfo(AzureRMModuleBase):
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
            outbound_rule_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.load_balancer_name = None
        self.outbound_rule_name = None

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
        super(AzureRMLoadBalancerOutboundRuleInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01')

        if (self.resource_group_name is not None and
            self.load_balancer_name is not None and
            self.outbound_rule_name is not None):
            self.results['load_balancer_outbound_rules'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.load_balancer_name is not None):
            self.results['load_balancer_outbound_rules'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.load_balancer_outbound_rules.get(resource_group_name=self.resource_group_name,
                                                                         load_balancer_name=self.load_balancer_name,
                                                                         outbound_rule_name=self.outbound_rule_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.load_balancer_outbound_rules.list(resource_group_name=self.resource_group_name,
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
    AzureRMLoadBalancerOutboundRuleInfo()


if __name__ == '__main__':
    main()
