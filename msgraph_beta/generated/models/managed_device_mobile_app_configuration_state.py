from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .compliance_status import ComplianceStatus
    from .entity import Entity
    from .managed_device_mobile_app_configuration_setting_state import ManagedDeviceMobileAppConfigurationSettingState
    from .policy_platform_type import PolicyPlatformType

from .entity import Entity

@dataclass
class ManagedDeviceMobileAppConfigurationState(Entity):
    """
    Managed Device Mobile App Configuration State for a given device.
    """
    # The name of the policy for this policyBase
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Supported platform types for policies.
    platform_type: Optional[PolicyPlatformType] = None
    # Count of how many setting a policy holds
    setting_count: Optional[int] = None
    # The settingStates property
    setting_states: Optional[List[ManagedDeviceMobileAppConfigurationSettingState]] = None
    # The state property
    state: Optional[ComplianceStatus] = None
    # User unique identifier, must be Guid
    user_id: Optional[str] = None
    # User Principal Name
    user_principal_name: Optional[str] = None
    # The version of the policy
    version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedDeviceMobileAppConfigurationState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedDeviceMobileAppConfigurationState
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ManagedDeviceMobileAppConfigurationState()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .compliance_status import ComplianceStatus
        from .entity import Entity
        from .managed_device_mobile_app_configuration_setting_state import ManagedDeviceMobileAppConfigurationSettingState
        from .policy_platform_type import PolicyPlatformType

        from .compliance_status import ComplianceStatus
        from .entity import Entity
        from .managed_device_mobile_app_configuration_setting_state import ManagedDeviceMobileAppConfigurationSettingState
        from .policy_platform_type import PolicyPlatformType

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "platformType": lambda n : setattr(self, 'platform_type', n.get_enum_value(PolicyPlatformType)),
            "settingCount": lambda n : setattr(self, 'setting_count', n.get_int_value()),
            "settingStates": lambda n : setattr(self, 'setting_states', n.get_collection_of_object_values(ManagedDeviceMobileAppConfigurationSettingState)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(ComplianceStatus)),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("platformType", self.platform_type)
        writer.write_int_value("settingCount", self.setting_count)
        writer.write_collection_of_object_values("settingStates", self.setting_states)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_int_value("version", self.version)
    
