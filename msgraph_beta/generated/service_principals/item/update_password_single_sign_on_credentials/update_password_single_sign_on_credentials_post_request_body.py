from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.credential import Credential

@dataclass
class UpdatePasswordSingleSignOnCredentialsPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The credentials property
    credentials: Optional[List[Credential]] = None
    # The id property
    id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpdatePasswordSingleSignOnCredentialsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UpdatePasswordSingleSignOnCredentialsPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UpdatePasswordSingleSignOnCredentialsPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ....models.credential import Credential

        from ....models.credential import Credential

        fields: Dict[str, Callable[[Any], None]] = {
            "credentials": lambda n : setattr(self, 'credentials', n.get_collection_of_object_values(Credential)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
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
        writer.write_collection_of_object_values("credentials", self.credentials)
        writer.write_str_value("id", self.id)
        writer.write_additional_data_value(self.additional_data)
    
