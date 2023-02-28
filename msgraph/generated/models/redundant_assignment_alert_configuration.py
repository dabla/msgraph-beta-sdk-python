from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

unified_role_management_alert_configuration = lazy_import('msgraph.generated.models.unified_role_management_alert_configuration')

class RedundantAssignmentAlertConfiguration(unified_role_management_alert_configuration.UnifiedRoleManagementAlertConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new RedundantAssignmentAlertConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.redundantAssignmentAlertConfiguration"
        # The duration property
        self._duration: Optional[Timedelta] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RedundantAssignmentAlertConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RedundantAssignmentAlertConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RedundantAssignmentAlertConfiguration()
    
    @property
    def duration(self,) -> Optional[Timedelta]:
        """
        Gets the duration property value. The duration property
        Returns: Optional[Timedelta]
        """
        return self._duration
    
    @duration.setter
    def duration(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the duration property value. The duration property
        Args:
            value: Value to set for the duration property.
        """
        self._duration = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "duration": lambda n : setattr(self, 'duration', n.get_object_value(Timedelta)),
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
        writer.write_object_value("duration", self.duration)
    

