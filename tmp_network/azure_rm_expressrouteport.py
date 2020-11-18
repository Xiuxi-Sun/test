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
module: azure_rm_expressrouteport
version_added: '2.9'
short_description: Manage Azure ExpressRoutePort instance.
description:
  - 'Create, update and delete instance of Azure ExpressRoutePort.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  express_route_port_name:
    description:
      - The name of the ExpressRoutePort resource.
      - The name of ExpressRoutePort.
    required: true
    type: str
  identity:
    description:
      - 'The identity of ExpressRoutePort, if configured.'
    type: dict
    suboptions:
      type:
        description:
          - >-
            The type of identity used for the resource. The type
            'SystemAssigned, UserAssigned' includes both an implicitly created
            identity and a set of user assigned identities. The type 'None' will
            remove any identities from the virtual machine.
        type: sealed-choice
      user_assigned_identities:
        description:
          - >-
            The list of user identities associated with resource. The user
            identity dictionary key references will be ARM resource ids in the
            form:
            '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
        type: dictionary
  peering_location:
    description:
      - >-
        The name of the peering location that the ExpressRoutePort is mapped to
        physically.
    type: str
  bandwidth_in_gbps:
    description:
      - Bandwidth of procured ports in Gbps.
    type: integer
  encapsulation:
    description:
      - Encapsulation method on physical ports.
    type: str
    choices:
      - Dot1Q
      - QinQ
  links:
    description:
      - The set of physical links of the ExpressRoutePort resource.
    type: list
    suboptions:
      name:
        description:
          - >-
            Name of child port resource that is unique among child port
            resources of the parent.
        type: str
      admin_state:
        description:
          - Administrative state of the physical port.
        type: str
        choices:
          - Enabled
          - Disabled
      mac_sec_config:
        description:
          - MacSec configuration.
        type: dict
        suboptions:
          ckn_secret_identifier:
            description:
              - Keyvault Secret Identifier URL containing Mac security CKN key.
            type: str
          cak_secret_identifier:
            description:
              - Keyvault Secret Identifier URL containing Mac security CAK key.
            type: str
          cipher:
            description:
              - Mac security cipher.
            type: str
            choices:
              - GcmAes256
              - GcmAes128
              - GcmAesXpn128
              - GcmAesXpn256
          sci_state:
            description:
              - Sci mode enabled/disabled.
            type: str
            choices:
              - Disabled
              - Enabled
  circuits:
    description:
      - >-
        Reference the ExpressRoute circuit(s) that are provisioned on this
        ExpressRoutePort resource.
    type: list
    suboptions:
      id:
        description:
          - Resource ID.
        type: str
  state:
    description:
      - Assert the state of the ExpressRoutePort.
      - >-
        Use C(present) to create or update an ExpressRoutePort and C(absent) to
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
    - name: ExpressRoutePortDelete
      azure_rm_expressrouteport: 
        express_route_port_name: portName
        resource_group_name: rg1
        

    - name: ExpressRoutePortCreate
      azure_rm_expressrouteport: 
        express_route_port_name: portName
        resource_group_name: rg1
        location: westus
        properties:
          bandwidth_in_gbps: 100
          encapsulation: QinQ
          peering_location: peeringLocationName
        

    - name: ExpressRoutePortUpdateLink
      azure_rm_expressrouteport: 
        express_route_port_name: portName
        resource_group_name: rg1
        location: westus
        properties:
          bandwidth_in_gbps: 100
          encapsulation: QinQ
          links:
            - name: link1
              properties:
                admin_state: Enabled
          peering_location: peeringLocationName
        

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
identity:
  description:
    - 'The identity of ExpressRoutePort, if configured.'
  returned: always
  type: dict
  sample: null
  contains:
    type:
      description:
        - >-
          The type of identity used for the resource. The type 'SystemAssigned,
          UserAssigned' includes both an implicitly created identity and a set
          of user assigned identities. The type 'None' will remove any
          identities from the virtual machine.
      returned: always
      type: sealed-choice
      sample: null
    user_assigned_identities:
      description:
        - >-
          The list of user identities associated with resource. The user
          identity dictionary key references will be ARM resource ids in the
          form:
          '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
      returned: always
      type: dictionary
      sample: null
peering_location:
  description:
    - >-
      The name of the peering location that the ExpressRoutePort is mapped to
      physically.
  returned: always
  type: str
  sample: null
bandwidth_in_gbps:
  description:
    - Bandwidth of procured ports in Gbps.
  returned: always
  type: integer
  sample: null
provisioned_bandwidth_in_gbps:
  description:
    - Aggregate Gbps of associated circuit bandwidths.
  returned: always
  type: number
  sample: null
mtu:
  description:
    - Maximum transmission unit of the physical port pair(s).
  returned: always
  type: str
  sample: null
encapsulation:
  description:
    - Encapsulation method on physical ports.
  returned: always
  type: str
  sample: null
ether_type:
  description:
    - Ether type of the physical port.
  returned: always
  type: str
  sample: null
allocation_date:
  description:
    - >-
      Date of the physical port allocation to be used in Letter of
      Authorization.
  returned: always
  type: str
  sample: null
links:
  description:
    - The set of physical links of the ExpressRoutePort resource.
  returned: always
  type: list
  sample: null
  contains:
    name:
      description:
        - >-
          Name of child port resource that is unique among child port resources
          of the parent.
      returned: always
      type: str
      sample: null
    admin_state:
      description:
        - Administrative state of the physical port.
      returned: always
      type: str
      sample: null
    mac_sec_config:
      description:
        - MacSec configuration.
      returned: always
      type: dict
      sample: null
      contains:
        ckn_secret_identifier:
          description:
            - Keyvault Secret Identifier URL containing Mac security CKN key.
          returned: always
          type: str
          sample: null
        cak_secret_identifier:
          description:
            - Keyvault Secret Identifier URL containing Mac security CAK key.
          returned: always
          type: str
          sample: null
        cipher:
          description:
            - Mac security cipher.
          returned: always
          type: str
          sample: null
        sci_state:
          description:
            - Sci mode enabled/disabled.
          returned: always
          type: str
          sample: null
circuits:
  description:
    - >-
      Reference the ExpressRoute circuit(s) that are provisioned on this
      ExpressRoutePort resource.
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
    - The provisioning state of the express route port resource.
  returned: always
  type: str
  sample: null
resource_guid:
  description:
    - The resource GUID property of the express route port resource.
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


class AzureRMExpressRoutePort(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            express_route_port_name=dict(
                type='str',
                required=True
            ),
            identity=dict(
                type='dict',
                disposition='/identity',
                options=dict(
                    type=dict(
                        type='sealed-choice',
                        disposition='type'
                    ),
                    user_assigned_identities=dict(
                        type='dictionary',
                        disposition='user_assigned_identities'
                    )
                )
            ),
            peering_location=dict(
                type='str',
                disposition='/peering_location'
            ),
            bandwidth_in_gbps=dict(
                type='integer',
                disposition='/bandwidth_in_gbps'
            ),
            encapsulation=dict(
                type='str',
                disposition='/encapsulation',
                choices=['Dot1Q',
                         'QinQ']
            ),
            links=dict(
                type='list',
                disposition='/links',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    admin_state=dict(
                        type='str',
                        disposition='admin_state',
                        choices=['Enabled',
                                 'Disabled']
                    ),
                    mac_sec_config=dict(
                        type='dict',
                        disposition='mac_sec_config',
                        options=dict(
                            ckn_secret_identifier=dict(
                                type='str',
                                disposition='ckn_secret_identifier'
                            ),
                            cak_secret_identifier=dict(
                                type='str',
                                disposition='cak_secret_identifier'
                            ),
                            cipher=dict(
                                type='str',
                                disposition='cipher',
                                choices=['GcmAes256',
                                         'GcmAes128',
                                         'GcmAesXpn128',
                                         'GcmAesXpn256']
                            ),
                            sci_state=dict(
                                type='str',
                                disposition='sci_state',
                                choices=['Disabled',
                                         'Enabled']
                            )
                        )
                    )
                )
            ),
            circuits=dict(
                type='list',
                updatable=False,
                disposition='/circuits',
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
        self.express_route_port_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMExpressRoutePort, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.express_route_ports.create_or_update(resource_group_name=self.resource_group_name,
                                                                             express_route_port_name=self.express_route_port_name,
                                                                             parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ExpressRoutePort instance.')
            self.fail('Error creating the ExpressRoutePort instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.express_route_ports.delete(resource_group_name=self.resource_group_name,
                                                                   express_route_port_name=self.express_route_port_name)
        except CloudError as e:
            self.log('Error attempting to delete the ExpressRoutePort instance.')
            self.fail('Error deleting the ExpressRoutePort instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.express_route_ports.get(resource_group_name=self.resource_group_name,
                                                                express_route_port_name=self.express_route_port_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMExpressRoutePort()


if __name__ == '__main__':
    main()
