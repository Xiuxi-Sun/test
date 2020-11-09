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
module: azure_rm_gallery
version_added: '2.9'
short_description: Manage Azure Gallery instance.
description:
  - 'Create, update and delete instance of Azure Gallery.'
options:
  resource_group_name:
    description:
      - The name of the resource group.
    required: true
    type: str
  gallery_name:
    description:
      - >-
        The name of the Shared Image Gallery. The allowed characters are
        alphabets and numbers with dots and periods allowed in the middle. The
        maximum length is 80 characters.
      - The name of the Shared Image Gallery to be deleted.
    required: true
    type: str
  description:
    description:
      - >-
        The description of this Shared Image Gallery resource. This property is
        updatable.
    type: str
  sharing_profile:
    description:
      - Profile for gallery sharing to subscription or tenant
    type: dict
    suboptions:
      permissions:
        description:
          - >-
            This property allows you to specify the permission of sharing
            gallery. :code:`<br>`:code:`<br>` Possible values are:
            :code:`<br>`:code:`<br>` **Private** :code:`<br>`:code:`<br>`
            **Groups**
        type: str
        choices:
          - Private
          - Groups
      groups:
        description:
          - A list of sharing profile groups.
        type: list
        suboptions:
          type:
            description:
              - >-
                This property allows you to specify the type of sharing group.
                :code:`<br>`:code:`<br>` Possible values are:
                :code:`<br>`:code:`<br>` **Subscriptions**
                :code:`<br>`:code:`<br>` **AADTenants**
            type: str
            choices:
              - Subscriptions
              - AADTenants
          ids:
            description:
              - >-
                A list of subscription/tenant ids the gallery is aimed to be
                shared to.
            type: list
  select:
    description:
      - The select expression to apply on the operation.
    type: str
    choices:
      - Permissions
  state:
    description:
      - Assert the state of the Gallery.
      - >-
        Use C(present) to create or update an Gallery and C(absent) to delete
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
    - name: Create or update a simple gallery with sharing profile.
      azure_rm_gallery: 
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        location: West US
        properties:
          description: This is the gallery description.
          sharing_profile:
            permissions: Groups
        

    - name: Create or update a simple gallery.
      azure_rm_gallery: 
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        location: West US
        properties:
          description: This is the gallery description.
        

    - name: Update a simple gallery.
      azure_rm_gallery: 
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        properties:
          description: This is the gallery description.
        

    - name: Delete a gallery.
      azure_rm_gallery: 
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
id:
  description:
    - Resource Id
  returned: always
  type: str
  sample: null
name:
  description:
    - Resource name
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource type
  returned: always
  type: str
  sample: null
location:
  description:
    - Resource location
  returned: always
  type: str
  sample: null
tags:
  description:
    - Resource tags
  returned: always
  type: dictionary
  sample: null
description:
  description:
    - >-
      The description of this Shared Image Gallery resource. This property is
      updatable.
  returned: always
  type: str
  sample: null
identifier:
  description:
    - Describes the gallery unique name.
  returned: always
  type: dict
  sample: null
provisioning_state:
  description:
    - 'The provisioning state, which only appears in the response.'
  returned: always
  type: str
  sample: null
sharing_profile:
  description:
    - Profile for gallery sharing to subscription or tenant
  returned: always
  type: dict
  sample: null
  contains:
    permissions:
      description:
        - >-
          This property allows you to specify the permission of sharing gallery.
          :code:`<br>`:code:`<br>` Possible values are: :code:`<br>`:code:`<br>`
          **Private** :code:`<br>`:code:`<br>` **Groups**
      returned: always
      type: str
      sample: null
    groups:
      description:
        - A list of sharing profile groups.
      returned: always
      type: list
      sample: null
      contains:
        type:
          description:
            - >-
              This property allows you to specify the type of sharing group.
              :code:`<br>`:code:`<br>` Possible values are:
              :code:`<br>`:code:`<br>` **Subscriptions**
              :code:`<br>`:code:`<br>` **AADTenants**
          returned: always
          type: str
          sample: null
        ids:
          description:
            - >-
              A list of subscription/tenant ids the gallery is aimed to be
              shared to.
          returned: always
          type: list
          sample: null

'''

from ansible_collections.azure.azcollection.plugins.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.compute import ComputeManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMGallery(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            gallery_name=dict(
                type='str',
                required=True
            ),
            description=dict(
                type='str',
                disposition='/description'
            ),
            sharing_profile=dict(
                type='dict',
                disposition='/sharing_profile',
                options=dict(
                    permissions=dict(
                        type='str',
                        disposition='permissions',
                        choices=['Private',
                                 'Groups']
                    ),
                    groups=dict(
                        type='list',
                        updatable=False,
                        disposition='groups',
                        elements='dict',
                        options=dict(
                            type=dict(
                                type='str',
                                disposition='type',
                                choices=['Subscriptions',
                                         'AADTenants']
                            ),
                            ids=dict(
                                type='list',
                                disposition='ids',
                                elements='str'
                            )
                        )
                    )
                )
            ),
            select=dict(
                type='str',
                choices=['Permissions']
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group_name = None
        self.gallery_name = None
        self.select = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMGallery, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-09-30')

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
            response = self.mgmt_client.galleries.create_or_update(resource_group_name=self.resource_group_name,
                                                                   gallery_name=self.gallery_name,
                                                                   gallery=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Gallery instance.')
            self.fail('Error creating the Gallery instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.galleries.delete(resource_group_name=self.resource_group_name,
                                                         gallery_name=self.gallery_name)
        except CloudError as e:
            self.log('Error attempting to delete the Gallery instance.')
            self.fail('Error deleting the Gallery instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.galleries.get(resource_group_name=self.resource_group_name,
                                                      gallery_name=self.gallery_name,
                                                      select=self.select)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMGallery()


if __name__ == '__main__':
    main()
