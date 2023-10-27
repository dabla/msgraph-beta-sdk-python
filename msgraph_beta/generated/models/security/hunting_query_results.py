from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .hunting_row_result import HuntingRowResult
    from .single_property_schema import SinglePropertySchema

@dataclass
class HuntingQueryResults(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # The results of the hunting query.
    results: Optional[List[HuntingRowResult]] = None
    # The schema for the response.
    schema: Optional[List[SinglePropertySchema]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> HuntingQueryResults:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HuntingQueryResults
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return HuntingQueryResults()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .hunting_row_result import HuntingRowResult
        from .single_property_schema import SinglePropertySchema

        from .hunting_row_result import HuntingRowResult
        from .single_property_schema import SinglePropertySchema

        fields: Dict[str, Callable[[Any], None]] = {
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "results": lambda n : setattr(self, 'results', n.get_collection_of_object_values(HuntingRowResult)),
            "schema": lambda n : setattr(self, 'schema', n.get_collection_of_object_values(SinglePropertySchema)),
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
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_collection_of_object_values("results", self.results)
        writer.write_collection_of_object_values("schema", self.schema)
        writer.write_additional_data_value(self.additional_data)
    
