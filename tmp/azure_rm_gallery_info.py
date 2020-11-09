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
module: azure_rm_gallery_info
version_added: '2.9'
short_description: Get Gallery info.
description:
  - Get info of Gallery.
options:
  resource_group_name:
    description:
      - The name of the resource group.
    type: str
  gallery_name:
    description:
      - The name of the Shared Image Gallery.
    type: str
  select:
    description:
      - The select expression to apply on the operation.
    type: str
    choices:
      - Permissions
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a gallery with select permissions.
      azure_rm_gallery_info: 
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        

    - name: Get a gallery.
      azure_rm_gallery_info: 
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        

    - name: List galleries in a resource group.
      azure_rm_gallery_info: 
        resource_group_name: myResourceGroup
        

    - name: List galleries in a subscription.
      azure_rm_gallery_info: 

'''

RETURN = '''
galleries:
  description: >-
    A list of dict results where the key is the name of the Gallery and the
    values are the facts for that Gallery.
  returned: always
  type: complex
  contains:
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
          The description of this Shared Image Gallery resource. This property
          is updatable.
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
              This property allows you to specify the permission of sharing
              gallery. :code:`<br>`:code:`<br>` Possible values are:
              :code:`<br>`:code:`<br>` **Private** :code:`<br>`:code:`<br>`
              **Groups**
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
    value:
      description:
        - A list of galleries.
      returned: always
      type: list
      sample: null
      contains:
        description:
          description:
            - >-
              The description of this Shared Image Gallery resource. This
              property is updatable.
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
                  This property allows you to specify the permission of sharing
                  gallery. :code:`<br>`:code:`<br>` Possible values are:
                  :code:`<br>`:code:`<br>` **Private** :code:`<br>`:code:`<br>`
                  **Groups**
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
                      This property allows you to specify the type of sharing
                      group. :code:`<br>`:code:`<br>` Possible values are:
                      :code:`<br>`:code:`<br>` **Subscriptions**
                      :code:`<br>`:code:`<br>` **AADTenants**
                  returned: always
                  type: str
                  sample: null
                ids:
                  description:
                    - >-
                      A list of subscription/tenant ids the gallery is aimed to
                      be shared to.
                  returned: always
                  type: list
                  sample: null
    next_link:
      description:
        - >-
          The uri to fetch the next page of galleries. Call ListNext() with this
          to fetch the next page of galleries.
      returned: always
      type: str
      sample: null

'''

from ansible_collections.azure.azcollection.plugins.module_utils.azure_rm_common_ext import AzureRMModuleBase
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.compute import ComputeManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMGalleryInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            gallery_name=dict(
                type='str'
            ),
            select=dict(
                type='str',
                choices=['Permissions']
            )
        )

        self.resource_group_name = None
        self.gallery_name = None
        self.select = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-09-30'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMGalleryInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-09-30')

        if (self.resource_group_name is not None and
            self.gallery_name is not None):
            self.results['galleries'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['galleries'] = self.format_item(self.list_by_resource_group())
        else:
            self.results['galleries'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.galleries.get(resource_group_name=self.resource_group_name,
                                                      gallery_name=self.gallery_name,
                                                      select=self.select)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_by_resource_group(self):
        response = None

        try:
            response = self.mgmt_client.galleries.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.galleries.list()
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
    AzureRMGalleryInfo()


if __name__ == '__main__':
    main()
