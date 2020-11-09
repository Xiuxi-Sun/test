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
module: azure_rm_sharedgalleryimageversion
version_added: '2.9'
short_description: Manage Azure SharedGalleryImageVersion instance.
description:
  - 'Create, update and delete instance of Azure SharedGalleryImageVersion.'
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
  gallery_image_version_name:
    description:
      - >-
        The name of the gallery image version to be created. Needs to follow
        semantic version name pattern: The allowed characters are digit and
        period. Digits must be within the range of a 32-bit integer. Format:
        :code:`<MajorVersion>`.:code:`<MinorVersion>`.:code:`<Patch>`
    required: true
    type: str
  state:
    description:
      - Assert the state of the SharedGalleryImageVersion.
      - >-
        Use C(present) to create or update an SharedGalleryImageVersion and
        C(absent) to delete it.
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
published_date:
  description:
    - >-
      The published date of the gallery image version Definition. This property
      can be used for decommissioning purposes. This property is updatable.
  returned: always
  type: str
  sample: null
end_of_life_date:
  description:
    - >-
      The end of life date of the gallery image version Definition. This
      property can be used for decommissioning purposes. This property is
      updatable.
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


class AzureRMSharedGalleryImageVersion(AzureRMModuleBaseExt):
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
            gallery_image_version_name=dict(
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
        self.gallery_image_version_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSharedGalleryImageVersion, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                response = self.mgmt_client.shared_gallery_image_versions.create()
            else:
                response = self.mgmt_client.shared_gallery_image_versions.update()
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the SharedGalleryImageVersion instance.')
            self.fail('Error creating the SharedGalleryImageVersion instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.shared_gallery_image_versions.delete()
        except CloudError as e:
            self.log('Error attempting to delete the SharedGalleryImageVersion instance.')
            self.fail('Error deleting the SharedGalleryImageVersion instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.shared_gallery_image_versions.get(location=self.location,
                                                                          gallery_unique_name=self.gallery_unique_name,
                                                                          gallery_image_name=self.gallery_image_name,
                                                                          gallery_image_version_name=self.gallery_image_version_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMSharedGalleryImageVersion()


if __name__ == '__main__':
    main()
