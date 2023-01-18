from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

directory_object = lazy_import('msgraph.generated.models.directory_object')
group = lazy_import('msgraph.generated.models.group')
privileged_access_group_eligibility_schedule = lazy_import('msgraph.generated.models.privileged_access_group_eligibility_schedule')
privileged_access_group_relationships = lazy_import('msgraph.generated.models.privileged_access_group_relationships')
privileged_access_schedule_request = lazy_import('msgraph.generated.models.privileged_access_schedule_request')

class PrivilegedAccessGroupEligibilityScheduleRequest(privileged_access_schedule_request.PrivilegedAccessScheduleRequest):
    @property
    def access_id(self,) -> Optional[privileged_access_group_relationships.PrivilegedAccessGroupRelationships]:
        """
        Gets the accessId property value. The accessId property
        Returns: Optional[privileged_access_group_relationships.PrivilegedAccessGroupRelationships]
        """
        return self._access_id
    
    @access_id.setter
    def access_id(self,value: Optional[privileged_access_group_relationships.PrivilegedAccessGroupRelationships] = None) -> None:
        """
        Sets the accessId property value. The accessId property
        Args:
            value: Value to set for the accessId property.
        """
        self._access_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new PrivilegedAccessGroupEligibilityScheduleRequest and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.privilegedAccessGroupEligibilityScheduleRequest"
        # The accessId property
        self._access_id: Optional[privileged_access_group_relationships.PrivilegedAccessGroupRelationships] = None
        # The group property
        self._group: Optional[group.Group] = None
        # The groupId property
        self._group_id: Optional[str] = None
        # The principal property
        self._principal: Optional[directory_object.DirectoryObject] = None
        # The principalId property
        self._principal_id: Optional[str] = None
        # The targetSchedule property
        self._target_schedule: Optional[privileged_access_group_eligibility_schedule.PrivilegedAccessGroupEligibilitySchedule] = None
        # The targetScheduleId property
        self._target_schedule_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrivilegedAccessGroupEligibilityScheduleRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedAccessGroupEligibilityScheduleRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrivilegedAccessGroupEligibilityScheduleRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "access_id": lambda n : setattr(self, 'access_id', n.get_enum_value(privileged_access_group_relationships.PrivilegedAccessGroupRelationships)),
            "group": lambda n : setattr(self, 'group', n.get_object_value(group.Group)),
            "group_id": lambda n : setattr(self, 'group_id', n.get_str_value()),
            "principal": lambda n : setattr(self, 'principal', n.get_object_value(directory_object.DirectoryObject)),
            "principal_id": lambda n : setattr(self, 'principal_id', n.get_str_value()),
            "target_schedule": lambda n : setattr(self, 'target_schedule', n.get_object_value(privileged_access_group_eligibility_schedule.PrivilegedAccessGroupEligibilitySchedule)),
            "target_schedule_id": lambda n : setattr(self, 'target_schedule_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group(self,) -> Optional[group.Group]:
        """
        Gets the group property value. The group property
        Returns: Optional[group.Group]
        """
        return self._group
    
    @group.setter
    def group(self,value: Optional[group.Group] = None) -> None:
        """
        Sets the group property value. The group property
        Args:
            value: Value to set for the group property.
        """
        self._group = value
    
    @property
    def group_id(self,) -> Optional[str]:
        """
        Gets the groupId property value. The groupId property
        Returns: Optional[str]
        """
        return self._group_id
    
    @group_id.setter
    def group_id(self,value: Optional[str] = None) -> None:
        """
        Sets the groupId property value. The groupId property
        Args:
            value: Value to set for the groupId property.
        """
        self._group_id = value
    
    @property
    def principal(self,) -> Optional[directory_object.DirectoryObject]:
        """
        Gets the principal property value. The principal property
        Returns: Optional[directory_object.DirectoryObject]
        """
        return self._principal
    
    @principal.setter
    def principal(self,value: Optional[directory_object.DirectoryObject] = None) -> None:
        """
        Sets the principal property value. The principal property
        Args:
            value: Value to set for the principal property.
        """
        self._principal = value
    
    @property
    def principal_id(self,) -> Optional[str]:
        """
        Gets the principalId property value. The principalId property
        Returns: Optional[str]
        """
        return self._principal_id
    
    @principal_id.setter
    def principal_id(self,value: Optional[str] = None) -> None:
        """
        Sets the principalId property value. The principalId property
        Args:
            value: Value to set for the principalId property.
        """
        self._principal_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("accessId", self.access_id)
        writer.write_object_value("group", self.group)
        writer.write_str_value("groupId", self.group_id)
        writer.write_object_value("principal", self.principal)
        writer.write_str_value("principalId", self.principal_id)
        writer.write_object_value("targetSchedule", self.target_schedule)
        writer.write_str_value("targetScheduleId", self.target_schedule_id)
    
    @property
    def target_schedule(self,) -> Optional[privileged_access_group_eligibility_schedule.PrivilegedAccessGroupEligibilitySchedule]:
        """
        Gets the targetSchedule property value. The targetSchedule property
        Returns: Optional[privileged_access_group_eligibility_schedule.PrivilegedAccessGroupEligibilitySchedule]
        """
        return self._target_schedule
    
    @target_schedule.setter
    def target_schedule(self,value: Optional[privileged_access_group_eligibility_schedule.PrivilegedAccessGroupEligibilitySchedule] = None) -> None:
        """
        Sets the targetSchedule property value. The targetSchedule property
        Args:
            value: Value to set for the targetSchedule property.
        """
        self._target_schedule = value
    
    @property
    def target_schedule_id(self,) -> Optional[str]:
        """
        Gets the targetScheduleId property value. The targetScheduleId property
        Returns: Optional[str]
        """
        return self._target_schedule_id
    
    @target_schedule_id.setter
    def target_schedule_id(self,value: Optional[str] = None) -> None:
        """
        Sets the targetScheduleId property value. The targetScheduleId property
        Args:
            value: Value to set for the targetScheduleId property.
        """
        self._target_schedule_id = value
    

