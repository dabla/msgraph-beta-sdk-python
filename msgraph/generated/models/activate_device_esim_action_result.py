from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_action_result = lazy_import('msgraph.generated.models.device_action_result')

class ActivateDeviceEsimActionResult(device_action_result.DeviceActionResult):
    @property
    def carrier_url(self,) -> Optional[str]:
        """
        Gets the carrierUrl property value. Carrier Url to activate the device eSIM
        Returns: Optional[str]
        """
        return self._carrier_url
    
    @carrier_url.setter
    def carrier_url(self,value: Optional[str] = None) -> None:
        """
        Sets the carrierUrl property value. Carrier Url to activate the device eSIM
        Args:
            value: Value to set for the carrier_url property.
        """
        self._carrier_url = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new ActivateDeviceEsimActionResult and sets the default values.
        """
        super().__init__()
        # Carrier Url to activate the device eSIM
        self._carrier_url: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ActivateDeviceEsimActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ActivateDeviceEsimActionResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ActivateDeviceEsimActionResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "carrierUrl": lambda n : setattr(self, 'carrier_url', n.get_str_value()),
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
        writer.write_str_value("carrierUrl", self.carrier_url)
    

