from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ChromeOSDeviceProperty(AdditionalDataHolder, BackedModel, Parsable):
    """
    Represents a property of the ChromeOS device.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Name of the property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Whether this property is updatable
    updatable: Optional[bool] = None
    # Value of the property
    value: Optional[str] = None
    # Type of the value
    value_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChromeOSDeviceProperty:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ChromeOSDeviceProperty
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ChromeOSDeviceProperty()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "updatable": lambda n : setattr(self, 'updatable', n.get_bool_value()),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
            "valueType": lambda n : setattr(self, 'value_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("name", self.name)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_bool_value("updatable", self.updatable)
        writer.write_str_value("value", self.value)
        writer.write_str_value("valueType", self.value_type)
        writer.write_additional_data_value(self.additional_data)
    

