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
module: azure_rm_securityrule
version_added: '2.9'
short_description: Manage Azure SecurityRule instance.
description:
  - 'Create, update and delete instance of Azure SecurityRule.'
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
    required: true
    type: str
  name:
    description:
      - >-
        The name of the resource that is unique within a resource group. This
        name can be used to access the resource.
    type: str
  description:
    description:
      - A description for this rule. Restricted to 140 chars.
    type: str
  protocol:
    description:
      - Network protocol this rule applies to.
    type: str
    choices:
      - Tcp
      - Udp
      - Icmp
      - Esp
      - '*'
      - Ah
  source_port_range:
    description:
      - >-
        The source port or range. Integer or range between 0 and 65535. Asterisk
        '*' can also be used to match all ports.
    type: str
  destination_port_range:
    description:
      - >-
        The destination port or range. Integer or range between 0 and 65535.
        Asterisk '*' can also be used to match all ports.
    type: str
  source_address_prefix:
    description:
      - >-
        The CIDR or source IP range. Asterisk '*' can also be used to match all
        source IPs. Default tags such as 'VirtualNetwork', 'AzureLoadBalancer'
        and 'Internet' can also be used. If this is an ingress rule, specifies
        where network traffic originates from.
    type: str
  source_address_prefixes:
    description:
      - The CIDR or source IP ranges.
    type: list
  destination_address_prefix:
    description:
      - >-
        The destination address prefix. CIDR or destination IP range. Asterisk
        '*' can also be used to match all source IPs. Default tags such as
        'VirtualNetwork', 'AzureLoadBalancer' and 'Internet' can also be used.
    type: str
  destination_address_prefixes:
    description:
      - The destination address prefixes. CIDR or destination IP ranges.
    type: list
  source_port_ranges:
    description:
      - The source port ranges.
    type: list
  destination_port_ranges:
    description:
      - The destination port ranges.
    type: list
  access:
    description:
      - The network traffic is allowed or denied.
    type: str
    choices:
      - Allow
      - Deny
  priority:
    description:
      - >-
        The priority of the rule. The value can be between 100 and 4096. The
        priority number must be unique for each rule in the collection. The
        lower the priority number, the higher the priority of the rule.
    type: integer
  direction:
    description:
      - >-
        The direction of the rule. The direction specifies if rule will be
        evaluated on incoming or outgoing traffic.
    type: str
    choices:
      - Inbound
      - Outbound
  state:
    description:
      - Assert the state of the SecurityRule.
      - >-
        Use C(present) to create or update an SecurityRule and C(absent) to
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
    - name: Delete network security rule from network security group
      azure_rm_securityrule: 
        network_security_group_name: testnsg
        resource_group_name: rg1
        security_rule_name: rule1
        

    - name: Create security rule
      azure_rm_securityrule: 
        network_security_group_name: testnsg
        resource_group_name: rg1
        security_rule_name: rule1
        

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
      The name of the resource that is unique within a resource group. This name
      can be used to access the resource.
  returned: always
  type: str
  sample: null
etag:
  description:
    - A unique read-only string that changes whenever the resource is updated.
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
      The source port or range. Integer or range between 0 and 65535. Asterisk
      '*' can also be used to match all ports.
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
      The CIDR or source IP range. Asterisk '*' can also be used to match all
      source IPs. Default tags such as 'VirtualNetwork', 'AzureLoadBalancer' and
      'Internet' can also be used. If this is an ingress rule, specifies where
      network traffic originates from.
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
      The destination address prefix. CIDR or destination IP range. Asterisk '*'
      can also be used to match all source IPs. Default tags such as
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
      priority number must be unique for each rule in the collection. The lower
      the priority number, the higher the priority of the rule.
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


class AzureRMSecurityRule(AzureRMModuleBaseExt):
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
                type='str',
                required=True
            ),
            name=dict(
                type='str',
                disposition='/name'
            ),
            description=dict(
                type='str',
                disposition='/description'
            ),
            protocol=dict(
                type='str',
                disposition='/protocol',
                choices=['Tcp',
                         'Udp',
                         'Icmp',
                         'Esp',
                         '*',
                         'Ah']
            ),
            source_port_range=dict(
                type='str',
                disposition='/source_port_range'
            ),
            destination_port_range=dict(
                type='str',
                disposition='/destination_port_range'
            ),
            source_address_prefix=dict(
                type='str',
                disposition='/source_address_prefix'
            ),
            source_address_prefixes=dict(
                type='list',
                disposition='/source_address_prefixes',
                elements='str'
            ),
            destination_address_prefix=dict(
                type='str',
                disposition='/destination_address_prefix'
            ),
            destination_address_prefixes=dict(
                type='list',
                disposition='/destination_address_prefixes',
                elements='str'
            ),
            source_port_ranges=dict(
                type='list',
                disposition='/source_port_ranges',
                elements='str'
            ),
            destination_port_ranges=dict(
                type='list',
                disposition='/destination_port_ranges',
                elements='str'
            ),
            access=dict(
                type='str',
                disposition='/access',
                choices=['Allow',
                         'Deny']
            ),
            priority=dict(
                type='integer',
                disposition='/priority'
            ),
            direction=dict(
                type='str',
                disposition='/direction',
                choices=['Inbound',
                         'Outbound']
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.network_security_group_name = None
        self.security_rule_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSecurityRule, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.security_rules.create_or_update(resource_group_name=self.resource_group_name,
                                                                        network_security_group_name=self.network_security_group_name,
                                                                        security_rule_name=self.security_rule_name,
                                                                        security_rule_parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the SecurityRule instance.')
            self.fail('Error creating the SecurityRule instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.security_rules.delete(resource_group_name=self.resource_group_name,
                                                              network_security_group_name=self.network_security_group_name,
                                                              security_rule_name=self.security_rule_name)
        except CloudError as e:
            self.log('Error attempting to delete the SecurityRule instance.')
            self.fail('Error deleting the SecurityRule instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.security_rules.get(resource_group_name=self.resource_group_name,
                                                           network_security_group_name=self.network_security_group_name,
                                                           security_rule_name=self.security_rule_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMSecurityRule()


if __name__ == '__main__':
    main()
