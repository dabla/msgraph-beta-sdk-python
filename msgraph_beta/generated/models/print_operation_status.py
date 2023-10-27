from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .print_operation_processing_state import PrintOperationProcessingState

@dataclass
class PrintOperationStatus(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # A human-readable description of the printOperation's current processing state. Read-only.
    description: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The state property
    state: Optional[PrintOperationProcessingState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrintOperationStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrintOperationStatus
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PrintOperationStatus()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .print_operation_processing_state import PrintOperationProcessingState

        from .print_operation_processing_state import PrintOperationProcessingState

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(PrintOperationProcessingState)),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_enum_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    
