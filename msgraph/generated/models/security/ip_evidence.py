from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import alert_evidence

class IpEvidence(alert_evidence.AlertEvidence):
    def __init__(self,) -> None:
        """
        Instantiates a new IpEvidence and sets the default values.
        """
        super().__init__()
        # The value of the IP Address, can be either in V4 address or V6 address format.
        self._ip_address: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IpEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IpEvidence
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IpEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "ip_address": lambda n : setattr(self, 'ip_address', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def ip_address(self,) -> Optional[str]:
        """
        Gets the ipAddress property value. The value of the IP Address, can be either in V4 address or V6 address format.
        Returns: Optional[str]
        """
        return self._ip_address
    
    @ip_address.setter
    def ip_address(self,value: Optional[str] = None) -> None:
        """
        Sets the ipAddress property value. The value of the IP Address, can be either in V4 address or V6 address format.
        Args:
            value: Value to set for the ipAddress property.
        """
        self._ip_address = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("ipAddress", self.ip_address)
    
