from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ControlScore(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The controlCategory property
    control_category: Optional[str] = None
    # The controlName property
    control_name: Optional[str] = None
    # The description property
    description: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The score property
    score: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ControlScore:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ControlScore
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ControlScore()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "controlCategory": lambda n : setattr(self, 'control_category', n.get_str_value()),
            "controlName": lambda n : setattr(self, 'control_name', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "score": lambda n : setattr(self, 'score', n.get_float_value()),
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
        writer.write_str_value("controlCategory", self.control_category)
        writer.write_str_value("controlName", self.control_name)
        writer.write_str_value("description", self.description)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_float_value("score", self.score)
        writer.write_additional_data_value(self.additional_data)
    
