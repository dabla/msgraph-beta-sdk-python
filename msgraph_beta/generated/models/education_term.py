from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class EducationTerm(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Display name of the term.
    display_name: Optional[str] = None
    # End of the term.
    end_date: Optional[datetime.date] = None
    # ID of term in the syncing system.
    external_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Start of the term.
    start_date: Optional[datetime.date] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationTerm:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationTerm
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EducationTerm()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "endDate": lambda n : setattr(self, 'end_date', n.get_date_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "startDate": lambda n : setattr(self, 'start_date', n.get_date_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_date_value("endDate", self.end_date)
        writer.write_str_value("externalId", self.external_id)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_date_value("startDate", self.start_date)
        writer.write_additional_data_value(self.additional_data)
    
