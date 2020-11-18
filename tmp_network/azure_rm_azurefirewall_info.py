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
module: azure_rm_azurefirewall_info
version_added: '2.9'
short_description: Get AzureFirewall info.
description:
  - Get info of AzureFirewall.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  azure_firewall_name:
    description:
      - The name of the Azure Firewall.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get Azure Firewall
      azure_rm_azurefirewall_info: 
        azure_firewall_name: azurefirewall
        resource_group_name: rg1
        

    - name: Get Azure Firewall With Additional Properties
      azure_rm_azurefirewall_info: 
        azure_firewall_name: azurefirewall
        resource_group_name: rg1
        

    - name: Get Azure Firewall With IpGroups
      azure_rm_azurefirewall_info: 
        azure_firewall_name: azurefirewall
        resource_group_name: rg1
        

    - name: Get Azure Firewall With Zones
      azure_rm_azurefirewall_info: 
        azure_firewall_name: azurefirewall
        resource_group_name: rg1
        

    - name: Get Azure Firewall With management subnet
      azure_rm_azurefirewall_info: 
        azure_firewall_name: azurefirewall
        resource_group_name: rg1
        

    - name: List all Azure Firewalls for a given resource group
      azure_rm_azurefirewall_info: 
        resource_group_name: rg1
        

    - name: List all Azure Firewalls for a given subscription
      azure_rm_azurefirewall_info: 

'''

RETURN = '''
azure_firewalls:
  description: >-
    A list of dict results where the key is the name of the AzureFirewall and
    the values are the facts for that AzureFirewall.
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
        - Resource name.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Resource type.
      returned: always
      type: str
      sample: null
    location:
      description:
        - Resource location.
      returned: always
      type: str
      sample: null
    tags:
      description:
        - Resource tags.
      returned: always
      type: dictionary
      sample: null
    zones:
      description:
        - >-
          A list of availability zones denoting where the resource needs to come
          from.
      returned: always
      type: list
      sample: null
    etag:
      description:
        - >-
          A unique read-only string that changes whenever the resource is
          updated.
      returned: always
      type: str
      sample: null
    application_rule_collections:
      description:
        - Collection of application rule collections used by Azure Firewall.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - >-
              The name of the resource that is unique within the Azure firewall.
              This name can be used to access the resource.
          returned: always
          type: str
          sample: null
        priority:
          description:
            - Priority of the application rule collection resource.
          returned: always
          type: integer
          sample: null
        action:
          description:
            - The action type of a rule collection.
          returned: always
          type: dict
          sample: null
          contains:
            type:
              description:
                - The type of action.
              returned: always
              type: str
              sample: null
        rules:
          description:
            - Collection of rules used by a application rule collection.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - Name of the application rule.
              returned: always
              type: str
              sample: null
            description:
              description:
                - Description of the rule.
              returned: always
              type: str
              sample: null
            source_addresses:
              description:
                - List of source IP addresses for this rule.
              returned: always
              type: list
              sample: null
            protocols:
              description:
                - Array of ApplicationRuleProtocols.
              returned: always
              type: list
              sample: null
              contains:
                protocol_type:
                  description:
                    - Protocol type.
                  returned: always
                  type: str
                  sample: null
                port:
                  description:
                    - >-
                      Port number for the protocol, cannot be greater than
                      64000. This field is optional.
                  returned: always
                  type: integer
                  sample: null
            target_fqdns:
              description:
                - List of FQDNs for this rule.
              returned: always
              type: list
              sample: null
            fqdn_tags:
              description:
                - List of FQDN Tags for this rule.
              returned: always
              type: list
              sample: null
            source_ip_groups:
              description:
                - List of source IpGroups for this rule.
              returned: always
              type: list
              sample: null
    nat_rule_collections:
      description:
        - Collection of NAT rule collections used by Azure Firewall.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - >-
              The name of the resource that is unique within the Azure firewall.
              This name can be used to access the resource.
          returned: always
          type: str
          sample: null
        priority:
          description:
            - Priority of the NAT rule collection resource.
          returned: always
          type: integer
          sample: null
        action:
          description:
            - The action type of a NAT rule collection.
          returned: always
          type: dict
          sample: null
          contains:
            type:
              description:
                - The type of action.
              returned: always
              type: str
              sample: null
        rules:
          description:
            - Collection of rules used by a NAT rule collection.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - Name of the NAT rule.
              returned: always
              type: str
              sample: null
            description:
              description:
                - Description of the rule.
              returned: always
              type: str
              sample: null
            source_addresses:
              description:
                - List of source IP addresses for this rule.
              returned: always
              type: list
              sample: null
            destination_addresses:
              description:
                - >-
                  List of destination IP addresses for this rule. Supports IP
                  ranges, prefixes, and service tags.
              returned: always
              type: list
              sample: null
            destination_ports:
              description:
                - List of destination ports.
              returned: always
              type: list
              sample: null
            protocols:
              description:
                - >-
                  Array of AzureFirewallNetworkRuleProtocols applicable to this
                  NAT rule.
              returned: always
              type: list
              sample: null
            translated_address:
              description:
                - The translated address for this NAT rule.
              returned: always
              type: str
              sample: null
            translated_port:
              description:
                - The translated port for this NAT rule.
              returned: always
              type: str
              sample: null
            translated_fqdn:
              description:
                - The translated FQDN for this NAT rule.
              returned: always
              type: str
              sample: null
            source_ip_groups:
              description:
                - List of source IpGroups for this rule.
              returned: always
              type: list
              sample: null
    network_rule_collections:
      description:
        - Collection of network rule collections used by Azure Firewall.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - >-
              The name of the resource that is unique within the Azure firewall.
              This name can be used to access the resource.
          returned: always
          type: str
          sample: null
        priority:
          description:
            - Priority of the network rule collection resource.
          returned: always
          type: integer
          sample: null
        action:
          description:
            - The action type of a rule collection.
          returned: always
          type: dict
          sample: null
          contains:
            type:
              description:
                - The type of action.
              returned: always
              type: str
              sample: null
        rules:
          description:
            - Collection of rules used by a network rule collection.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - Name of the network rule.
              returned: always
              type: str
              sample: null
            description:
              description:
                - Description of the rule.
              returned: always
              type: str
              sample: null
            protocols:
              description:
                - Array of AzureFirewallNetworkRuleProtocols.
              returned: always
              type: list
              sample: null
            source_addresses:
              description:
                - List of source IP addresses for this rule.
              returned: always
              type: list
              sample: null
            destination_addresses:
              description:
                - List of destination IP addresses.
              returned: always
              type: list
              sample: null
            destination_ports:
              description:
                - List of destination ports.
              returned: always
              type: list
              sample: null
            destination_fqdns:
              description:
                - List of destination FQDNs.
              returned: always
              type: list
              sample: null
            source_ip_groups:
              description:
                - List of source IpGroups for this rule.
              returned: always
              type: list
              sample: null
            destination_ip_groups:
              description:
                - List of destination IpGroups for this rule.
              returned: always
              type: list
              sample: null
    ip_configurations:
      description:
        - IP configuration of the Azure Firewall resource.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - >-
              Name of the resource that is unique within a resource group. This
              name can be used to access the resource.
          returned: always
          type: str
          sample: null
        subnet:
          description:
            - >-
              Reference to the subnet resource. This resource must be named
              'AzureFirewallSubnet' or 'AzureFirewallManagementSubnet'.
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
        public_ip_address:
          description:
            - >-
              Reference to the PublicIP resource. This field is a mandatory
              input if subnet is not null.
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
    management_ip_configuration:
      description:
        - IP configuration of the Azure Firewall used for management traffic.
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - >-
              Name of the resource that is unique within a resource group. This
              name can be used to access the resource.
          returned: always
          type: str
          sample: null
        subnet:
          description:
            - >-
              Reference to the subnet resource. This resource must be named
              'AzureFirewallSubnet' or 'AzureFirewallManagementSubnet'.
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
        public_ip_address:
          description:
            - >-
              Reference to the PublicIP resource. This field is a mandatory
              input if subnet is not null.
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
        - The provisioning state of the Azure firewall resource.
      returned: always
      type: str
      sample: null
    threat_intel_mode:
      description:
        - The operation mode for Threat Intelligence.
      returned: always
      type: str
      sample: null
    virtual_hub:
      description:
        - The virtualHub to which the firewall belongs.
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
    firewall_policy:
      description:
        - The firewallPolicy associated with this azure firewall.
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
    hub_ip_addresses:
      description:
        - IP addresses associated with AzureFirewall.
      returned: always
      type: dict
      sample: null
      contains:
        public_i_ps:
          description:
            - Public IP addresses associated with azure firewall.
          returned: always
          type: dict
          sample: null
          contains:
            addresses:
              description:
                - >-
                  The list of Public IP addresses associated with azure firewall
                  or IP addresses to be retained.
              returned: always
              type: list
              sample: null
              contains:
                address:
                  description:
                    - Public IP Address value.
                  returned: always
                  type: str
                  sample: null
            count:
              description:
                - >-
                  The number of Public IP addresses associated with azure
                  firewall.
              returned: always
              type: integer
              sample: null
        private_ip_address:
          description:
            - Private IP Address associated with azure firewall.
          returned: always
          type: str
          sample: null
    ip_groups:
      description:
        - IpGroups associated with AzureFirewall.
      returned: always
      type: list
      sample: null
    sku:
      description:
        - The Azure Firewall Resource SKU.
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - Name of an Azure Firewall SKU.
          returned: always
          type: str
          sample: null
        tier:
          description:
            - Tier of an Azure Firewall.
          returned: always
          type: str
          sample: null
    additional_properties:
      description:
        - The additional properties used to further config this azure firewall.
      returned: always
      type: dictionary
      sample: null
    value:
      description:
        - List of Azure Firewalls in a resource group.
      returned: always
      type: list
      sample: null
      contains:
        zones:
          description:
            - >-
              A list of availability zones denoting where the resource needs to
              come from.
          returned: always
          type: list
          sample: null
        application_rule_collections:
          description:
            - Collection of application rule collections used by Azure Firewall.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - >-
                  The name of the resource that is unique within the Azure
                  firewall. This name can be used to access the resource.
              returned: always
              type: str
              sample: null
            priority:
              description:
                - Priority of the application rule collection resource.
              returned: always
              type: integer
              sample: null
            action:
              description:
                - The action type of a rule collection.
              returned: always
              type: dict
              sample: null
              contains:
                type:
                  description:
                    - The type of action.
                  returned: always
                  type: str
                  sample: null
            rules:
              description:
                - Collection of rules used by a application rule collection.
              returned: always
              type: list
              sample: null
              contains:
                name:
                  description:
                    - Name of the application rule.
                  returned: always
                  type: str
                  sample: null
                description:
                  description:
                    - Description of the rule.
                  returned: always
                  type: str
                  sample: null
                source_addresses:
                  description:
                    - List of source IP addresses for this rule.
                  returned: always
                  type: list
                  sample: null
                protocols:
                  description:
                    - Array of ApplicationRuleProtocols.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    protocol_type:
                      description:
                        - Protocol type.
                      returned: always
                      type: str
                      sample: null
                    port:
                      description:
                        - >-
                          Port number for the protocol, cannot be greater than
                          64000. This field is optional.
                      returned: always
                      type: integer
                      sample: null
                target_fqdns:
                  description:
                    - List of FQDNs for this rule.
                  returned: always
                  type: list
                  sample: null
                fqdn_tags:
                  description:
                    - List of FQDN Tags for this rule.
                  returned: always
                  type: list
                  sample: null
                source_ip_groups:
                  description:
                    - List of source IpGroups for this rule.
                  returned: always
                  type: list
                  sample: null
        nat_rule_collections:
          description:
            - Collection of NAT rule collections used by Azure Firewall.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - >-
                  The name of the resource that is unique within the Azure
                  firewall. This name can be used to access the resource.
              returned: always
              type: str
              sample: null
            priority:
              description:
                - Priority of the NAT rule collection resource.
              returned: always
              type: integer
              sample: null
            action:
              description:
                - The action type of a NAT rule collection.
              returned: always
              type: dict
              sample: null
              contains:
                type:
                  description:
                    - The type of action.
                  returned: always
                  type: str
                  sample: null
            rules:
              description:
                - Collection of rules used by a NAT rule collection.
              returned: always
              type: list
              sample: null
              contains:
                name:
                  description:
                    - Name of the NAT rule.
                  returned: always
                  type: str
                  sample: null
                description:
                  description:
                    - Description of the rule.
                  returned: always
                  type: str
                  sample: null
                source_addresses:
                  description:
                    - List of source IP addresses for this rule.
                  returned: always
                  type: list
                  sample: null
                destination_addresses:
                  description:
                    - >-
                      List of destination IP addresses for this rule. Supports
                      IP ranges, prefixes, and service tags.
                  returned: always
                  type: list
                  sample: null
                destination_ports:
                  description:
                    - List of destination ports.
                  returned: always
                  type: list
                  sample: null
                protocols:
                  description:
                    - >-
                      Array of AzureFirewallNetworkRuleProtocols applicable to
                      this NAT rule.
                  returned: always
                  type: list
                  sample: null
                translated_address:
                  description:
                    - The translated address for this NAT rule.
                  returned: always
                  type: str
                  sample: null
                translated_port:
                  description:
                    - The translated port for this NAT rule.
                  returned: always
                  type: str
                  sample: null
                translated_fqdn:
                  description:
                    - The translated FQDN for this NAT rule.
                  returned: always
                  type: str
                  sample: null
                source_ip_groups:
                  description:
                    - List of source IpGroups for this rule.
                  returned: always
                  type: list
                  sample: null
        network_rule_collections:
          description:
            - Collection of network rule collections used by Azure Firewall.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - >-
                  The name of the resource that is unique within the Azure
                  firewall. This name can be used to access the resource.
              returned: always
              type: str
              sample: null
            priority:
              description:
                - Priority of the network rule collection resource.
              returned: always
              type: integer
              sample: null
            action:
              description:
                - The action type of a rule collection.
              returned: always
              type: dict
              sample: null
              contains:
                type:
                  description:
                    - The type of action.
                  returned: always
                  type: str
                  sample: null
            rules:
              description:
                - Collection of rules used by a network rule collection.
              returned: always
              type: list
              sample: null
              contains:
                name:
                  description:
                    - Name of the network rule.
                  returned: always
                  type: str
                  sample: null
                description:
                  description:
                    - Description of the rule.
                  returned: always
                  type: str
                  sample: null
                protocols:
                  description:
                    - Array of AzureFirewallNetworkRuleProtocols.
                  returned: always
                  type: list
                  sample: null
                source_addresses:
                  description:
                    - List of source IP addresses for this rule.
                  returned: always
                  type: list
                  sample: null
                destination_addresses:
                  description:
                    - List of destination IP addresses.
                  returned: always
                  type: list
                  sample: null
                destination_ports:
                  description:
                    - List of destination ports.
                  returned: always
                  type: list
                  sample: null
                destination_fqdns:
                  description:
                    - List of destination FQDNs.
                  returned: always
                  type: list
                  sample: null
                source_ip_groups:
                  description:
                    - List of source IpGroups for this rule.
                  returned: always
                  type: list
                  sample: null
                destination_ip_groups:
                  description:
                    - List of destination IpGroups for this rule.
                  returned: always
                  type: list
                  sample: null
        ip_configurations:
          description:
            - IP configuration of the Azure Firewall resource.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - >-
                  Name of the resource that is unique within a resource group.
                  This name can be used to access the resource.
              returned: always
              type: str
              sample: null
            subnet:
              description:
                - >-
                  Reference to the subnet resource. This resource must be named
                  'AzureFirewallSubnet' or 'AzureFirewallManagementSubnet'.
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
            public_ip_address:
              description:
                - >-
                  Reference to the PublicIP resource. This field is a mandatory
                  input if subnet is not null.
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
        management_ip_configuration:
          description:
            - >-
              IP configuration of the Azure Firewall used for management
              traffic.
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - >-
                  Name of the resource that is unique within a resource group.
                  This name can be used to access the resource.
              returned: always
              type: str
              sample: null
            subnet:
              description:
                - >-
                  Reference to the subnet resource. This resource must be named
                  'AzureFirewallSubnet' or 'AzureFirewallManagementSubnet'.
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
            public_ip_address:
              description:
                - >-
                  Reference to the PublicIP resource. This field is a mandatory
                  input if subnet is not null.
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
        threat_intel_mode:
          description:
            - The operation mode for Threat Intelligence.
          returned: always
          type: str
          sample: null
        virtual_hub:
          description:
            - The virtualHub to which the firewall belongs.
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
        firewall_policy:
          description:
            - The firewallPolicy associated with this azure firewall.
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
        hub_ip_addresses:
          description:
            - IP addresses associated with AzureFirewall.
          returned: always
          type: dict
          sample: null
          contains:
            public_i_ps:
              description:
                - Public IP addresses associated with azure firewall.
              returned: always
              type: dict
              sample: null
              contains:
                addresses:
                  description:
                    - >-
                      The list of Public IP addresses associated with azure
                      firewall or IP addresses to be retained.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    address:
                      description:
                        - Public IP Address value.
                      returned: always
                      type: str
                      sample: null
                count:
                  description:
                    - >-
                      The number of Public IP addresses associated with azure
                      firewall.
                  returned: always
                  type: integer
                  sample: null
            private_ip_address:
              description:
                - Private IP Address associated with azure firewall.
              returned: always
              type: str
              sample: null
        sku:
          description:
            - The Azure Firewall Resource SKU.
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - Name of an Azure Firewall SKU.
              returned: always
              type: str
              sample: null
            tier:
              description:
                - Tier of an Azure Firewall.
              returned: always
              type: str
              sample: null
        additional_properties:
          description:
            - >-
              The additional properties used to further config this azure
              firewall.
          returned: always
          type: dictionary
          sample: null
    next_link:
      description:
        - URL to get the next set of results.
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


class AzureRMAzureFirewallInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            azure_firewall_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.azure_firewall_name = None

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
        super(AzureRMAzureFirewallInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01')

        if (self.resource_group_name is not None and
            self.azure_firewall_name is not None):
            self.results['azure_firewalls'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['azure_firewalls'] = self.format_item(self.list())
        else:
            self.results['azure_firewalls'] = self.format_item(self.list_all())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.azure_firewalls.get(resource_group_name=self.resource_group_name,
                                                            azure_firewall_name=self.azure_firewall_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.azure_firewalls.list(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_all(self):
        response = None

        try:
            response = self.mgmt_client.azure_firewalls.list_all()
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
    AzureRMAzureFirewallInfo()


if __name__ == '__main__':
    main()
