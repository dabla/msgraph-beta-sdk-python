from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity_set import IdentitySet

@dataclass
class IncomingContext(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The id of the participant that is under observation. Read-only.
    observed_participant_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The identity that the call is happening on behalf of.
    on_behalf_of: Optional[IdentitySet] = None
    # The id of the participant that triggered the incoming call. Read-only.
    source_participant_id: Optional[str] = None
    # The identity that transferred the call.
    transferor: Optional[IdentitySet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IncomingContext:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IncomingContext
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return IncomingContext()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .identity_set import IdentitySet

        from .identity_set import IdentitySet

        fields: Dict[str, Callable[[Any], None]] = {
            "observedParticipantId": lambda n : setattr(self, 'observed_participant_id', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "onBehalfOf": lambda n : setattr(self, 'on_behalf_of', n.get_object_value(IdentitySet)),
            "sourceParticipantId": lambda n : setattr(self, 'source_participant_id', n.get_str_value()),
            "transferor": lambda n : setattr(self, 'transferor', n.get_object_value(IdentitySet)),
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
        writer.write_str_value("observedParticipantId", self.observed_participant_id)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_object_value("onBehalfOf", self.on_behalf_of)
        writer.write_str_value("sourceParticipantId", self.source_participant_id)
        writer.write_object_value("transferor", self.transferor)
        writer.write_additional_data_value(self.additional_data)
    

