from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import base_collection_pagination_count_response, mobile_app_relationship

class MobileAppRelationshipCollectionResponse(base_collection_pagination_count_response.BaseCollectionPaginationCountResponse):
    """
    Provides operations to manage the relationships property of the microsoft.graph.mobileApp entity.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new MobileAppRelationshipCollectionResponse and sets the default values.
        """
        super().__init__()
        # The value property
        self._value: Optional[List[mobile_app_relationship.MobileAppRelationship]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileAppRelationshipCollectionResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppRelationshipCollectionResponse
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MobileAppRelationshipCollectionResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "value": lambda n : setattr(self, 'value', n.get_collection_of_object_values(mobile_app_relationship.MobileAppRelationship)),
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
    def value(self,) -> Optional[List[mobile_app_relationship.MobileAppRelationship]]:
        """
        Gets the value property value. The value property
        Returns: Optional[List[mobile_app_relationship.MobileAppRelationship]]
        """
        return self._value
    
    @value.setter
    def value(self,value: Optional[List[mobile_app_relationship.MobileAppRelationship]] = None) -> None:
        """
        Sets the value property value. The value property
        Args:
            value: Value to set for the value property.
        """
        self._value = value
    
