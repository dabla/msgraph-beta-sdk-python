from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

advanced_threat_protection_onboarding_device_setting_state = lazy_import('msgraph.generated.models.advanced_threat_protection_onboarding_device_setting_state')
entity = lazy_import('msgraph.generated.models.entity')

class AdvancedThreatProtectionOnboardingStateSummary(entity.Entity):
    @property
    def advanced_threat_protection_onboarding_device_setting_states(self,) -> Optional[List[advanced_threat_protection_onboarding_device_setting_state.AdvancedThreatProtectionOnboardingDeviceSettingState]]:
        """
        Gets the advancedThreatProtectionOnboardingDeviceSettingStates property value. Not yet documented
        Returns: Optional[List[advanced_threat_protection_onboarding_device_setting_state.AdvancedThreatProtectionOnboardingDeviceSettingState]]
        """
        return self._advanced_threat_protection_onboarding_device_setting_states
    
    @advanced_threat_protection_onboarding_device_setting_states.setter
    def advanced_threat_protection_onboarding_device_setting_states(self,value: Optional[List[advanced_threat_protection_onboarding_device_setting_state.AdvancedThreatProtectionOnboardingDeviceSettingState]] = None) -> None:
        """
        Sets the advancedThreatProtectionOnboardingDeviceSettingStates property value. Not yet documented
        Args:
            value: Value to set for the advancedThreatProtectionOnboardingDeviceSettingStates property.
        """
        self._advanced_threat_protection_onboarding_device_setting_states = value
    
    @property
    def compliant_device_count(self,) -> Optional[int]:
        """
        Gets the compliantDeviceCount property value. Number of compliant devices
        Returns: Optional[int]
        """
        return self._compliant_device_count
    
    @compliant_device_count.setter
    def compliant_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the compliantDeviceCount property value. Number of compliant devices
        Args:
            value: Value to set for the compliantDeviceCount property.
        """
        self._compliant_device_count = value
    
    @property
    def conflict_device_count(self,) -> Optional[int]:
        """
        Gets the conflictDeviceCount property value. Number of conflict devices
        Returns: Optional[int]
        """
        return self._conflict_device_count
    
    @conflict_device_count.setter
    def conflict_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the conflictDeviceCount property value. Number of conflict devices
        Args:
            value: Value to set for the conflictDeviceCount property.
        """
        self._conflict_device_count = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AdvancedThreatProtectionOnboardingStateSummary and sets the default values.
        """
        super().__init__()
        # Not yet documented
        self._advanced_threat_protection_onboarding_device_setting_states: Optional[List[advanced_threat_protection_onboarding_device_setting_state.AdvancedThreatProtectionOnboardingDeviceSettingState]] = None
        # Number of compliant devices
        self._compliant_device_count: Optional[int] = None
        # Number of conflict devices
        self._conflict_device_count: Optional[int] = None
        # Number of error devices
        self._error_device_count: Optional[int] = None
        # Number of NonCompliant devices
        self._non_compliant_device_count: Optional[int] = None
        # Number of not applicable devices
        self._not_applicable_device_count: Optional[int] = None
        # Number of not assigned devices
        self._not_assigned_device_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Number of remediated devices
        self._remediated_device_count: Optional[int] = None
        # Number of unknown devices
        self._unknown_device_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AdvancedThreatProtectionOnboardingStateSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AdvancedThreatProtectionOnboardingStateSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AdvancedThreatProtectionOnboardingStateSummary()
    
    @property
    def error_device_count(self,) -> Optional[int]:
        """
        Gets the errorDeviceCount property value. Number of error devices
        Returns: Optional[int]
        """
        return self._error_device_count
    
    @error_device_count.setter
    def error_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the errorDeviceCount property value. Number of error devices
        Args:
            value: Value to set for the errorDeviceCount property.
        """
        self._error_device_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "advanced_threat_protection_onboarding_device_setting_states": lambda n : setattr(self, 'advanced_threat_protection_onboarding_device_setting_states', n.get_collection_of_object_values(advanced_threat_protection_onboarding_device_setting_state.AdvancedThreatProtectionOnboardingDeviceSettingState)),
            "compliant_device_count": lambda n : setattr(self, 'compliant_device_count', n.get_int_value()),
            "conflict_device_count": lambda n : setattr(self, 'conflict_device_count', n.get_int_value()),
            "error_device_count": lambda n : setattr(self, 'error_device_count', n.get_int_value()),
            "non_compliant_device_count": lambda n : setattr(self, 'non_compliant_device_count', n.get_int_value()),
            "not_applicable_device_count": lambda n : setattr(self, 'not_applicable_device_count', n.get_int_value()),
            "not_assigned_device_count": lambda n : setattr(self, 'not_assigned_device_count', n.get_int_value()),
            "remediated_device_count": lambda n : setattr(self, 'remediated_device_count', n.get_int_value()),
            "unknown_device_count": lambda n : setattr(self, 'unknown_device_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def non_compliant_device_count(self,) -> Optional[int]:
        """
        Gets the nonCompliantDeviceCount property value. Number of NonCompliant devices
        Returns: Optional[int]
        """
        return self._non_compliant_device_count
    
    @non_compliant_device_count.setter
    def non_compliant_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the nonCompliantDeviceCount property value. Number of NonCompliant devices
        Args:
            value: Value to set for the nonCompliantDeviceCount property.
        """
        self._non_compliant_device_count = value
    
    @property
    def not_applicable_device_count(self,) -> Optional[int]:
        """
        Gets the notApplicableDeviceCount property value. Number of not applicable devices
        Returns: Optional[int]
        """
        return self._not_applicable_device_count
    
    @not_applicable_device_count.setter
    def not_applicable_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the notApplicableDeviceCount property value. Number of not applicable devices
        Args:
            value: Value to set for the notApplicableDeviceCount property.
        """
        self._not_applicable_device_count = value
    
    @property
    def not_assigned_device_count(self,) -> Optional[int]:
        """
        Gets the notAssignedDeviceCount property value. Number of not assigned devices
        Returns: Optional[int]
        """
        return self._not_assigned_device_count
    
    @not_assigned_device_count.setter
    def not_assigned_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the notAssignedDeviceCount property value. Number of not assigned devices
        Args:
            value: Value to set for the notAssignedDeviceCount property.
        """
        self._not_assigned_device_count = value
    
    @property
    def remediated_device_count(self,) -> Optional[int]:
        """
        Gets the remediatedDeviceCount property value. Number of remediated devices
        Returns: Optional[int]
        """
        return self._remediated_device_count
    
    @remediated_device_count.setter
    def remediated_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the remediatedDeviceCount property value. Number of remediated devices
        Args:
            value: Value to set for the remediatedDeviceCount property.
        """
        self._remediated_device_count = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("advancedThreatProtectionOnboardingDeviceSettingStates", self.advanced_threat_protection_onboarding_device_setting_states)
        writer.write_int_value("compliantDeviceCount", self.compliant_device_count)
        writer.write_int_value("conflictDeviceCount", self.conflict_device_count)
        writer.write_int_value("errorDeviceCount", self.error_device_count)
        writer.write_int_value("nonCompliantDeviceCount", self.non_compliant_device_count)
        writer.write_int_value("notApplicableDeviceCount", self.not_applicable_device_count)
        writer.write_int_value("notAssignedDeviceCount", self.not_assigned_device_count)
        writer.write_int_value("remediatedDeviceCount", self.remediated_device_count)
        writer.write_int_value("unknownDeviceCount", self.unknown_device_count)
    
    @property
    def unknown_device_count(self,) -> Optional[int]:
        """
        Gets the unknownDeviceCount property value. Number of unknown devices
        Returns: Optional[int]
        """
        return self._unknown_device_count
    
    @unknown_device_count.setter
    def unknown_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the unknownDeviceCount property value. Number of unknown devices
        Args:
            value: Value to set for the unknownDeviceCount property.
        """
        self._unknown_device_count = value
    

