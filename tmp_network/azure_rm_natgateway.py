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
module: azure_rm_natgateway
version_added: '2.9'
short_description: Manage Azure NatGateway instance.
description:
  - 'Create, update and delete instance of Azure NatGateway.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  nat_gateway_name:
    description:
      - The name of the nat gateway.
    required: true
    type: str
  expand:
    description:
      - Expands referenced resources.
    type: str
  sku:
    description:
      - The nat gateway SKU.
    type: dict
    suboptions:
      name:
        description:
          - Name of Nat Gateway SKU.
        type: str
        choices:
          - Standard
  zones:
    description:
      - >-
        A list of availability zones denoting the zone in which Nat Gateway
        should be deployed.
    type: list
  idle_timeout_in_minutes:
    description:
      - The idle timeout of the nat gateway.
    type: integer
  public_ip_addresses:
    description:
      - >-
        An array of public ip addresses associated with the nat gateway
        resource.
    type: list
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
  public_ip_prefixes:
    description:
      - An array of public ip prefixes associated with the nat gateway resource.
    type: list
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
  subnets:
    description:
      - An array of references to the subnets using this nat gateway resource.
    type: list
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
  state:
    description:
      - Assert the state of the NatGateway.
      - >-
        Use C(present) to create or update an NatGateway and C(absent) to delete
        it.
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
    - name: Delete nat gateway
      azure_rm_natgateway: 
        nat_gateway_name: test-natGateway
        resource_group_name: rg1
        

    - name: Create nat gateway
      azure_rm_natgateway: 
        nat_gateway_name: test-natgateway
        resource_group_name: rg1
        location: westus
        properties:
          public_ip_addresses:
            - id: >-
                /subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/publicIPAddresses/PublicIpAddress1
          public_ip_prefixes:
            - id: >-
                /subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/publicIPPrefixes/PublicIpPrefix1
        sku:
          name: Standard
        

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
sku:
  description:
    - The nat gateway SKU.
  returned: always
  type: dict
  sample: null
  contains:
    name:
      description:
        - Name of Nat Gateway SKU.
      returned: always
      type: str
      sample: null
zones:
  description:
    - >-
      A list of availability zones denoting the zone in which Nat Gateway should
      be deployed.
  returned: always
  type: list
  sample: null
etag:
  description:
    - A unique read-only string that changes whenever the resource is updated.
  returned: always
  type: str
  sample: null
idle_timeout_in_minutes:
  description:
    - The idle timeout of the nat gateway.
  returned: always
  type: integer
  sample: null
public_ip_addresses:
  description:
    - An array of public ip addresses associated with the nat gateway resource.
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
public_ip_prefixes:
  description:
    - An array of public ip prefixes associated with the nat gateway resource.
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
subnets:
  description:
    - An array of references to the subnets using this nat gateway resource.
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
resource_guid:
  description:
    - The resource GUID property of the NAT gateway resource.
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - The provisioning state of the NAT gateway resource.
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


class AzureRMNatGateway(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            nat_gateway_name=dict(
                type='str',
                required=True
            ),
            expand=dict(
                type='str'
            ),
            sku=dict(
                type='dict',
                disposition='/sku',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        choices=['Standard']
                    )
                )
            ),
            zones=dict(
                type='list',
                disposition='/zones',
                elements='str'
            ),
            idle_timeout_in_minutes=dict(
                type='integer',
                disposition='/idle_timeout_in_minutes'
            ),
            public_ip_addresses=dict(
                type='list',
                disposition='/public_ip_addresses',
                elements='dict',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            public_ip_prefixes=dict(
                type='list',
                disposition='/public_ip_prefixes',
                elements='dict',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            subnets=dict(
                type='list',
                updatable=False,
                disposition='/subnets',
                elements='dict',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.nat_gateway_name = None
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMNatGateway, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.nat_gateways.create_or_update(resource_group_name=self.resource_group_name,
                                                                      nat_gateway_name=self.nat_gateway_name,
                                                                      parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the NatGateway instance.')
            self.fail('Error creating the NatGateway instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.nat_gateways.delete(resource_group_name=self.resource_group_name,
                                                            nat_gateway_name=self.nat_gateway_name)
        except CloudError as e:
            self.log('Error attempting to delete the NatGateway instance.')
            self.fail('Error deleting the NatGateway instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.nat_gateways.get(resource_group_name=self.resource_group_name,
                                                         nat_gateway_name=self.nat_gateway_name,
                                                         expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMNatGateway()


if __name__ == '__main__':
    main()
