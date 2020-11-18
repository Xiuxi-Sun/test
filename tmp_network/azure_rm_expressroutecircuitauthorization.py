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
module: azure_rm_expressroutecircuitauthorization
version_added: '2.9'
short_description: Manage Azure ExpressRouteCircuitAuthorization instance.
description:
  - >-
    Create, update and delete instance of Azure
    ExpressRouteCircuitAuthorization.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  circuit_name:
    description:
      - The name of the express route circuit.
    required: true
    type: str
  authorization_name:
    description:
      - The name of the authorization.
    required: true
    type: str
  name:
    description:
      - >-
        The name of the resource that is unique within a resource group. This
        name can be used to access the resource.
    type: str
  authorization_key:
    description:
      - The authorization key.
    type: str
  authorization_use_status:
    description:
      - The authorization use status.
    type: str
    choices:
      - Available
      - InUse
  state:
    description:
      - Assert the state of the ExpressRouteCircuitAuthorization.
      - >-
        Use C(present) to create or update an ExpressRouteCircuitAuthorization
        and C(absent) to delete it.
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
    - name: Delete ExpressRouteCircuit Authorization
      azure_rm_expressroutecircuitauthorization: 
        authorization_name: authorizationName
        circuit_name: circuitName
        resource_group_name: rg1
        

    - name: Create ExpressRouteCircuit Authorization
      azure_rm_expressroutecircuitauthorization: 
        authorization_name: authorizatinName
        circuit_name: circuitName
        resource_group_name: rg1
        

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
type:
  description:
    - Type of the resource.
  returned: always
  type: str
  sample: null
authorization_key:
  description:
    - The authorization key.
  returned: always
  type: str
  sample: null
authorization_use_status:
  description:
    - The authorization use status.
  returned: always
  type: str
  sample: null
provisioning_state:
  description:
    - The provisioning state of the authorization resource.
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


class AzureRMExpressRouteCircuitAuthorization(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            circuit_name=dict(
                type='str',
                required=True
            ),
            authorization_name=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str',
                disposition='/name'
            ),
            authorization_key=dict(
                type='str',
                disposition='/authorization_key'
            ),
            authorization_use_status=dict(
                type='str',
                disposition='/authorization_use_status',
                choices=['Available',
                         'InUse']
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.circuit_name = None
        self.authorization_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMExpressRouteCircuitAuthorization, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.express_route_circuit_authorizations.create_or_update(resource_group_name=self.resource_group_name,
                                                                                              circuit_name=self.circuit_name,
                                                                                              authorization_name=self.authorization_name,
                                                                                              authorization_parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ExpressRouteCircuitAuthorization instance.')
            self.fail('Error creating the ExpressRouteCircuitAuthorization instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.express_route_circuit_authorizations.delete(resource_group_name=self.resource_group_name,
                                                                                    circuit_name=self.circuit_name,
                                                                                    authorization_name=self.authorization_name)
        except CloudError as e:
            self.log('Error attempting to delete the ExpressRouteCircuitAuthorization instance.')
            self.fail('Error deleting the ExpressRouteCircuitAuthorization instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.express_route_circuit_authorizations.get(resource_group_name=self.resource_group_name,
                                                                                 circuit_name=self.circuit_name,
                                                                                 authorization_name=self.authorization_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMExpressRouteCircuitAuthorization()


if __name__ == '__main__':
    main()
