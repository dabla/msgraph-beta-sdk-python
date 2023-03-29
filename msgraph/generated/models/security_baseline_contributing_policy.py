from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import security_baseline_policy_source_type

class SecurityBaselineContributingPolicy(AdditionalDataHolder, Parsable):
    """
    The security baseline compliance state of a setting for a device
    """
    def __init__(self,) -> None:
        """
        Instantiates a new securityBaselineContributingPolicy and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Name of the policy
        self._display_name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Unique identifier of the policy
        self._source_id: Optional[str] = None
        # Authoring source of a policy
        self._source_type: Optional[security_baseline_policy_source_type.SecurityBaselinePolicySourceType] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SecurityBaselineContributingPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SecurityBaselineContributingPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SecurityBaselineContributingPolicy()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Name of the policy
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Name of the policy
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import security_baseline_policy_source_type

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sourceId": lambda n : setattr(self, 'source_id', n.get_str_value()),
            "sourceType": lambda n : setattr(self, 'source_type', n.get_enum_value(security_baseline_policy_source_type.SecurityBaselinePolicySourceType)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sourceId", self.source_id)
        writer.write_enum_value("sourceType", self.source_type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def source_id(self,) -> Optional[str]:
        """
        Gets the sourceId property value. Unique identifier of the policy
        Returns: Optional[str]
        """
        return self._source_id
    
    @source_id.setter
    def source_id(self,value: Optional[str] = None) -> None:
        """
        Sets the sourceId property value. Unique identifier of the policy
        Args:
            value: Value to set for the source_id property.
        """
        self._source_id = value
    
    @property
    def source_type(self,) -> Optional[security_baseline_policy_source_type.SecurityBaselinePolicySourceType]:
        """
        Gets the sourceType property value. Authoring source of a policy
        Returns: Optional[security_baseline_policy_source_type.SecurityBaselinePolicySourceType]
        """
        return self._source_type
    
    @source_type.setter
    def source_type(self,value: Optional[security_baseline_policy_source_type.SecurityBaselinePolicySourceType] = None) -> None:
        """
        Sets the sourceType property value. Authoring source of a policy
        Args:
            value: Value to set for the source_type property.
        """
        self._source_type = value
    

