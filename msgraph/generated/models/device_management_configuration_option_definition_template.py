from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_setting_instance_template = lazy_import('msgraph.generated.models.device_management_configuration_setting_instance_template')

class DeviceManagementConfigurationOptionDefinitionTemplate(AdditionalDataHolder, Parsable):
    """
    Option Definition Template
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
    
    @property
    def children(self,) -> Optional[List[device_management_configuration_setting_instance_template.DeviceManagementConfigurationSettingInstanceTemplate]]:
        """
        Gets the children property value. Option Children
        Returns: Optional[List[device_management_configuration_setting_instance_template.DeviceManagementConfigurationSettingInstanceTemplate]]
        """
        return self._children
    
    @children.setter
    def children(self,value: Optional[List[device_management_configuration_setting_instance_template.DeviceManagementConfigurationSettingInstanceTemplate]] = None) -> None:
        """
        Sets the children property value. Option Children
        Args:
            value: Value to set for the children property.
        """
        self._children = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementConfigurationOptionDefinitionTemplate and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Option Children
        self._children: Optional[List[device_management_configuration_setting_instance_template.DeviceManagementConfigurationSettingInstanceTemplate]] = None
        # Option ItemId
        self._item_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationOptionDefinitionTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationOptionDefinitionTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationOptionDefinitionTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "children": lambda n : setattr(self, 'children', n.get_collection_of_object_values(device_management_configuration_setting_instance_template.DeviceManagementConfigurationSettingInstanceTemplate)),
            "itemId": lambda n : setattr(self, 'item_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def item_id(self,) -> Optional[str]:
        """
        Gets the itemId property value. Option ItemId
        Returns: Optional[str]
        """
        return self._item_id
    
    @item_id.setter
    def item_id(self,value: Optional[str] = None) -> None:
        """
        Sets the itemId property value. Option ItemId
        Args:
            value: Value to set for the item_id property.
        """
        self._item_id = value
    
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
        writer.write_collection_of_object_values("children", self.children)
        writer.write_str_value("itemId", self.item_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

