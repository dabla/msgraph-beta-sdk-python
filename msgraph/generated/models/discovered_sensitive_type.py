from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .classification_attribute import ClassificationAttribute

@dataclass
class DiscoveredSensitiveType(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The classificationAttributes property
    classification_attributes: Optional[List[ClassificationAttribute]] = None
    # The confidence property
    confidence: Optional[int] = None
    # The count property
    count: Optional[int] = None
    # The id property
    id: Optional[UUID] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DiscoveredSensitiveType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DiscoveredSensitiveType
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DiscoveredSensitiveType()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .classification_attribute import ClassificationAttribute

        from .classification_attribute import ClassificationAttribute

        fields: Dict[str, Callable[[Any], None]] = {
            "classificationAttributes": lambda n : setattr(self, 'classification_attributes', n.get_collection_of_object_values(ClassificationAttribute)),
            "confidence": lambda n : setattr(self, 'confidence', n.get_int_value()),
            "count": lambda n : setattr(self, 'count', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_collection_of_object_values("classificationAttributes", self.classification_attributes)
        writer.write_int_value("confidence", self.confidence)
        writer.write_int_value("count", self.count)
        writer.write_uuid_value("id", self.id)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

