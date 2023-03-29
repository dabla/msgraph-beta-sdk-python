from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_configuration, vpn_server, windows10_vpn_configuration, windows81_vpn_configuration, windows_phone81_vpn_configuration

from . import device_configuration

class WindowsVpnConfiguration(device_configuration.DeviceConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsVpnConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsVpnConfiguration"
        # Connection name displayed to the user.
        self._connection_name: Optional[str] = None
        # Custom XML commands that configures the VPN connection. (UTF8 encoded byte array)
        self._custom_xml: Optional[bytes] = None
        # List of VPN Servers on the network. Make sure end users can access these network locations. This collection can contain a maximum of 500 elements.
        self._servers: Optional[List[vpn_server.VpnServer]] = None
    
    @property
    def connection_name(self,) -> Optional[str]:
        """
        Gets the connectionName property value. Connection name displayed to the user.
        Returns: Optional[str]
        """
        return self._connection_name
    
    @connection_name.setter
    def connection_name(self,value: Optional[str] = None) -> None:
        """
        Sets the connectionName property value. Connection name displayed to the user.
        Args:
            value: Value to set for the connection_name property.
        """
        self._connection_name = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsVpnConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsVpnConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.windows10VpnConfiguration":
                from . import windows10_vpn_configuration

                return windows10_vpn_configuration.Windows10VpnConfiguration()
            if mapping_value == "#microsoft.graph.windows81VpnConfiguration":
                from . import windows81_vpn_configuration

                return windows81_vpn_configuration.Windows81VpnConfiguration()
            if mapping_value == "#microsoft.graph.windowsPhone81VpnConfiguration":
                from . import windows_phone81_vpn_configuration

                return windows_phone81_vpn_configuration.WindowsPhone81VpnConfiguration()
        return WindowsVpnConfiguration()
    
    @property
    def custom_xml(self,) -> Optional[bytes]:
        """
        Gets the customXml property value. Custom XML commands that configures the VPN connection. (UTF8 encoded byte array)
        Returns: Optional[bytes]
        """
        return self._custom_xml
    
    @custom_xml.setter
    def custom_xml(self,value: Optional[bytes] = None) -> None:
        """
        Sets the customXml property value. Custom XML commands that configures the VPN connection. (UTF8 encoded byte array)
        Args:
            value: Value to set for the custom_xml property.
        """
        self._custom_xml = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_configuration, vpn_server, windows10_vpn_configuration, windows81_vpn_configuration, windows_phone81_vpn_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "connectionName": lambda n : setattr(self, 'connection_name', n.get_str_value()),
            "customXml": lambda n : setattr(self, 'custom_xml', n.get_bytes_value()),
            "servers": lambda n : setattr(self, 'servers', n.get_collection_of_object_values(vpn_server.VpnServer)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("connectionName", self.connection_name)
        writer.write_object_value("customXml", self.custom_xml)
        writer.write_collection_of_object_values("servers", self.servers)
    
    @property
    def servers(self,) -> Optional[List[vpn_server.VpnServer]]:
        """
        Gets the servers property value. List of VPN Servers on the network. Make sure end users can access these network locations. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[vpn_server.VpnServer]]
        """
        return self._servers
    
    @servers.setter
    def servers(self,value: Optional[List[vpn_server.VpnServer]] = None) -> None:
        """
        Sets the servers property value. List of VPN Servers on the network. Make sure end users can access these network locations. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the servers property.
        """
        self._servers = value
    

