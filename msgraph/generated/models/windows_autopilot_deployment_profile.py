from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import entity, out_of_box_experience_settings, windows_autopilot_deployment_profile_assignment, windows_autopilot_device_identity, windows_autopilot_device_type, windows_enrollment_status_screen_settings

class WindowsAutopilotDeploymentProfile(entity.Entity):
    """
    Windows Autopilot Deployment Profile
    """
    @property
    def assigned_devices(self,) -> Optional[List[windows_autopilot_device_identity.WindowsAutopilotDeviceIdentity]]:
        """
        Gets the assignedDevices property value. The list of assigned devices for the profile.
        Returns: Optional[List[windows_autopilot_device_identity.WindowsAutopilotDeviceIdentity]]
        """
        return self._assigned_devices
    
    @assigned_devices.setter
    def assigned_devices(self,value: Optional[List[windows_autopilot_device_identity.WindowsAutopilotDeviceIdentity]] = None) -> None:
        """
        Sets the assignedDevices property value. The list of assigned devices for the profile.
        Args:
            value: Value to set for the assignedDevices property.
        """
        self._assigned_devices = value
    
    @property
    def assignments(self,) -> Optional[List[windows_autopilot_deployment_profile_assignment.WindowsAutopilotDeploymentProfileAssignment]]:
        """
        Gets the assignments property value. The list of group assignments for the profile.
        Returns: Optional[List[windows_autopilot_deployment_profile_assignment.WindowsAutopilotDeploymentProfileAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[windows_autopilot_deployment_profile_assignment.WindowsAutopilotDeploymentProfileAssignment]] = None) -> None:
        """
        Sets the assignments property value. The list of group assignments for the profile.
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new windowsAutopilotDeploymentProfile and sets the default values.
        """
        super().__init__()
        # The list of assigned devices for the profile.
        self._assigned_devices: Optional[List[windows_autopilot_device_identity.WindowsAutopilotDeviceIdentity]] = None
        # The list of group assignments for the profile.
        self._assignments: Optional[List[windows_autopilot_deployment_profile_assignment.WindowsAutopilotDeploymentProfileAssignment]] = None
        # Profile creation time
        self._created_date_time: Optional[datetime] = None
        # Description of the profile
        self._description: Optional[str] = None
        # The template used to name the AutoPilot Device. This can be a custom text and can also contain either the serial number of the device, or a randomly generated number. The total length of the text generated by the template can be no more than 15 characters.
        self._device_name_template: Optional[str] = None
        # The deviceType property
        self._device_type: Optional[windows_autopilot_device_type.WindowsAutopilotDeviceType] = None
        # Name of the profile
        self._display_name: Optional[str] = None
        # Enable Autopilot White Glove for the profile.
        self._enable_white_glove: Optional[bool] = None
        # Enrollment status screen setting
        self._enrollment_status_screen_settings: Optional[windows_enrollment_status_screen_settings.WindowsEnrollmentStatusScreenSettings] = None
        # HardwareHash Extraction for the profile
        self._extract_hardware_hash: Optional[bool] = None
        # Language configured on the device
        self._language: Optional[str] = None
        # Profile last modified time
        self._last_modified_date_time: Optional[datetime] = None
        # AzureAD management app ID used during client device-based enrollment discovery
        self._management_service_app_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Out of box experience setting
        self._out_of_box_experience_settings: Optional[out_of_box_experience_settings.OutOfBoxExperienceSettings] = None
        # Scope tags for the profile.
        self._role_scope_tag_ids: Optional[List[str]] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Profile creation time
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Profile creation time
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsAutopilotDeploymentProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsAutopilotDeploymentProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsAutopilotDeploymentProfile()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the profile
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the profile
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def device_name_template(self,) -> Optional[str]:
        """
        Gets the deviceNameTemplate property value. The template used to name the AutoPilot Device. This can be a custom text and can also contain either the serial number of the device, or a randomly generated number. The total length of the text generated by the template can be no more than 15 characters.
        Returns: Optional[str]
        """
        return self._device_name_template
    
    @device_name_template.setter
    def device_name_template(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceNameTemplate property value. The template used to name the AutoPilot Device. This can be a custom text and can also contain either the serial number of the device, or a randomly generated number. The total length of the text generated by the template can be no more than 15 characters.
        Args:
            value: Value to set for the deviceNameTemplate property.
        """
        self._device_name_template = value
    
    @property
    def device_type(self,) -> Optional[windows_autopilot_device_type.WindowsAutopilotDeviceType]:
        """
        Gets the deviceType property value. The deviceType property
        Returns: Optional[windows_autopilot_device_type.WindowsAutopilotDeviceType]
        """
        return self._device_type
    
    @device_type.setter
    def device_type(self,value: Optional[windows_autopilot_device_type.WindowsAutopilotDeviceType] = None) -> None:
        """
        Sets the deviceType property value. The deviceType property
        Args:
            value: Value to set for the deviceType property.
        """
        self._device_type = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Name of the profile
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Name of the profile
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def enable_white_glove(self,) -> Optional[bool]:
        """
        Gets the enableWhiteGlove property value. Enable Autopilot White Glove for the profile.
        Returns: Optional[bool]
        """
        return self._enable_white_glove
    
    @enable_white_glove.setter
    def enable_white_glove(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableWhiteGlove property value. Enable Autopilot White Glove for the profile.
        Args:
            value: Value to set for the enableWhiteGlove property.
        """
        self._enable_white_glove = value
    
    @property
    def enrollment_status_screen_settings(self,) -> Optional[windows_enrollment_status_screen_settings.WindowsEnrollmentStatusScreenSettings]:
        """
        Gets the enrollmentStatusScreenSettings property value. Enrollment status screen setting
        Returns: Optional[windows_enrollment_status_screen_settings.WindowsEnrollmentStatusScreenSettings]
        """
        return self._enrollment_status_screen_settings
    
    @enrollment_status_screen_settings.setter
    def enrollment_status_screen_settings(self,value: Optional[windows_enrollment_status_screen_settings.WindowsEnrollmentStatusScreenSettings] = None) -> None:
        """
        Sets the enrollmentStatusScreenSettings property value. Enrollment status screen setting
        Args:
            value: Value to set for the enrollmentStatusScreenSettings property.
        """
        self._enrollment_status_screen_settings = value
    
    @property
    def extract_hardware_hash(self,) -> Optional[bool]:
        """
        Gets the extractHardwareHash property value. HardwareHash Extraction for the profile
        Returns: Optional[bool]
        """
        return self._extract_hardware_hash
    
    @extract_hardware_hash.setter
    def extract_hardware_hash(self,value: Optional[bool] = None) -> None:
        """
        Sets the extractHardwareHash property value. HardwareHash Extraction for the profile
        Args:
            value: Value to set for the extractHardwareHash property.
        """
        self._extract_hardware_hash = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assigned_devices": lambda n : setattr(self, 'assigned_devices', n.get_collection_of_object_values(windows_autopilot_device_identity.WindowsAutopilotDeviceIdentity)),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(windows_autopilot_deployment_profile_assignment.WindowsAutopilotDeploymentProfileAssignment)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "device_name_template": lambda n : setattr(self, 'device_name_template', n.get_str_value()),
            "device_type": lambda n : setattr(self, 'device_type', n.get_enum_value(windows_autopilot_device_type.WindowsAutopilotDeviceType)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enable_white_glove": lambda n : setattr(self, 'enable_white_glove', n.get_bool_value()),
            "enrollment_status_screen_settings": lambda n : setattr(self, 'enrollment_status_screen_settings', n.get_object_value(windows_enrollment_status_screen_settings.WindowsEnrollmentStatusScreenSettings)),
            "extract_hardware_hash": lambda n : setattr(self, 'extract_hardware_hash', n.get_bool_value()),
            "language": lambda n : setattr(self, 'language', n.get_str_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "management_service_app_id": lambda n : setattr(self, 'management_service_app_id', n.get_str_value()),
            "out_of_box_experience_settings": lambda n : setattr(self, 'out_of_box_experience_settings', n.get_object_value(out_of_box_experience_settings.OutOfBoxExperienceSettings)),
            "role_scope_tag_ids": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def language(self,) -> Optional[str]:
        """
        Gets the language property value. Language configured on the device
        Returns: Optional[str]
        """
        return self._language
    
    @language.setter
    def language(self,value: Optional[str] = None) -> None:
        """
        Sets the language property value. Language configured on the device
        Args:
            value: Value to set for the language property.
        """
        self._language = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Profile last modified time
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Profile last modified time
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def management_service_app_id(self,) -> Optional[str]:
        """
        Gets the managementServiceAppId property value. AzureAD management app ID used during client device-based enrollment discovery
        Returns: Optional[str]
        """
        return self._management_service_app_id
    
    @management_service_app_id.setter
    def management_service_app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the managementServiceAppId property value. AzureAD management app ID used during client device-based enrollment discovery
        Args:
            value: Value to set for the managementServiceAppId property.
        """
        self._management_service_app_id = value
    
    @property
    def out_of_box_experience_settings(self,) -> Optional[out_of_box_experience_settings.OutOfBoxExperienceSettings]:
        """
        Gets the outOfBoxExperienceSettings property value. Out of box experience setting
        Returns: Optional[out_of_box_experience_settings.OutOfBoxExperienceSettings]
        """
        return self._out_of_box_experience_settings
    
    @out_of_box_experience_settings.setter
    def out_of_box_experience_settings(self,value: Optional[out_of_box_experience_settings.OutOfBoxExperienceSettings] = None) -> None:
        """
        Sets the outOfBoxExperienceSettings property value. Out of box experience setting
        Args:
            value: Value to set for the outOfBoxExperienceSettings property.
        """
        self._out_of_box_experience_settings = value
    
    @property
    def role_scope_tag_ids(self,) -> Optional[List[str]]:
        """
        Gets the roleScopeTagIds property value. Scope tags for the profile.
        Returns: Optional[List[str]]
        """
        return self._role_scope_tag_ids
    
    @role_scope_tag_ids.setter
    def role_scope_tag_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the roleScopeTagIds property value. Scope tags for the profile.
        Args:
            value: Value to set for the roleScopeTagIds property.
        """
        self._role_scope_tag_ids = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("assignedDevices", self.assigned_devices)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("deviceNameTemplate", self.device_name_template)
        writer.write_enum_value("deviceType", self.device_type)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("enableWhiteGlove", self.enable_white_glove)
        writer.write_object_value("enrollmentStatusScreenSettings", self.enrollment_status_screen_settings)
        writer.write_bool_value("extractHardwareHash", self.extract_hardware_hash)
        writer.write_str_value("language", self.language)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("managementServiceAppId", self.management_service_app_id)
        writer.write_object_value("outOfBoxExperienceSettings", self.out_of_box_experience_settings)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
    
