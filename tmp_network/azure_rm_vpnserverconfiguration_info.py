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
module: azure_rm_vpnserverconfiguration_info
version_added: '2.9'
short_description: Get VpnServerConfiguration info.
description:
  - Get info of VpnServerConfiguration.
options:
  resource_group_name:
    description:
      - The resource group name of the VpnServerConfiguration.
    type: str
  vpn_server_configuration_name:
    description:
      - The name of the VpnServerConfiguration being retrieved.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: VpnServerConfigurationGet
      azure_rm_vpnserverconfiguration_info: 
        resource_group_name: rg1
        vpn_server_configuration_name: vpnServerConfiguration1
        

    - name: VpnServerConfigurationListByResourceGroup
      azure_rm_vpnserverconfiguration_info: 
        resource_group_name: rg1
        

    - name: VpnServerConfigurationList
      azure_rm_vpnserverconfiguration_info: 

'''

RETURN = '''
vpn_server_configurations:
  description: >-
    A list of dict results where the key is the name of the
    VpnServerConfiguration and the values are the facts for that
    VpnServerConfiguration.
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
    name_properties_name:
      description:
        - >-
          The name of the VpnServerConfiguration that is unique within a
          resource group.
      returned: always
      type: str
      sample: null
    vpn_protocols:
      description:
        - VPN protocols for the VpnServerConfiguration.
      returned: always
      type: list
      sample: null
    vpn_authentication_types:
      description:
        - VPN authentication types for the VpnServerConfiguration.
      returned: always
      type: list
      sample: null
    vpn_client_root_certificates:
      description:
        - VPN client root certificate of VpnServerConfiguration.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - The certificate name.
          returned: always
          type: str
          sample: null
        public_cert_data:
          description:
            - The certificate public data.
          returned: always
          type: str
          sample: null
    vpn_client_revoked_certificates:
      description:
        - VPN client revoked certificate of VpnServerConfiguration.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - The certificate name.
          returned: always
          type: str
          sample: null
        thumbprint:
          description:
            - The revoked VPN client certificate thumbprint.
          returned: always
          type: str
          sample: null
    radius_server_root_certificates:
      description:
        - Radius Server root certificate of VpnServerConfiguration.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - The certificate name.
          returned: always
          type: str
          sample: null
        public_cert_data:
          description:
            - The certificate public data.
          returned: always
          type: str
          sample: null
    radius_client_root_certificates:
      description:
        - Radius client root certificate of VpnServerConfiguration.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - The certificate name.
          returned: always
          type: str
          sample: null
        thumbprint:
          description:
            - The Radius client root certificate thumbprint.
          returned: always
          type: str
          sample: null
    vpn_client_ipsec_policies:
      description:
        - VpnClientIpsecPolicies for VpnServerConfiguration.
      returned: always
      type: list
      sample: null
      contains:
        sa_life_time_seconds:
          description:
            - >-
              The IPSec Security Association (also called Quick Mode or Phase 2
              SA) lifetime in seconds for a site to site VPN tunnel.
          returned: always
          type: integer
          sample: null
        sa_data_size_kilobytes:
          description:
            - >-
              The IPSec Security Association (also called Quick Mode or Phase 2
              SA) payload size in KB for a site to site VPN tunnel.
          returned: always
          type: integer
          sample: null
        ipsec_encryption:
          description:
            - The IPSec encryption algorithm (IKE phase 1).
          returned: always
          type: str
          sample: null
        ipsec_integrity:
          description:
            - The IPSec integrity algorithm (IKE phase 1).
          returned: always
          type: str
          sample: null
        ike_encryption:
          description:
            - The IKE encryption algorithm (IKE phase 2).
          returned: always
          type: str
          sample: null
        ike_integrity:
          description:
            - The IKE integrity algorithm (IKE phase 2).
          returned: always
          type: str
          sample: null
        dh_group:
          description:
            - The DH Group used in IKE Phase 1 for initial SA.
          returned: always
          type: str
          sample: null
        pfs_group:
          description:
            - The Pfs Group used in IKE Phase 2 for new child SA.
          returned: always
          type: str
          sample: null
    radius_server_address:
      description:
        - >-
          The radius server address property of the VpnServerConfiguration
          resource for point to site client connection.
      returned: always
      type: str
      sample: null
    radius_server_secret:
      description:
        - >-
          The radius secret property of the VpnServerConfiguration resource for
          point to site client connection.
      returned: always
      type: str
      sample: null
    radius_servers:
      description:
        - Multiple Radius Server configuration for VpnServerConfiguration.
      returned: always
      type: list
      sample: null
      contains:
        radius_server_address:
          description:
            - The address of this radius server.
          returned: always
          type: str
          sample: null
        radius_server_score:
          description:
            - The initial score assigned to this radius server.
          returned: always
          type: integer
          sample: null
        radius_server_secret:
          description:
            - The secret used for this radius server.
          returned: always
          type: str
          sample: null
    aad_authentication_parameters:
      description:
        - The set of aad vpn authentication parameters.
      returned: always
      type: dict
      sample: null
      contains:
        aad_tenant:
          description:
            - AAD Vpn authentication parameter AAD tenant.
          returned: always
          type: str
          sample: null
        aad_audience:
          description:
            - AAD Vpn authentication parameter AAD audience.
          returned: always
          type: str
          sample: null
        aad_issuer:
          description:
            - AAD Vpn authentication parameter AAD issuer.
          returned: always
          type: str
          sample: null
    provisioning_state:
      description:
        - >-
          The provisioning state of the VpnServerConfiguration resource.
          Possible values are: 'Updating', 'Deleting', and 'Failed'.
      returned: always
      type: str
      sample: null
    p2_s_vpn_gateways:
      description:
        - List of references to P2SVpnGateways.
      returned: always
      type: list
      sample: null
      contains:
        virtual_hub:
          description:
            - The VirtualHub to which the gateway belongs.
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
        p2_s_connection_configurations:
          description:
            - List of all p2s connection configurations of the gateway.
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
            vpn_client_address_pool:
              description:
                - >-
                  The reference to the address space resource which represents
                  Address space for P2S VpnClient.
              returned: always
              type: dict
              sample: null
              contains:
                address_prefixes:
                  description:
                    - >-
                      A list of address blocks reserved for this virtual network
                      in CIDR notation.
                  returned: always
                  type: list
                  sample: null
            routing_configuration:
              description:
                - >-
                  The Routing Configuration indicating the associated and
                  propagated route tables on this connection.
              returned: always
              type: dict
              sample: null
              contains:
                associated_route_table:
                  description:
                    - >-
                      The resource id RouteTable associated with this
                      RoutingConfiguration.
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
                propagated_route_tables:
                  description:
                    - The list of RouteTables to advertise the routes to.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    labels:
                      description:
                        - The list of labels.
                      returned: always
                      type: list
                      sample: null
                    ids:
                      description:
                        - The list of resource ids of all the RouteTables.
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
                vnet_routes:
                  description:
                    - >-
                      List of routes that control routing from VirtualHub into a
                      virtual network connection.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    static_routes:
                      description:
                        - List of all Static Routes.
                      returned: always
                      type: list
                      sample: null
                      contains:
                        name:
                          description:
                            - >-
                              The name of the StaticRoute that is unique within
                              a VnetRoute.
                          returned: always
                          type: str
                          sample: null
                        address_prefixes:
                          description:
                            - List of all address prefixes.
                          returned: always
                          type: list
                          sample: null
                        next_hop_ip_address:
                          description:
                            - The ip address of the next hop.
                          returned: always
                          type: str
                          sample: null
            enable_internet_security:
              description:
                - >-
                  Flag indicating whether the enable internet security flag is
                  turned on for the P2S Connections or not.
              returned: always
              type: bool
              sample: null
        vpn_gateway_scale_unit:
          description:
            - The scale unit for this p2s vpn gateway.
          returned: always
          type: integer
          sample: null
        vpn_server_configuration:
          description:
            - >-
              The VpnServerConfiguration to which the p2sVpnGateway is attached
              to.
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
        vpn_client_connection_health:
          description:
            - All P2S VPN clients' connection health status.
          returned: always
          type: dict
          sample: null
          contains:
            vpn_client_connections_count:
              description:
                - >-
                  The total of p2s vpn clients connected at this time to this
                  P2SVpnGateway.
              returned: always
              type: integer
              sample: null
            allocated_ip_addresses:
              description:
                - >-
                  List of allocated ip addresses to the connected p2s vpn
                  clients.
              returned: always
              type: list
              sample: null
        custom_dns_servers:
          description:
            - List of all customer specified DNS servers IP addresses.
          returned: always
          type: list
          sample: null
    etag_properties_etag:
      description:
        - >-
          A unique read-only string that changes whenever the resource is
          updated.
      returned: always
      type: str
      sample: null
    value:
      description:
        - List of VpnServerConfigurations.
      returned: always
      type: list
      sample: null
      contains:
        name_properties_name:
          description:
            - >-
              The name of the VpnServerConfiguration that is unique within a
              resource group.
          returned: always
          type: str
          sample: null
        vpn_protocols:
          description:
            - VPN protocols for the VpnServerConfiguration.
          returned: always
          type: list
          sample: null
        vpn_authentication_types:
          description:
            - VPN authentication types for the VpnServerConfiguration.
          returned: always
          type: list
          sample: null
        vpn_client_root_certificates:
          description:
            - VPN client root certificate of VpnServerConfiguration.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - The certificate name.
              returned: always
              type: str
              sample: null
            public_cert_data:
              description:
                - The certificate public data.
              returned: always
              type: str
              sample: null
        vpn_client_revoked_certificates:
          description:
            - VPN client revoked certificate of VpnServerConfiguration.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - The certificate name.
              returned: always
              type: str
              sample: null
            thumbprint:
              description:
                - The revoked VPN client certificate thumbprint.
              returned: always
              type: str
              sample: null
        radius_server_root_certificates:
          description:
            - Radius Server root certificate of VpnServerConfiguration.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - The certificate name.
              returned: always
              type: str
              sample: null
            public_cert_data:
              description:
                - The certificate public data.
              returned: always
              type: str
              sample: null
        radius_client_root_certificates:
          description:
            - Radius client root certificate of VpnServerConfiguration.
          returned: always
          type: list
          sample: null
          contains:
            name:
              description:
                - The certificate name.
              returned: always
              type: str
              sample: null
            thumbprint:
              description:
                - The Radius client root certificate thumbprint.
              returned: always
              type: str
              sample: null
        vpn_client_ipsec_policies:
          description:
            - VpnClientIpsecPolicies for VpnServerConfiguration.
          returned: always
          type: list
          sample: null
          contains:
            sa_life_time_seconds:
              description:
                - >-
                  The IPSec Security Association (also called Quick Mode or
                  Phase 2 SA) lifetime in seconds for a site to site VPN tunnel.
              returned: always
              type: integer
              sample: null
            sa_data_size_kilobytes:
              description:
                - >-
                  The IPSec Security Association (also called Quick Mode or
                  Phase 2 SA) payload size in KB for a site to site VPN tunnel.
              returned: always
              type: integer
              sample: null
            ipsec_encryption:
              description:
                - The IPSec encryption algorithm (IKE phase 1).
              returned: always
              type: str
              sample: null
            ipsec_integrity:
              description:
                - The IPSec integrity algorithm (IKE phase 1).
              returned: always
              type: str
              sample: null
            ike_encryption:
              description:
                - The IKE encryption algorithm (IKE phase 2).
              returned: always
              type: str
              sample: null
            ike_integrity:
              description:
                - The IKE integrity algorithm (IKE phase 2).
              returned: always
              type: str
              sample: null
            dh_group:
              description:
                - The DH Group used in IKE Phase 1 for initial SA.
              returned: always
              type: str
              sample: null
            pfs_group:
              description:
                - The Pfs Group used in IKE Phase 2 for new child SA.
              returned: always
              type: str
              sample: null
        radius_server_address:
          description:
            - >-
              The radius server address property of the VpnServerConfiguration
              resource for point to site client connection.
          returned: always
          type: str
          sample: null
        radius_server_secret:
          description:
            - >-
              The radius secret property of the VpnServerConfiguration resource
              for point to site client connection.
          returned: always
          type: str
          sample: null
        radius_servers:
          description:
            - Multiple Radius Server configuration for VpnServerConfiguration.
          returned: always
          type: list
          sample: null
          contains:
            radius_server_address:
              description:
                - The address of this radius server.
              returned: always
              type: str
              sample: null
            radius_server_score:
              description:
                - The initial score assigned to this radius server.
              returned: always
              type: integer
              sample: null
            radius_server_secret:
              description:
                - The secret used for this radius server.
              returned: always
              type: str
              sample: null
        aad_authentication_parameters:
          description:
            - The set of aad vpn authentication parameters.
          returned: always
          type: dict
          sample: null
          contains:
            aad_tenant:
              description:
                - AAD Vpn authentication parameter AAD tenant.
              returned: always
              type: str
              sample: null
            aad_audience:
              description:
                - AAD Vpn authentication parameter AAD audience.
              returned: always
              type: str
              sample: null
            aad_issuer:
              description:
                - AAD Vpn authentication parameter AAD issuer.
              returned: always
              type: str
              sample: null
        p2_s_vpn_gateways:
          description:
            - List of references to P2SVpnGateways.
          returned: always
          type: list
          sample: null
          contains:
            virtual_hub:
              description:
                - The VirtualHub to which the gateway belongs.
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
            p2_s_connection_configurations:
              description:
                - List of all p2s connection configurations of the gateway.
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
                vpn_client_address_pool:
                  description:
                    - >-
                      The reference to the address space resource which
                      represents Address space for P2S VpnClient.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    address_prefixes:
                      description:
                        - >-
                          A list of address blocks reserved for this virtual
                          network in CIDR notation.
                      returned: always
                      type: list
                      sample: null
                routing_configuration:
                  description:
                    - >-
                      The Routing Configuration indicating the associated and
                      propagated route tables on this connection.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    associated_route_table:
                      description:
                        - >-
                          The resource id RouteTable associated with this
                          RoutingConfiguration.
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
                    propagated_route_tables:
                      description:
                        - The list of RouteTables to advertise the routes to.
                      returned: always
                      type: dict
                      sample: null
                      contains:
                        labels:
                          description:
                            - The list of labels.
                          returned: always
                          type: list
                          sample: null
                        ids:
                          description:
                            - The list of resource ids of all the RouteTables.
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
                    vnet_routes:
                      description:
                        - >-
                          List of routes that control routing from VirtualHub
                          into a virtual network connection.
                      returned: always
                      type: dict
                      sample: null
                      contains:
                        static_routes:
                          description:
                            - List of all Static Routes.
                          returned: always
                          type: list
                          sample: null
                          contains:
                            name:
                              description:
                                - >-
                                  The name of the StaticRoute that is unique
                                  within a VnetRoute.
                              returned: always
                              type: str
                              sample: null
                            address_prefixes:
                              description:
                                - List of all address prefixes.
                              returned: always
                              type: list
                              sample: null
                            next_hop_ip_address:
                              description:
                                - The ip address of the next hop.
                              returned: always
                              type: str
                              sample: null
                enable_internet_security:
                  description:
                    - >-
                      Flag indicating whether the enable internet security flag
                      is turned on for the P2S Connections or not.
                  returned: always
                  type: bool
                  sample: null
            vpn_gateway_scale_unit:
              description:
                - The scale unit for this p2s vpn gateway.
              returned: always
              type: integer
              sample: null
            vpn_server_configuration:
              description:
                - >-
                  The VpnServerConfiguration to which the p2sVpnGateway is
                  attached to.
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
            vpn_client_connection_health:
              description:
                - All P2S VPN clients' connection health status.
              returned: always
              type: dict
              sample: null
              contains:
                vpn_client_connections_count:
                  description:
                    - >-
                      The total of p2s vpn clients connected at this time to
                      this P2SVpnGateway.
                  returned: always
                  type: integer
                  sample: null
                allocated_ip_addresses:
                  description:
                    - >-
                      List of allocated ip addresses to the connected p2s vpn
                      clients.
                  returned: always
                  type: list
                  sample: null
            custom_dns_servers:
              description:
                - List of all customer specified DNS servers IP addresses.
              returned: always
              type: list
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


class AzureRMVpnServerConfigurationInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            vpn_server_configuration_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.vpn_server_configuration_name = None

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
        super(AzureRMVpnServerConfigurationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group_name is not None and
            self.vpn_server_configuration_name is not None):
            self.results['vpn_server_configurations'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['vpn_server_configurations'] = self.format_item(self.list_by_resource_group())
        else:
            self.results['vpn_server_configurations'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.vpn_server_configurations.get(resource_group_name=self.resource_group_name,
                                                                      vpn_server_configuration_name=self.vpn_server_configuration_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_by_resource_group(self):
        response = None

        try:
            response = self.mgmt_client.vpn_server_configurations.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.vpn_server_configurations.list()
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
    AzureRMVpnServerConfigurationInfo()


if __name__ == '__main__':
    main()
