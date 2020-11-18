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
module: azure_rm_vpnsite_info
version_added: '2.9'
short_description: Get VpnSite info.
description:
  - Get info of VpnSite.
options:
  resource_group_name:
    description:
      - The resource group name of the VpnSite.
    type: str
  vpn_site_name:
    description:
      - The name of the VpnSite being retrieved.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: VpnSiteGet
      azure_rm_vpnsite_info: 
        resource_group_name: rg1
        vpn_site_name: vpnSite1
        

    - name: VpnSiteListByResourceGroup
      azure_rm_vpnsite_info: 
        resource_group_name: rg1
        

    - name: VpnSiteList
      azure_rm_vpnsite_info: 

'''

RETURN = '''
vpn_sites:
  description: >-
    A list of dict results where the key is the name of the VpnSite and the
    values are the facts for that VpnSite.
  returned: always
  type: complex
  contains:
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
        - >-
          A unique read-only string that changes whenever the resource is
          updated.
      returned: always
      type: str
      sample: null
    virtual_wan:
      description:
        - The VirtualWAN to which the vpnSite belongs.
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
    device_properties:
      description:
        - The device properties.
      returned: always
      type: dict
      sample: null
      contains:
        device_vendor:
          description:
            - Name of the device Vendor.
          returned: always
          type: str
          sample: null
        device_model:
          description:
            - Model of the device.
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
        - The ip-address for the vpn-site.
      returned: always
      type: str
      sample: null
    site_key:
      description:
        - The key for vpn-site that can be used for connections.
      returned: always
      type: str
      sample: null
    address_space:
      description:
        - The AddressSpace that contains an array of IP address ranges.
      returned: always
      type: dict
      sample: null
      contains:
        address_prefixes:
          description:
            - >-
              A list of address blocks reserved for this virtual network in CIDR
              notation.
          returned: always
          type: list
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
        peer_weight:
          description:
            - The weight added to routes learned from this BGP speaker.
          returned: always
          type: integer
          sample: null
        bgp_peering_addresses:
          description:
            - >-
              BGP peering address with IP configuration ID for virtual network
              gateway.
          returned: always
          type: list
          sample: null
          contains:
            ipconfiguration_id:
              description:
                - The ID of IP configuration which belongs to gateway.
              returned: always
              type: str
              sample: null
            default_bgp_ip_addresses:
              description:
                - >-
                  The list of default BGP peering addresses which belong to IP
                  configuration.
              returned: always
              type: list
              sample: null
            custom_bgp_ip_addresses:
              description:
                - >-
                  The list of custom BGP peering addresses which belong to IP
                  configuration.
              returned: always
              type: list
              sample: null
            tunnel_ip_addresses:
              description:
                - >-
                  The list of tunnel public IP addresses which belong to IP
                  configuration.
              returned: always
              type: list
              sample: null
    provisioning_state:
      description:
        - The provisioning state of the VPN site resource.
      returned: always
      type: str
      sample: null
    is_security_site:
      description:
        - IsSecuritySite flag.
      returned: always
      type: bool
      sample: null
    vpn_site_links:
      description:
        - List of all vpn site links.
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
    o365_policy:
      description:
        - Office365 Policy.
      returned: always
      type: dict
      sample: null
      contains:
        break_out_categories:
          description:
            - Office365 breakout categories.
          returned: always
          type: dict
          sample: null
          contains:
            allow:
              description:
                - Flag to control allow category.
              returned: always
              type: bool
              sample: null
            optimize:
              description:
                - Flag to control optimize category.
              returned: always
              type: bool
              sample: null
            default:
              description:
                - Flag to control default category.
              returned: always
              type: bool
              sample: null
    value:
      description:
        - List of VpnSites.
      returned: always
      type: list
      sample: null
      contains:
        virtual_wan:
          description:
            - The VirtualWAN to which the vpnSite belongs.
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
        device_properties:
          description:
            - The device properties.
          returned: always
          type: dict
          sample: null
          contains:
            device_vendor:
              description:
                - Name of the device Vendor.
              returned: always
              type: str
              sample: null
            device_model:
              description:
                - Model of the device.
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
            - The ip-address for the vpn-site.
          returned: always
          type: str
          sample: null
        site_key:
          description:
            - The key for vpn-site that can be used for connections.
          returned: always
          type: str
          sample: null
        address_space:
          description:
            - The AddressSpace that contains an array of IP address ranges.
          returned: always
          type: dict
          sample: null
          contains:
            address_prefixes:
              description:
                - >-
                  A list of address blocks reserved for this virtual network in
                  CIDR notation.
              returned: always
              type: list
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
            peer_weight:
              description:
                - The weight added to routes learned from this BGP speaker.
              returned: always
              type: integer
              sample: null
            bgp_peering_addresses:
              description:
                - >-
                  BGP peering address with IP configuration ID for virtual
                  network gateway.
              returned: always
              type: list
              sample: null
              contains:
                ipconfiguration_id:
                  description:
                    - The ID of IP configuration which belongs to gateway.
                  returned: always
                  type: str
                  sample: null
                default_bgp_ip_addresses:
                  description:
                    - >-
                      The list of default BGP peering addresses which belong to
                      IP configuration.
                  returned: always
                  type: list
                  sample: null
                custom_bgp_ip_addresses:
                  description:
                    - >-
                      The list of custom BGP peering addresses which belong to
                      IP configuration.
                  returned: always
                  type: list
                  sample: null
                tunnel_ip_addresses:
                  description:
                    - >-
                      The list of tunnel public IP addresses which belong to IP
                      configuration.
                  returned: always
                  type: list
                  sample: null
        is_security_site:
          description:
            - IsSecuritySite flag.
          returned: always
          type: bool
          sample: null
        vpn_site_links:
          description:
            - List of all vpn site links.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - >-
                  The name of the resource that is unique within a resource
                  group. This name can be used to access the resource.
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
        o365_policy:
          description:
            - Office365 Policy.
          returned: always
          type: dict
          sample: null
          contains:
            break_out_categories:
              description:
                - Office365 breakout categories.
              returned: always
              type: dict
              sample: null
              contains:
                allow:
                  description:
                    - Flag to control allow category.
                  returned: always
                  type: bool
                  sample: null
                optimize:
                  description:
                    - Flag to control optimize category.
                  returned: always
                  type: bool
                  sample: null
                default:
                  description:
                    - Flag to control default category.
                  returned: always
                  type: bool
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


class AzureRMVpnSiteInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            vpn_site_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.vpn_site_name = None

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
        super(AzureRMVpnSiteInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group_name is not None and
            self.vpn_site_name is not None):
            self.results['vpn_sites'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['vpn_sites'] = self.format_item(self.list_by_resource_group())
        else:
            self.results['vpn_sites'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.vpn_sites.get(resource_group_name=self.resource_group_name,
                                                      vpn_site_name=self.vpn_site_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_by_resource_group(self):
        response = None

        try:
            response = self.mgmt_client.vpn_sites.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.vpn_sites.list()
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
    AzureRMVpnSiteInfo()


if __name__ == '__main__':
    main()
