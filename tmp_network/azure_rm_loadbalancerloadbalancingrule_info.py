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
module: azure_rm_loadbalancerloadbalancingrule_info
version_added: '2.9'
short_description: Get LoadBalancerLoadBalancingRule info.
description:
  - Get info of LoadBalancerLoadBalancingRule.
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
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: LoadBalancerLoadBalancingRuleList
      azure_rm_loadbalancerloadbalancingrule_info: 
        load_balancer_name: lb1
        resource_group_name: testrg
        

    - name: LoadBalancerLoadBalancingRuleGet
      azure_rm_loadbalancerloadbalancingrule_info: 
        load_balancer_name: lb1
        load_balancing_rule_name: rule1
        resource_group_name: testrg
        

'''

RETURN = '''
load_balancer_load_balancing_rules:
  description: >-
    A list of dict results where the key is the name of the
    LoadBalancerLoadBalancingRule and the values are the facts for that
    LoadBalancerLoadBalancingRule.
  returned: always
  type: complex
  contains:
    value:
      description:
        - A list of load balancing rules in a load balancer.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - >-
              The name of the resource that is unique within the set of load
              balancing rules used by the load balancer. This name can be used
              to access the resource.
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
              A reference to a pool of DIPs. Inbound traffic is randomly load
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
        probe:
          description:
            - >-
              The reference to the load balancer probe used by the load
              balancing rule.
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
            - >-
              The reference to the transport protocol used by the load balancing
              rule.
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
              The port for the external endpoint. Port numbers for each rule
              must be unique within the Load Balancer. Acceptable values are
              between 0 and 65534. Note that value 0 enables "Any Port".
          returned: always
          type: integer
          sample: null
        backend_port:
          description:
            - >-
              The port used for internal connections on the endpoint. Acceptable
              values are between 0 and 65535. Note that value 0 enables "Any
              Port".
          returned: always
          type: integer
          sample: null
        idle_timeout_in_minutes:
          description:
            - >-
              The timeout for the TCP idle connection. The value can be set
              between 4 and 30 minutes. The default value is 4 minutes. This
              element is only used when the protocol is set to TCP.
          returned: always
          type: integer
          sample: null
        enable_floating_ip:
          description:
            - >-
              Configures a virtual machine's endpoint for the floating IP
              capability required to configure a SQL AlwaysOn Availability
              Group. This setting is required when using the SQL AlwaysOn
              Availability Groups in SQL server. This setting can't be changed
              after you create the endpoint.
          returned: always
          type: bool
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
        disable_outbound_snat:
          description:
            - >-
              Configures SNAT for the VMs in the backend pool to use the
              publicIP address specified in the frontend of the load balancing
              rule.
          returned: always
          type: bool
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
          The name of the resource that is unique within the set of load
          balancing rules used by the load balancer. This name can be used to
          access the resource.
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
          A reference to a pool of DIPs. Inbound traffic is randomly load
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
    probe:
      description:
        - >-
          The reference to the load balancer probe used by the load balancing
          rule.
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
        - >-
          The reference to the transport protocol used by the load balancing
          rule.
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
          The port used for internal connections on the endpoint. Acceptable
          values are between 0 and 65535. Note that value 0 enables "Any Port".
      returned: always
      type: integer
      sample: null
    idle_timeout_in_minutes:
      description:
        - >-
          The timeout for the TCP idle connection. The value can be set between
          4 and 30 minutes. The default value is 4 minutes. This element is only
          used when the protocol is set to TCP.
      returned: always
      type: integer
      sample: null
    enable_floating_ip:
      description:
        - >-
          Configures a virtual machine's endpoint for the floating IP capability
          required to configure a SQL AlwaysOn Availability Group. This setting
          is required when using the SQL AlwaysOn Availability Groups in SQL
          server. This setting can't be changed after you create the endpoint.
      returned: always
      type: bool
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

from ansible_collections.azure.azcollection.plugins.module_utils.azure_rm_common_ext import AzureRMModuleBase
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.network import NetworkManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMLoadBalancerLoadBalancingRuleInfo(AzureRMModuleBase):
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
                type='str'
            )
        )

        self.resource_group_name = None
        self.load_balancer_name = None
        self.load_balancing_rule_name = None

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
        super(AzureRMLoadBalancerLoadBalancingRuleInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01')

        if (self.resource_group_name is not None and
            self.load_balancer_name is not None and
            self.load_balancing_rule_name is not None):
            self.results['load_balancer_load_balancing_rules'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.load_balancer_name is not None):
            self.results['load_balancer_load_balancing_rules'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.load_balancer_load_balancing_rules.get(resource_group_name=self.resource_group_name,
                                                                               load_balancer_name=self.load_balancer_name,
                                                                               load_balancing_rule_name=self.load_balancing_rule_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.load_balancer_load_balancing_rules.list(resource_group_name=self.resource_group_name,
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
    AzureRMLoadBalancerLoadBalancingRuleInfo()


if __name__ == '__main__':
    main()
