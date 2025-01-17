from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .azure_permissions_definition_action import AzurePermissionsDefinitionAction
    from .permissions_definition import PermissionsDefinition

from .permissions_definition import PermissionsDefinition

@dataclass
class SingleResourceAzurePermissionsDefinition(PermissionsDefinition):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.singleResourceAzurePermissionsDefinition"
    # The actionInfo property
    action_info: Optional[AzurePermissionsDefinitionAction] = None
    # The resourceId property
    resource_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SingleResourceAzurePermissionsDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SingleResourceAzurePermissionsDefinition
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SingleResourceAzurePermissionsDefinition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .azure_permissions_definition_action import AzurePermissionsDefinitionAction
        from .permissions_definition import PermissionsDefinition

        from .azure_permissions_definition_action import AzurePermissionsDefinitionAction
        from .permissions_definition import PermissionsDefinition

        fields: Dict[str, Callable[[Any], None]] = {
            "actionInfo": lambda n : setattr(self, 'action_info', n.get_object_value(AzurePermissionsDefinitionAction)),
            "resourceId": lambda n : setattr(self, 'resource_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("actionInfo", self.action_info)
        writer.write_str_value("resourceId", self.resource_id)
    

