from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_compliance_action_item, entity

from . import entity

class DeviceManagementComplianceScheduledActionForRule(entity.Entity):
    """
    Scheduled Action for Rule
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementComplianceScheduledActionForRule and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Name of the rule which this scheduled action applies to.
        self._rule_name: Optional[str] = None
        # The list of scheduled action configurations for this compliance policy. This collection can contain a maximum of 100 elements.
        self._scheduled_action_configurations: Optional[List[device_management_compliance_action_item.DeviceManagementComplianceActionItem]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementComplianceScheduledActionForRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementComplianceScheduledActionForRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementComplianceScheduledActionForRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_compliance_action_item, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "ruleName": lambda n : setattr(self, 'rule_name', n.get_str_value()),
            "scheduledActionConfigurations": lambda n : setattr(self, 'scheduled_action_configurations', n.get_collection_of_object_values(device_management_compliance_action_item.DeviceManagementComplianceActionItem)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def rule_name(self,) -> Optional[str]:
        """
        Gets the ruleName property value. Name of the rule which this scheduled action applies to.
        Returns: Optional[str]
        """
        return self._rule_name
    
    @rule_name.setter
    def rule_name(self,value: Optional[str] = None) -> None:
        """
        Sets the ruleName property value. Name of the rule which this scheduled action applies to.
        Args:
            value: Value to set for the rule_name property.
        """
        self._rule_name = value
    
    @property
    def scheduled_action_configurations(self,) -> Optional[List[device_management_compliance_action_item.DeviceManagementComplianceActionItem]]:
        """
        Gets the scheduledActionConfigurations property value. The list of scheduled action configurations for this compliance policy. This collection can contain a maximum of 100 elements.
        Returns: Optional[List[device_management_compliance_action_item.DeviceManagementComplianceActionItem]]
        """
        return self._scheduled_action_configurations
    
    @scheduled_action_configurations.setter
    def scheduled_action_configurations(self,value: Optional[List[device_management_compliance_action_item.DeviceManagementComplianceActionItem]] = None) -> None:
        """
        Sets the scheduledActionConfigurations property value. The list of scheduled action configurations for this compliance policy. This collection can contain a maximum of 100 elements.
        Args:
            value: Value to set for the scheduled_action_configurations property.
        """
        self._scheduled_action_configurations = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("ruleName", self.rule_name)
        writer.write_collection_of_object_values("scheduledActionConfigurations", self.scheduled_action_configurations)
    

