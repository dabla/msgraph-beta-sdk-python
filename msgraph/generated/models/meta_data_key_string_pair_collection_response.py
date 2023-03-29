from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import base_collection_pagination_count_response, meta_data_key_string_pair

from . import base_collection_pagination_count_response

class MetaDataKeyStringPairCollectionResponse(base_collection_pagination_count_response.BaseCollectionPaginationCountResponse):
    def __init__(self,) -> None:
        """
        Instantiates a new MetaDataKeyStringPairCollectionResponse and sets the default values.
        """
        super().__init__()
        # The value property
        self._value: Optional[List[meta_data_key_string_pair.MetaDataKeyStringPair]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MetaDataKeyStringPairCollectionResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MetaDataKeyStringPairCollectionResponse
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MetaDataKeyStringPairCollectionResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import base_collection_pagination_count_response, meta_data_key_string_pair

        fields: Dict[str, Callable[[Any], None]] = {
            "value": lambda n : setattr(self, 'value', n.get_collection_of_object_values(meta_data_key_string_pair.MetaDataKeyStringPair)),
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
        writer.write_collection_of_object_values("value", self.value)
    
    @property
    def value(self,) -> Optional[List[meta_data_key_string_pair.MetaDataKeyStringPair]]:
        """
        Gets the value property value. The value property
        Returns: Optional[List[meta_data_key_string_pair.MetaDataKeyStringPair]]
        """
        return self._value
    
    @value.setter
    def value(self,value: Optional[List[meta_data_key_string_pair.MetaDataKeyStringPair]] = None) -> None:
        """
        Sets the value property value. The value property
        Args:
            value: Value to set for the value property.
        """
        self._value = value
    

