from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import unified_role_management_alert_incident

from . import unified_role_management_alert_incident

class SequentialActivationRenewalsAlertIncident(unified_role_management_alert_incident.UnifiedRoleManagementAlertIncident):
    def __init__(self,) -> None:
        """
        Instantiates a new SequentialActivationRenewalsAlertIncident and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.sequentialActivationRenewalsAlertIncident"
        # The activationCount property
        self._activation_count: Optional[int] = None
        # The assigneeDisplayName property
        self._assignee_display_name: Optional[str] = None
        # The assigneeId property
        self._assignee_id: Optional[str] = None
        # The assigneeUserPrincipalName property
        self._assignee_user_principal_name: Optional[str] = None
        # The roleDefinitionId property
        self._role_definition_id: Optional[str] = None
        # The roleDisplayName property
        self._role_display_name: Optional[str] = None
        # The roleTemplateId property
        self._role_template_id: Optional[str] = None
        # The sequenceEndDateTime property
        self._sequence_end_date_time: Optional[datetime] = None
        # The sequenceStartDateTime property
        self._sequence_start_date_time: Optional[datetime] = None
    
    @property
    def activation_count(self,) -> Optional[int]:
        """
        Gets the activationCount property value. The activationCount property
        Returns: Optional[int]
        """
        return self._activation_count
    
    @activation_count.setter
    def activation_count(self,value: Optional[int] = None) -> None:
        """
        Sets the activationCount property value. The activationCount property
        Args:
            value: Value to set for the activation_count property.
        """
        self._activation_count = value
    
    @property
    def assignee_display_name(self,) -> Optional[str]:
        """
        Gets the assigneeDisplayName property value. The assigneeDisplayName property
        Returns: Optional[str]
        """
        return self._assignee_display_name
    
    @assignee_display_name.setter
    def assignee_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the assigneeDisplayName property value. The assigneeDisplayName property
        Args:
            value: Value to set for the assignee_display_name property.
        """
        self._assignee_display_name = value
    
    @property
    def assignee_id(self,) -> Optional[str]:
        """
        Gets the assigneeId property value. The assigneeId property
        Returns: Optional[str]
        """
        return self._assignee_id
    
    @assignee_id.setter
    def assignee_id(self,value: Optional[str] = None) -> None:
        """
        Sets the assigneeId property value. The assigneeId property
        Args:
            value: Value to set for the assignee_id property.
        """
        self._assignee_id = value
    
    @property
    def assignee_user_principal_name(self,) -> Optional[str]:
        """
        Gets the assigneeUserPrincipalName property value. The assigneeUserPrincipalName property
        Returns: Optional[str]
        """
        return self._assignee_user_principal_name
    
    @assignee_user_principal_name.setter
    def assignee_user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the assigneeUserPrincipalName property value. The assigneeUserPrincipalName property
        Args:
            value: Value to set for the assignee_user_principal_name property.
        """
        self._assignee_user_principal_name = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SequentialActivationRenewalsAlertIncident:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SequentialActivationRenewalsAlertIncident
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SequentialActivationRenewalsAlertIncident()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import unified_role_management_alert_incident

        fields: Dict[str, Callable[[Any], None]] = {
            "activationCount": lambda n : setattr(self, 'activation_count', n.get_int_value()),
            "assigneeDisplayName": lambda n : setattr(self, 'assignee_display_name', n.get_str_value()),
            "assigneeId": lambda n : setattr(self, 'assignee_id', n.get_str_value()),
            "assigneeUserPrincipalName": lambda n : setattr(self, 'assignee_user_principal_name', n.get_str_value()),
            "roleDefinitionId": lambda n : setattr(self, 'role_definition_id', n.get_str_value()),
            "roleDisplayName": lambda n : setattr(self, 'role_display_name', n.get_str_value()),
            "roleTemplateId": lambda n : setattr(self, 'role_template_id', n.get_str_value()),
            "sequenceEndDateTime": lambda n : setattr(self, 'sequence_end_date_time', n.get_datetime_value()),
            "sequenceStartDateTime": lambda n : setattr(self, 'sequence_start_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def role_definition_id(self,) -> Optional[str]:
        """
        Gets the roleDefinitionId property value. The roleDefinitionId property
        Returns: Optional[str]
        """
        return self._role_definition_id
    
    @role_definition_id.setter
    def role_definition_id(self,value: Optional[str] = None) -> None:
        """
        Sets the roleDefinitionId property value. The roleDefinitionId property
        Args:
            value: Value to set for the role_definition_id property.
        """
        self._role_definition_id = value
    
    @property
    def role_display_name(self,) -> Optional[str]:
        """
        Gets the roleDisplayName property value. The roleDisplayName property
        Returns: Optional[str]
        """
        return self._role_display_name
    
    @role_display_name.setter
    def role_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the roleDisplayName property value. The roleDisplayName property
        Args:
            value: Value to set for the role_display_name property.
        """
        self._role_display_name = value
    
    @property
    def role_template_id(self,) -> Optional[str]:
        """
        Gets the roleTemplateId property value. The roleTemplateId property
        Returns: Optional[str]
        """
        return self._role_template_id
    
    @role_template_id.setter
    def role_template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the roleTemplateId property value. The roleTemplateId property
        Args:
            value: Value to set for the role_template_id property.
        """
        self._role_template_id = value
    
    @property
    def sequence_end_date_time(self,) -> Optional[datetime]:
        """
        Gets the sequenceEndDateTime property value. The sequenceEndDateTime property
        Returns: Optional[datetime]
        """
        return self._sequence_end_date_time
    
    @sequence_end_date_time.setter
    def sequence_end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the sequenceEndDateTime property value. The sequenceEndDateTime property
        Args:
            value: Value to set for the sequence_end_date_time property.
        """
        self._sequence_end_date_time = value
    
    @property
    def sequence_start_date_time(self,) -> Optional[datetime]:
        """
        Gets the sequenceStartDateTime property value. The sequenceStartDateTime property
        Returns: Optional[datetime]
        """
        return self._sequence_start_date_time
    
    @sequence_start_date_time.setter
    def sequence_start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the sequenceStartDateTime property value. The sequenceStartDateTime property
        Args:
            value: Value to set for the sequence_start_date_time property.
        """
        self._sequence_start_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("activationCount", self.activation_count)
        writer.write_str_value("assigneeDisplayName", self.assignee_display_name)
        writer.write_str_value("assigneeId", self.assignee_id)
        writer.write_str_value("assigneeUserPrincipalName", self.assignee_user_principal_name)
        writer.write_str_value("roleDefinitionId", self.role_definition_id)
        writer.write_str_value("roleDisplayName", self.role_display_name)
        writer.write_str_value("roleTemplateId", self.role_template_id)
        writer.write_datetime_value("sequenceEndDateTime", self.sequence_end_date_time)
        writer.write_datetime_value("sequenceStartDateTime", self.sequence_start_date_time)
    

