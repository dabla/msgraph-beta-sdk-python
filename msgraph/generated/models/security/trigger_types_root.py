from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
retention_event_type = lazy_import('msgraph.generated.models.security.retention_event_type')

class TriggerTypesRoot(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new triggerTypesRoot and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The retentionEventTypes property
        self._retention_event_types: Optional[List[retention_event_type.RetentionEventType]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TriggerTypesRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TriggerTypesRoot
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TriggerTypesRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "retentionEventTypes": lambda n : setattr(self, 'retention_event_types', n.get_collection_of_object_values(retention_event_type.RetentionEventType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def retention_event_types(self,) -> Optional[List[retention_event_type.RetentionEventType]]:
        """
        Gets the retentionEventTypes property value. The retentionEventTypes property
        Returns: Optional[List[retention_event_type.RetentionEventType]]
        """
        return self._retention_event_types
    
    @retention_event_types.setter
    def retention_event_types(self,value: Optional[List[retention_event_type.RetentionEventType]] = None) -> None:
        """
        Sets the retentionEventTypes property value. The retentionEventTypes property
        Args:
            value: Value to set for the retention_event_types property.
        """
        self._retention_event_types = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("retentionEventTypes", self.retention_event_types)
    

