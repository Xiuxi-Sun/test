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
module: azure_rm_securityrule_info
version_added: '2.9'
short_description: Get SecurityRule info.
description:
  - Get info of SecurityRule.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  network_security_group_name:
    description:
      - The name of the network security group.
    required: true
    type: str
  security_rule_name:
    description:
      - The name of the security rule.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get network security rule in network security group
      azure_rm_securityrule_info: 
        network_security_group_name: testnsg
        resource_group_name: rg1
        security_rule_name: rule1
        

    - name: List network security rules in network security group
      azure_rm_securityrule_info: 
        network_security_group_name: testnsg
        resource_group_name: rg1
        

'''

RETURN = '''
security_rules:
  description: >-
    A list of dict results where the key is the name of the SecurityRule and the
    values are the facts for that SecurityRule.
  returned: always
  type: complex
  contains:
    id:
      description:
        - Resource ID.
      returned: always
      type: str
      sample: null
    name:
      description:
        - >-
          The name of the resource that is unique within a resource group. This
          name can be used to access the resource.
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
    description:
      description:
        - A description for this rule. Restricted to 140 chars.
      returned: always
      type: str
      sample: null
    protocol:
      description:
        - Network protocol this rule applies to.
      returned: always
      type: str
      sample: null
    source_port_range:
      description:
        - >-
          The source port or range. Integer or range between 0 and 65535.
          Asterisk '*' can also be used to match all ports.
      returned: always
      type: str
      sample: null
    destination_port_range:
      description:
        - >-
          The destination port or range. Integer or range between 0 and 65535.
          Asterisk '*' can also be used to match all ports.
      returned: always
      type: str
      sample: null
    source_address_prefix:
      description:
        - >-
          The CIDR or source IP range. Asterisk '*' can also be used to match
          all source IPs. Default tags such as 'VirtualNetwork',
          'AzureLoadBalancer' and 'Internet' can also be used. If this is an
          ingress rule, specifies where network traffic originates from.
      returned: always
      type: str
      sample: null
    source_address_prefixes:
      description:
        - The CIDR or source IP ranges.
      returned: always
      type: list
      sample: null
    source_application_security_groups:
      description:
        - The application security group specified as source.
      returned: always
      type: list
      sample: null
    destination_address_prefix:
      description:
        - >-
          The destination address prefix. CIDR or destination IP range. Asterisk
          '*' can also be used to match all source IPs. Default tags such as
          'VirtualNetwork', 'AzureLoadBalancer' and 'Internet' can also be used.
      returned: always
      type: str
      sample: null
    destination_address_prefixes:
      description:
        - The destination address prefixes. CIDR or destination IP ranges.
      returned: always
      type: list
      sample: null
    destination_application_security_groups:
      description:
        - The application security group specified as destination.
      returned: always
      type: list
      sample: null
    source_port_ranges:
      description:
        - The source port ranges.
      returned: always
      type: list
      sample: null
    destination_port_ranges:
      description:
        - The destination port ranges.
      returned: always
      type: list
      sample: null
    access:
      description:
        - The network traffic is allowed or denied.
      returned: always
      type: str
      sample: null
    priority:
      description:
        - >-
          The priority of the rule. The value can be between 100 and 4096. The
          priority number must be unique for each rule in the collection. The
          lower the priority number, the higher the priority of the rule.
      returned: always
      type: integer
      sample: null
    direction:
      description:
        - >-
          The direction of the rule. The direction specifies if rule will be
          evaluated on incoming or outgoing traffic.
      returned: always
      type: str
      sample: null
    provisioning_state:
      description:
        - The provisioning state of the security rule resource.
      returned: always
      type: str
      sample: null
    value:
      description:
        - The security rules in a network security group.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - >-
              The name of the resource that is unique within a resource group.
              This name can be used to access the resource.
          returned: always
          type: str
          sample: null
        description:
          description:
            - A description for this rule. Restricted to 140 chars.
          returned: always
          type: str
          sample: null
        protocol:
          description:
            - Network protocol this rule applies to.
          returned: always
          type: str
          sample: null
        source_port_range:
          description:
            - >-
              The source port or range. Integer or range between 0 and 65535.
              Asterisk '*' can also be used to match all ports.
          returned: always
          type: str
          sample: null
        destination_port_range:
          description:
            - >-
              The destination port or range. Integer or range between 0 and
              65535. Asterisk '*' can also be used to match all ports.
          returned: always
          type: str
          sample: null
        source_address_prefix:
          description:
            - >-
              The CIDR or source IP range. Asterisk '*' can also be used to
              match all source IPs. Default tags such as 'VirtualNetwork',
              'AzureLoadBalancer' and 'Internet' can also be used. If this is an
              ingress rule, specifies where network traffic originates from.
          returned: always
          type: str
          sample: null
        source_address_prefixes:
          description:
            - The CIDR or source IP ranges.
          returned: always
          type: list
          sample: null
        destination_address_prefix:
          description:
            - >-
              The destination address prefix. CIDR or destination IP range.
              Asterisk '*' can also be used to match all source IPs. Default
              tags such as 'VirtualNetwork', 'AzureLoadBalancer' and 'Internet'
              can also be used.
          returned: always
          type: str
          sample: null
        destination_address_prefixes:
          description:
            - The destination address prefixes. CIDR or destination IP ranges.
          returned: always
          type: list
          sample: null
        source_port_ranges:
          description:
            - The source port ranges.
          returned: always
          type: list
          sample: null
        destination_port_ranges:
          description:
            - The destination port ranges.
          returned: always
          type: list
          sample: null
        access:
          description:
            - The network traffic is allowed or denied.
          returned: always
          type: str
          sample: null
        priority:
          description:
            - >-
              The priority of the rule. The value can be between 100 and 4096.
              The priority number must be unique for each rule in the
              collection. The lower the priority number, the higher the priority
              of the rule.
          returned: always
          type: integer
          sample: null
        direction:
          description:
            - >-
              The direction of the rule. The direction specifies if rule will be
              evaluated on incoming or outgoing traffic.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - The URL to get the next set of results.
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


class AzureRMSecurityRuleInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            network_security_group_name=dict(
                type='str',
                required=True
            ),
            security_rule_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.network_security_group_name = None
        self.security_rule_name = None

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
        super(AzureRMSecurityRuleInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01')

        if (self.resource_group_name is not None and
            self.network_security_group_name is not None and
            self.security_rule_name is not None):
            self.results['security_rules'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.network_security_group_name is not None):
            self.results['security_rules'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.security_rules.get(resource_group_name=self.resource_group_name,
                                                           network_security_group_name=self.network_security_group_name,
                                                           security_rule_name=self.security_rule_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.security_rules.list(resource_group_name=self.resource_group_name,
                                                            network_security_group_name=self.network_security_group_name)
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
    AzureRMSecurityRuleInfo()


if __name__ == '__main__':
    main()
