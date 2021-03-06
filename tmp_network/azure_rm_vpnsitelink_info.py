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
module: azure_rm_vpnsitelink_info
version_added: '2.9'
short_description: Get VpnSiteLink info.
description:
  - Get info of VpnSiteLink.
options:
  resource_group_name:
    description:
      - The resource group name of the VpnSite.
    required: true
    type: str
  vpn_site_name:
    description:
      - The name of the VpnSite.
    required: true
    type: str
  vpn_site_link_name:
    description:
      - The name of the VpnSiteLink being retrieved.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: VpnSiteGet
      azure_rm_vpnsitelink_info: 
        resource_group_name: rg1
        vpn_site_link_name: vpnSiteLink1
        vpn_site_name: vpnSite1
        

    - name: VpnSiteLinkListByVpnSite
      azure_rm_vpnsitelink_info: 
        resource_group_name: rg1
        vpn_site_name: vpnSite1
        

'''

RETURN = '''
vpn_site_links:
  description: >-
    A list of dict results where the key is the name of the VpnSiteLink and the
    values are the facts for that VpnSiteLink.
  returned: always
  type: complex
  contains:
    id:
      description:
        - Resource ID.
      returned: always
      type: str
      sample: null
    etag:
      description:
        - >-
          A unique read-only string that changes whenever the resource is
          updated.
      returned: always
      type: str
      sample: null
    name:
      description:
        - >-
          The name of the resource that is unique within a resource group. This
          name can be used to access the resource.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Resource type.
      returned: always
      type: str
      sample: null
    link_properties:
      description:
        - The link provider properties.
      returned: always
      type: dict
      sample: null
      contains:
        link_provider_name:
          description:
            - Name of the link provider.
          returned: always
          type: str
          sample: null
        link_speed_in_mbps:
          description:
            - Link speed.
          returned: always
          type: integer
          sample: null
    ip_address:
      description:
        - The ip-address for the vpn-site-link.
      returned: always
      type: str
      sample: null
    fqdn:
      description:
        - FQDN of vpn-site-link.
      returned: always
      type: str
      sample: null
    bgp_properties:
      description:
        - The set of bgp properties.
      returned: always
      type: dict
      sample: null
      contains:
        asn:
          description:
            - The BGP speaker's ASN.
          returned: always
          type: integer
          sample: null
        bgp_peering_address:
          description:
            - The BGP peering address and BGP identifier of this BGP speaker.
          returned: always
          type: str
          sample: null
    provisioning_state:
      description:
        - The provisioning state of the VPN site link resource.
      returned: always
      type: str
      sample: null
    value:
      description:
        - List of VpnSitesLinks.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - >-
              The name of the resource that is unique within a resource group.
              This name can be used to access the resource.
          returned: always
          type: str
          sample: null
        link_properties:
          description:
            - The link provider properties.
          returned: always
          type: dict
          sample: null
          contains:
            link_provider_name:
              description:
                - Name of the link provider.
              returned: always
              type: str
              sample: null
            link_speed_in_mbps:
              description:
                - Link speed.
              returned: always
              type: integer
              sample: null
        ip_address:
          description:
            - The ip-address for the vpn-site-link.
          returned: always
          type: str
          sample: null
        fqdn:
          description:
            - FQDN of vpn-site-link.
          returned: always
          type: str
          sample: null
        bgp_properties:
          description:
            - The set of bgp properties.
          returned: always
          type: dict
          sample: null
          contains:
            asn:
              description:
                - The BGP speaker's ASN.
              returned: always
              type: integer
              sample: null
            bgp_peering_address:
              description:
                - >-
                  The BGP peering address and BGP identifier of this BGP
                  speaker.
              returned: always
              type: str
              sample: null
    next_link:
      description:
        - URL to get the next set of operation list results if there are any.
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


class AzureRMVpnSiteLinkInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str',
                required=True
            ),
            vpn_site_name=dict(
                type='str',
                required=True
            ),
            vpn_site_link_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.vpn_site_name = None
        self.vpn_site_link_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMVpnSiteLinkInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group_name is not None and
            self.vpn_site_name is not None and
            self.vpn_site_link_name is not None):
            self.results['vpn_site_links'] = self.format_item(self.get())
        elif (self.resource_group_name is not None and
              self.vpn_site_name is not None):
            self.results['vpn_site_links'] = self.format_item(self.list_by_vpn_site())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.vpn_site_links.get(resource_group_name=self.resource_group_name,
                                                           vpn_site_name=self.vpn_site_name,
                                                           vpn_site_link_name=self.vpn_site_link_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_by_vpn_site(self):
        response = None

        try:
            response = self.mgmt_client.vpn_site_links.list_by_vpn_site(resource_group_name=self.resource_group_name,
                                                                        vpn_site_name=self.vpn_site_name)
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
    AzureRMVpnSiteLinkInfo()


if __name__ == '__main__':
    main()
