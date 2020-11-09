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
module: azure_rm_sharedgalleryimageversion_info
version_added: '2.9'
short_description: Get SharedGalleryImageVersion info.
description:
  - Get info of SharedGalleryImageVersion.
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
  shared_to:
    description:
      - >-
        The query parameter to decide what shared galleries to fetch when doing
        listing operations.
    type: str
    choices:
      - tenant
  gallery_image_version_name:
    description:
      - >-
        The name of the gallery image version to be created. Needs to follow
        semantic version name pattern: The allowed characters are digit and
        period. Digits must be within the range of a 32-bit integer. Format:
        :code:`<MajorVersion>`.:code:`<MinorVersion>`.:code:`<Patch>`
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a gallery.
      azure_rm_sharedgalleryimageversion_info: 
        gallery_image_name: myGalleryImageName
        gallery_unique_name: galleryUniqueName
        location: myLocation
        

'''

RETURN = '''
shared_gallery_image_versions:
  description: >-
    A list of dict results where the key is the name of the
    SharedGalleryImageVersion and the values are the facts for that
    SharedGalleryImageVersion.
  returned: always
  type: complex
  contains:
    value:
      description:
        - A list of shared gallery images versions.
      returned: always
      type: list
      sample: null
      contains:
        published_date:
          description:
            - >-
              The published date of the gallery image version Definition. This
              property can be used for decommissioning purposes. This property
              is updatable.
          returned: always
          type: str
          sample: null
        end_of_life_date:
          description:
            - >-
              The end of life date of the gallery image version Definition. This
              property can be used for decommissioning purposes. This property
              is updatable.
          returned: always
          type: str
          sample: null
    next_link:
      description:
        - >-
          The uri to fetch the next page of shared gallery image versions. Call
          ListNext() with this to fetch the next page of shared gallery image
          versions.
      returned: always
      type: str
      sample: null
    unique_id:
      description:
        - The unique id of this shared gallery.
      returned: always
      type: str
      sample: null
    published_date:
      description:
        - >-
          The published date of the gallery image version Definition. This
          property can be used for decommissioning purposes. This property is
          updatable.
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

from ansible_collections.azure.azcollection.plugins.module_utils.azure_rm_common_ext import AzureRMModuleBase
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.compute import ComputeManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMSharedGalleryImageVersionInfo(AzureRMModuleBase):
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
            shared_to=dict(
                type='str',
                choices=['tenant']
            ),
            gallery_image_version_name=dict(
                type='str'
            )
        )

        self.location = None
        self.gallery_unique_name = None
        self.gallery_image_name = None
        self.shared_to = None
        self.gallery_image_version_name = None

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
        super(AzureRMSharedGalleryImageVersionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-09-30')

        if (self.location is not None and
            self.gallery_unique_name is not None and
            self.gallery_image_name is not None and
            self.gallery_image_version_name is not None):
            self.results['shared_gallery_image_versions'] = self.format_item(self.get())
        elif (self.location is not None and
              self.gallery_unique_name is not None and
              self.gallery_image_name is not None):
            self.results['shared_gallery_image_versions'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.shared_gallery_image_versions.get(location=self.location,
                                                                          gallery_unique_name=self.gallery_unique_name,
                                                                          gallery_image_name=self.gallery_image_name,
                                                                          gallery_image_version_name=self.gallery_image_version_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.shared_gallery_image_versions.list(location=self.location,
                                                                           gallery_unique_name=self.gallery_unique_name,
                                                                           gallery_image_name=self.gallery_image_name,
                                                                           shared_to=self.shared_to)
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
    AzureRMSharedGalleryImageVersionInfo()


if __name__ == '__main__':
    main()
