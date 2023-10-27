from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity_set import IdentitySet

@dataclass
class PublicationFacet(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # User who has checked out the file.
    checked_out_by: Optional[IdentitySet] = None
    # The state of publication for this document. Either published or checkout. Read-only.
    level: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The unique identifier for the version that is visible to the current caller. Read-only.
    version_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PublicationFacet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PublicationFacet
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PublicationFacet()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .identity_set import IdentitySet

        from .identity_set import IdentitySet

        fields: Dict[str, Callable[[Any], None]] = {
            "checkedOutBy": lambda n : setattr(self, 'checked_out_by', n.get_object_value(IdentitySet)),
            "level": lambda n : setattr(self, 'level', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "versionId": lambda n : setattr(self, 'version_id', n.get_str_value()),
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
        writer.write_object_value("checkedOutBy", self.checked_out_by)
        writer.write_str_value("level", self.level)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("versionId", self.version_id)
        writer.write_additional_data_value(self.additional_data)
    
