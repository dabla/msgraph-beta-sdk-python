from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import action_capability, cloud_pc_remote_action_name

class CloudPcRemoteActionCapability(AdditionalDataHolder, Parsable):
    @property
    def action_capability(self,) -> Optional[action_capability.ActionCapability]:
        """
        Gets the actionCapability property value. The actionCapability property
        Returns: Optional[action_capability.ActionCapability]
        """
        return self._action_capability
    
    @action_capability.setter
    def action_capability(self,value: Optional[action_capability.ActionCapability] = None) -> None:
        """
        Sets the actionCapability property value. The actionCapability property
        Args:
            value: Value to set for the actionCapability property.
        """
        self._action_capability = value
    
    @property
    def action_name(self,) -> Optional[cloud_pc_remote_action_name.CloudPcRemoteActionName]:
        """
        Gets the actionName property value. The actionName property
        Returns: Optional[cloud_pc_remote_action_name.CloudPcRemoteActionName]
        """
        return self._action_name
    
    @action_name.setter
    def action_name(self,value: Optional[cloud_pc_remote_action_name.CloudPcRemoteActionName] = None) -> None:
        """
        Sets the actionName property value. The actionName property
        Args:
            value: Value to set for the actionName property.
        """
        self._action_name = value
    
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
        Instantiates a new cloudPcRemoteActionCapability and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The actionCapability property
        self._action_capability: Optional[action_capability.ActionCapability] = None
        # The actionName property
        self._action_name: Optional[cloud_pc_remote_action_name.CloudPcRemoteActionName] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcRemoteActionCapability:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcRemoteActionCapability
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcRemoteActionCapability()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "action_capability": lambda n : setattr(self, 'action_capability', n.get_enum_value(action_capability.ActionCapability)),
            "action_name": lambda n : setattr(self, 'action_name', n.get_enum_value(cloud_pc_remote_action_name.CloudPcRemoteActionName)),
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
            value: Value to set for the OdataType property.
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
        writer.write_enum_value("actionCapability", self.action_capability)
        writer.write_enum_value("actionName", self.action_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    
