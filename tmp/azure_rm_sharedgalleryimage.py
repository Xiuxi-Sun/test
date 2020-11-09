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
module: azure_rm_sharedgalleryimage
version_added: '2.9'
short_description: Manage Azure SharedGalleryImage instance.
description:
  - 'Create, update and delete instance of Azure SharedGalleryImage.'
options:
  location:
    description:
      - Resource location.
    required: true
    type: str
  gallery_unique_name:
    description:
      - The unique name of the Shared Gallery.
    required: true
    type: str
  gallery_image_name:
    description:
      - >-
        The name of the Shared Gallery Image Definition from which the Image
        Versions are to be listed.
    required: true
    type: str
  state:
    description:
      - Assert the state of the SharedGalleryImage.
      - >-
        Use C(present) to create or update an SharedGalleryImage and C(absent)
        to delete it.
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
'''

RETURN = '''
unique_id:
  description:
    - The unique id of this shared gallery.
  returned: always
  type: str
  sample: null
os_type:
  description:
    - >-
      This property allows you to specify the type of the OS that is included in
      the disk when creating a VM from a managed image. :code:`<br>`:code:`<br>`
      Possible values are: :code:`<br>`:code:`<br>` **Windows**
      :code:`<br>`:code:`<br>` **Linux**
  returned: always
  type: sealed-choice
  sample: null
os_state:
  description:
    - >-
      This property allows the user to specify whether the virtual machines
      created under this image are 'Generalized' or 'Specialized'.
  returned: always
  type: sealed-choice
  sample: null
end_of_life_date:
  description:
    - >-
      The end of life date of the gallery image definition. This property can be
      used for decommissioning purposes. This property is updatable.
  returned: always
  type: str
  sample: null
identifier:
  description:
    - This is the gallery image definition identifier.
  returned: always
  type: dict
  sample: null
  contains:
    publisher:
      description:
        - The name of the gallery image definition publisher.
      returned: always
      type: str
      sample: null
    offer:
      description:
        - The name of the gallery image definition offer.
      returned: always
      type: str
      sample: null
    sku:
      description:
        - The name of the gallery image definition SKU.
      returned: always
      type: str
      sample: null
recommended:
  description:
    - >-
      The properties describe the recommended machine configuration for this
      Image Definition. These properties are updatable.
  returned: always
  type: dict
  sample: null
  contains:
    v_cp_us:
      description:
        - Describes the resource range.
      returned: always
      type: dict
      sample: null
      contains:
        min:
          description:
            - The minimum number of the resource.
          returned: always
          type: integer
          sample: null
        max:
          description:
            - The maximum number of the resource.
          returned: always
          type: integer
          sample: null
    memory:
      description:
        - Describes the resource range.
      returned: always
      type: dict
      sample: null
      contains:
        min:
          description:
            - The minimum number of the resource.
          returned: always
          type: integer
          sample: null
        max:
          description:
            - The maximum number of the resource.
          returned: always
          type: integer
          sample: null
disallowed:
  description:
    - Describes the disallowed disk types.
  returned: always
  type: dict
  sample: null
  contains:
    disk_types:
      description:
        - A list of disk types.
      returned: always
      type: list
      sample: null
hyper_v_generation:
  description:
    - >-
      The hypervisor generation of the Virtual Machine. Applicable to OS disks
      only.
  returned: always
  type: str
  sample: null
features:
  description:
    - A list of gallery image features.
  returned: always
  type: list
  sample: null
  contains:
    name:
      description:
        - The name of the gallery image feature.
      returned: always
      type: str
      sample: null
    value:
      description:
        - The value of the gallery image feature.
      returned: always
      type: str
      sample: null
purchase_plan:
  description:
    - >-
      Describes the gallery image definition purchase plan. This is used by
      marketplace images.
  returned: always
  type: dict
  sample: null
  contains:
    name:
      description:
        - The plan ID.
      returned: always
      type: str
      sample: null
    publisher:
      description:
        - The publisher ID.
      returned: always
      type: str
      sample: null
    product:
      description:
        - The product ID.
      returned: always
      type: str
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


class AzureRMSharedGalleryImage(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            location=dict(
                type='str',
                required=True
            ),
            gallery_unique_name=dict(
                type='str',
                required=True
            ),
            gallery_image_name=dict(
                type='str',
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.location = None
        self.gallery_unique_name = None
        self.gallery_image_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSharedGalleryImage, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            if self.to_do == Actions.Create:
                response = self.mgmt_client.shared_gallery_images.create()
            else:
                response = self.mgmt_client.shared_gallery_images.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the SharedGalleryImage instance.')
            self.fail('Error creating the SharedGalleryImage instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.shared_gallery_images.delete()
        except CloudError as e:
            self.log('Error attempting to delete the SharedGalleryImage instance.')
            self.fail('Error deleting the SharedGalleryImage instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.shared_gallery_images.get(location=self.location,
                                                                  gallery_unique_name=self.gallery_unique_name,
                                                                  gallery_image_name=self.gallery_image_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMSharedGalleryImage()


if __name__ == '__main__':
    main()
