from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_and_app_management_assignment_filter_type = lazy_import('msgraph.generated.models.device_and_app_management_assignment_filter_type')

class DeviceAndAppManagementAssignmentTarget(AdditionalDataHolder, Parsable):
    """
    Base type for assignment targets.
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
        Instantiates a new deviceAndAppManagementAssignmentTarget and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The Id of the filter for the target assignment.
        self._device_and_app_management_assignment_filter_id: Optional[str] = None
        # Represents type of the assignment filter.
        self._device_and_app_management_assignment_filter_type: Optional[device_and_app_management_assignment_filter_type.DeviceAndAppManagementAssignmentFilterType] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceAndAppManagementAssignmentTarget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceAndAppManagementAssignmentTarget
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceAndAppManagementAssignmentTarget()
    
    @property
    def device_and_app_management_assignment_filter_id(self,) -> Optional[str]:
        """
        Gets the deviceAndAppManagementAssignmentFilterId property value. The Id of the filter for the target assignment.
        Returns: Optional[str]
        """
        return self._device_and_app_management_assignment_filter_id
    
    @device_and_app_management_assignment_filter_id.setter
    def device_and_app_management_assignment_filter_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceAndAppManagementAssignmentFilterId property value. The Id of the filter for the target assignment.
        Args:
            value: Value to set for the device_and_app_management_assignment_filter_id property.
        """
        self._device_and_app_management_assignment_filter_id = value
    
    @property
    def device_and_app_management_assignment_filter_type(self,) -> Optional[device_and_app_management_assignment_filter_type.DeviceAndAppManagementAssignmentFilterType]:
        """
        Gets the deviceAndAppManagementAssignmentFilterType property value. Represents type of the assignment filter.
        Returns: Optional[device_and_app_management_assignment_filter_type.DeviceAndAppManagementAssignmentFilterType]
        """
        return self._device_and_app_management_assignment_filter_type
    
    @device_and_app_management_assignment_filter_type.setter
    def device_and_app_management_assignment_filter_type(self,value: Optional[device_and_app_management_assignment_filter_type.DeviceAndAppManagementAssignmentFilterType] = None) -> None:
        """
        Sets the deviceAndAppManagementAssignmentFilterType property value. Represents type of the assignment filter.
        Args:
            value: Value to set for the device_and_app_management_assignment_filter_type property.
        """
        self._device_and_app_management_assignment_filter_type = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "deviceAndAppManagementAssignmentFilterId": lambda n : setattr(self, 'device_and_app_management_assignment_filter_id', n.get_str_value()),
            "deviceAndAppManagementAssignmentFilterType": lambda n : setattr(self, 'device_and_app_management_assignment_filter_type', n.get_enum_value(device_and_app_management_assignment_filter_type.DeviceAndAppManagementAssignmentFilterType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
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
        writer.write_str_value("deviceAndAppManagementAssignmentFilterId", self.device_and_app_management_assignment_filter_id)
        writer.write_enum_value("deviceAndAppManagementAssignmentFilterType", self.device_and_app_management_assignment_filter_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

