from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .vpn_proxy_server import VpnProxyServer

from .vpn_proxy_server import VpnProxyServer

@dataclass
class Windows10VpnProxyServer(VpnProxyServer):
    """
    VPN Proxy Server.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windows10VpnProxyServer"
    # Bypass proxy server for local address.
    bypass_proxy_server_for_local_address: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10VpnProxyServer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Windows10VpnProxyServer
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Windows10VpnProxyServer()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .vpn_proxy_server import VpnProxyServer

        from .vpn_proxy_server import VpnProxyServer

        fields: Dict[str, Callable[[Any], None]] = {
            "bypassProxyServerForLocalAddress": lambda n : setattr(self, 'bypass_proxy_server_for_local_address', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bool_value("bypassProxyServerForLocalAddress", self.bypass_proxy_server_for_local_address)
    
