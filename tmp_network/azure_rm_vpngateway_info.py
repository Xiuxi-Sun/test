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
module: azure_rm_vpngateway_info
version_added: '2.9'
short_description: Get VpnGateway info.
description:
  - Get info of VpnGateway.
options:
  resource_group_name:
    description:
      - The resource group name of the VpnGateway.
    type: str
  gateway_name:
    description:
      - The name of the gateway.
    type: str
extends_documentation_fragment:
  - azure
author:
  - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: VpnGatewayGet
      azure_rm_vpngateway_info: 
        gateway_name: gateway1
        resource_group_name: rg1
        

    - name: VpnGatewayListByResourceGroup
      azure_rm_vpngateway_info: 
        resource_group_name: rg1
        

    - name: VpnGatewayListBySubscription
      azure_rm_vpngateway_info: 

'''

RETURN = '''
vpn_gateways:
  description: >-
    A list of dict results where the key is the name of the VpnGateway and the
    values are the facts for that VpnGateway.
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
    connections:
      description:
        - List of all vpn connections to the gateway.
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
        remote_vpn_site:
          description:
            - Id of the connected vpn site.
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
        routing_weight:
          description:
            - Routing weight for vpn connection.
          returned: always
          type: integer
          sample: null
        dpd_timeout_seconds:
          description:
            - DPD timeout in seconds for vpn connection.
          returned: always
          type: integer
          sample: null
        vpn_connection_protocol_type:
          description:
            - Connection protocol used for this connection.
          returned: always
          type: str
          sample: null
        connection_bandwidth:
          description:
            - Expected bandwidth in MBPS.
          returned: always
          type: integer
          sample: null
        shared_key:
          description:
            - SharedKey for the vpn connection.
          returned: always
          type: str
          sample: null
        enable_bgp:
          description:
            - EnableBgp flag.
          returned: always
          type: bool
          sample: null
        use_policy_based_traffic_selectors:
          description:
            - Enable policy-based traffic selectors.
          returned: always
          type: bool
          sample: null
        ipsec_policies:
          description:
            - The IPSec Policies to be considered by this connection.
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
        enable_rate_limiting:
          description:
            - EnableBgp flag.
          returned: always
          type: bool
          sample: null
        enable_internet_security:
          description:
            - Enable internet security.
          returned: always
          type: bool
          sample: null
        use_local_azure_ip_address:
          description:
            - Use local azure ip to initiate connection.
          returned: always
          type: bool
          sample: null
        vpn_link_connections:
          description:
            - List of all vpn site link connections to the gateway.
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
            vpn_site_link:
              description:
                - Id of the connected vpn site link.
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
            routing_weight:
              description:
                - Routing weight for vpn connection.
              returned: always
              type: integer
              sample: null
            vpn_connection_protocol_type:
              description:
                - Connection protocol used for this connection.
              returned: always
              type: str
              sample: null
            connection_bandwidth:
              description:
                - Expected bandwidth in MBPS.
              returned: always
              type: integer
              sample: null
            shared_key:
              description:
                - SharedKey for the vpn connection.
              returned: always
              type: str
              sample: null
            enable_bgp:
              description:
                - EnableBgp flag.
              returned: always
              type: bool
              sample: null
            use_policy_based_traffic_selectors:
              description:
                - Enable policy-based traffic selectors.
              returned: always
              type: bool
              sample: null
            ipsec_policies:
              description:
                - The IPSec Policies to be considered by this connection.
              returned: always
              type: list
              sample: null
              contains:
                sa_life_time_seconds:
                  description:
                    - >-
                      The IPSec Security Association (also called Quick Mode or
                      Phase 2 SA) lifetime in seconds for a site to site VPN
                      tunnel.
                  returned: always
                  type: integer
                  sample: null
                sa_data_size_kilobytes:
                  description:
                    - >-
                      The IPSec Security Association (also called Quick Mode or
                      Phase 2 SA) payload size in KB for a site to site VPN
                      tunnel.
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
            enable_rate_limiting:
              description:
                - EnableBgp flag.
              returned: always
              type: bool
              sample: null
            use_local_azure_ip_address:
              description:
                - Use local azure ip to initiate connection.
              returned: always
              type: bool
              sample: null
        routing_configuration:
          description:
            - >-
              The Routing Configuration indicating the associated and propagated
              route tables on this connection.
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
                          The name of the StaticRoute that is unique within a
                          VnetRoute.
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
    bgp_settings:
      description:
        - Local network gateway's BGP speaker settings.
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
        - The provisioning state of the VPN gateway resource.
      returned: always
      type: str
      sample: null
    vpn_gateway_scale_unit:
      description:
        - The scale unit for this vpn gateway.
      returned: always
      type: integer
      sample: null
    ip_configurations:
      description:
        - List of all IPs configured on the gateway.
      returned: always
      type: list
      sample: null
      contains:
        id:
          description:
            - The identifier of the IP configuration for a VPN Gateway.
          returned: always
          type: str
          sample: null
        public_ip_address:
          description:
            - The public IP address of this IP configuration.
          returned: always
          type: str
          sample: null
        private_ip_address:
          description:
            - The private IP address of this IP configuration.
          returned: always
          type: str
          sample: null
    is_routing_preference_internet:
      description:
        - >-
          Enable Routing Preference property for the Public IP Interface of the
          VpnGateway.
      returned: always
      type: bool
      sample: null
    value:
      description:
        - List of VpnGateways.
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
        connections:
          description:
            - List of all vpn connections to the gateway.
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
            remote_vpn_site:
              description:
                - Id of the connected vpn site.
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
            routing_weight:
              description:
                - Routing weight for vpn connection.
              returned: always
              type: integer
              sample: null
            dpd_timeout_seconds:
              description:
                - DPD timeout in seconds for vpn connection.
              returned: always
              type: integer
              sample: null
            vpn_connection_protocol_type:
              description:
                - Connection protocol used for this connection.
              returned: always
              type: str
              sample: null
            connection_bandwidth:
              description:
                - Expected bandwidth in MBPS.
              returned: always
              type: integer
              sample: null
            shared_key:
              description:
                - SharedKey for the vpn connection.
              returned: always
              type: str
              sample: null
            enable_bgp:
              description:
                - EnableBgp flag.
              returned: always
              type: bool
              sample: null
            use_policy_based_traffic_selectors:
              description:
                - Enable policy-based traffic selectors.
              returned: always
              type: bool
              sample: null
            ipsec_policies:
              description:
                - The IPSec Policies to be considered by this connection.
              returned: always
              type: list
              sample: null
              contains:
                sa_life_time_seconds:
                  description:
                    - >-
                      The IPSec Security Association (also called Quick Mode or
                      Phase 2 SA) lifetime in seconds for a site to site VPN
                      tunnel.
                  returned: always
                  type: integer
                  sample: null
                sa_data_size_kilobytes:
                  description:
                    - >-
                      The IPSec Security Association (also called Quick Mode or
                      Phase 2 SA) payload size in KB for a site to site VPN
                      tunnel.
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
            enable_rate_limiting:
              description:
                - EnableBgp flag.
              returned: always
              type: bool
              sample: null
            enable_internet_security:
              description:
                - Enable internet security.
              returned: always
              type: bool
              sample: null
            use_local_azure_ip_address:
              description:
                - Use local azure ip to initiate connection.
              returned: always
              type: bool
              sample: null
            vpn_link_connections:
              description:
                - List of all vpn site link connections to the gateway.
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
                vpn_site_link:
                  description:
                    - Id of the connected vpn site link.
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
                routing_weight:
                  description:
                    - Routing weight for vpn connection.
                  returned: always
                  type: integer
                  sample: null
                vpn_connection_protocol_type:
                  description:
                    - Connection protocol used for this connection.
                  returned: always
                  type: str
                  sample: null
                connection_bandwidth:
                  description:
                    - Expected bandwidth in MBPS.
                  returned: always
                  type: integer
                  sample: null
                shared_key:
                  description:
                    - SharedKey for the vpn connection.
                  returned: always
                  type: str
                  sample: null
                enable_bgp:
                  description:
                    - EnableBgp flag.
                  returned: always
                  type: bool
                  sample: null
                use_policy_based_traffic_selectors:
                  description:
                    - Enable policy-based traffic selectors.
                  returned: always
                  type: bool
                  sample: null
                ipsec_policies:
                  description:
                    - The IPSec Policies to be considered by this connection.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    sa_life_time_seconds:
                      description:
                        - >-
                          The IPSec Security Association (also called Quick Mode
                          or Phase 2 SA) lifetime in seconds for a site to site
                          VPN tunnel.
                      returned: always
                      type: integer
                      sample: null
                    sa_data_size_kilobytes:
                      description:
                        - >-
                          The IPSec Security Association (also called Quick Mode
                          or Phase 2 SA) payload size in KB for a site to site
                          VPN tunnel.
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
                enable_rate_limiting:
                  description:
                    - EnableBgp flag.
                  returned: always
                  type: bool
                  sample: null
                use_local_azure_ip_address:
                  description:
                    - Use local azure ip to initiate connection.
                  returned: always
                  type: bool
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
        bgp_settings:
          description:
            - Local network gateway's BGP speaker settings.
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
        vpn_gateway_scale_unit:
          description:
            - The scale unit for this vpn gateway.
          returned: always
          type: integer
          sample: null
        ip_configurations:
          description:
            - List of all IPs configured on the gateway.
          returned: always
          type: list
          sample: null
          contains:
            id:
              description:
                - The identifier of the IP configuration for a VPN Gateway.
              returned: always
              type: str
              sample: null
            public_ip_address:
              description:
                - The public IP address of this IP configuration.
              returned: always
              type: str
              sample: null
            private_ip_address:
              description:
                - The private IP address of this IP configuration.
              returned: always
              type: str
              sample: null
        is_routing_preference_internet:
          description:
            - >-
              Enable Routing Preference property for the Public IP Interface of
              the VpnGateway.
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


class AzureRMVpnGatewayInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group_name=dict(
                type='str'
            ),
            gateway_name=dict(
                type='str'
            )
        )

        self.resource_group_name = None
        self.gateway_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-07-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMVpnGatewayInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(NetworkManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-07-01')

        if (self.resource_group_name is not None and
            self.gateway_name is not None):
            self.results['vpn_gateways'] = self.format_item(self.get())
        elif (self.resource_group_name is not None):
            self.results['vpn_gateways'] = self.format_item(self.list_by_resource_group())
        else:
            self.results['vpn_gateways'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.vpn_gateways.get(resource_group_name=self.resource_group_name,
                                                         gateway_name=self.gateway_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_by_resource_group(self):
        response = None

        try:
            response = self.mgmt_client.vpn_gateways.list_by_resource_group(resource_group_name=self.resource_group_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.vpn_gateways.list()
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
    AzureRMVpnGatewayInfo()


if __name__ == '__main__':
    main()
