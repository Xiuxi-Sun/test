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
module: azure_rm_virtualrouter
version_added: '2.9'
short_description: Manage Azure VirtualRouter instance.
description:
  - 'Create, update and delete instance of Azure VirtualRouter.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  virtual_router_name:
    description:
      - The name of the Virtual Router.
    required: true
    type: str
  expand:
    description:
      - Expands referenced resources.
    type: str
  virtual_router_asn:
    description:
      - VirtualRouter ASN.
    type: integer
  virtual_router_ips:
    description:
      - VirtualRouter IPs.
    type: list
  hosted_subnet:
    description:
      - The Subnet on which VirtualRouter is hosted.
    type: dict
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
  hosted_gateway:
    description:
      - The Gateway on which VirtualRouter is hosted.
    type: dict
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
  peerings:
    description:
      - List of references to VirtualRouterPeerings.
    type: list
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
  state:
    description:
      - Assert the state of the VirtualRouter.
      - >-
        Use C(present) to create or update an VirtualRouter and C(absent) to
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
    - name: Delete VirtualRouter
      azure_rm_virtualrouter: 
        resource_group_name: rg1
        virtual_router_name: virtualRouter
        

    - name: Create VirtualRouter
      azure_rm_virtualrouter: 
        resource_group_name: rg1
        virtual_router_name: virtualRouter
        location: West US
        properties:
          hosted_gateway:
            id: >-
              /subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/virtualNetworkGateways/vnetGateway
        tags:
          key1: value1
        

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
etag:
  description:
    - A unique read-only string that changes whenever the resource is updated.
  returned: always
  type: str
  sample: null
virtual_router_asn:
  description:
    - VirtualRouter ASN.
  returned: always
  type: integer
  sample: null
virtual_router_ips:
  description:
    - VirtualRouter IPs.
  returned: always
  type: list
  sample: null
hosted_subnet:
  description:
    - The Subnet on which VirtualRouter is hosted.
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
hosted_gateway:
  description:
    - The Gateway on which VirtualRouter is hosted.
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
peerings:
  description:
    - List of references to VirtualRouterPeerings.
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
provisioning_state:
  description:
    - The provisioning state of the resource.
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


class AzureRMVirtualRouter(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            virtual_router_name=dict(
                type='str',
                required=True
            ),
            expand=dict(
                type='str'
            ),
            virtual_router_asn=dict(
                type='integer',
                disposition='/virtual_router_asn'
            ),
            virtual_router_ips=dict(
                type='list',
                disposition='/virtual_router_ips',
                elements='str'
            ),
            hosted_subnet=dict(
                type='dict',
                disposition='/hosted_subnet',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            hosted_gateway=dict(
                type='dict',
                disposition='/hosted_gateway',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            peerings=dict(
                type='list',
                updatable=False,
                disposition='/peerings',
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
        self.virtual_router_name = None
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVirtualRouter, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.virtual_routers.create_or_update(resource_group_name=self.resource_group_name,
                                                                         virtual_router_name=self.virtual_router_name,
                                                                         parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the VirtualRouter instance.')
            self.fail('Error creating the VirtualRouter instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.virtual_routers.delete(resource_group_name=self.resource_group_name,
                                                               virtual_router_name=self.virtual_router_name)
        except CloudError as e:
            self.log('Error attempting to delete the VirtualRouter instance.')
            self.fail('Error deleting the VirtualRouter instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.virtual_routers.get(resource_group_name=self.resource_group_name,
                                                            virtual_router_name=self.virtual_router_name,
                                                            expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMVirtualRouter()


if __name__ == '__main__':
    main()
