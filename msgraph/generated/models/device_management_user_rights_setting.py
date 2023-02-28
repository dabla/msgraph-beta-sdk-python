from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_user_rights_local_user_or_group = lazy_import('msgraph.generated.models.device_management_user_rights_local_user_or_group')
state_management_setting = lazy_import('msgraph.generated.models.state_management_setting')

class DeviceManagementUserRightsSetting(AdditionalDataHolder, Parsable):
    """
    Represents a user rights setting.
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementUserRightsSetting and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Representing a collection of local users or groups which will be set on device if the state of this setting is Allowed. This collection can contain a maximum of 500 elements.
        self._local_users_or_groups: Optional[List[device_management_user_rights_local_user_or_group.DeviceManagementUserRightsLocalUserOrGroup]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # State Management Setting.
        self._state: Optional[state_management_setting.StateManagementSetting] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementUserRightsSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementUserRightsSetting
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementUserRightsSetting()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "localUsersOrGroups": lambda n : setattr(self, 'local_users_or_groups', n.get_collection_of_object_values(device_management_user_rights_local_user_or_group.DeviceManagementUserRightsLocalUserOrGroup)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(state_management_setting.StateManagementSetting)),
        }
        return fields
    
    @property
    def local_users_or_groups(self,) -> Optional[List[device_management_user_rights_local_user_or_group.DeviceManagementUserRightsLocalUserOrGroup]]:
        """
        Gets the localUsersOrGroups property value. Representing a collection of local users or groups which will be set on device if the state of this setting is Allowed. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[device_management_user_rights_local_user_or_group.DeviceManagementUserRightsLocalUserOrGroup]]
        """
        return self._local_users_or_groups
    
    @local_users_or_groups.setter
    def local_users_or_groups(self,value: Optional[List[device_management_user_rights_local_user_or_group.DeviceManagementUserRightsLocalUserOrGroup]] = None) -> None:
        """
        Sets the localUsersOrGroups property value. Representing a collection of local users or groups which will be set on device if the state of this setting is Allowed. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the local_users_or_groups property.
        """
        self._local_users_or_groups = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("localUsersOrGroups", self.local_users_or_groups)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def state(self,) -> Optional[state_management_setting.StateManagementSetting]:
        """
        Gets the state property value. State Management Setting.
        Returns: Optional[state_management_setting.StateManagementSetting]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[state_management_setting.StateManagementSetting] = None) -> None:
        """
        Sets the state property value. State Management Setting.
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    

