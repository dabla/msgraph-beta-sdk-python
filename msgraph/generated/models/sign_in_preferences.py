from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class SignInPreferences(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new signInPreferences and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates whether the credential preferences of the system are enabled.
        self._is_system_preferred_authentication_method_enabled: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SignInPreferences:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SignInPreferences
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SignInPreferences()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "isSystemPreferredAuthenticationMethodEnabled": lambda n : setattr(self, 'is_system_preferred_authentication_method_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def is_system_preferred_authentication_method_enabled(self,) -> Optional[bool]:
        """
        Gets the isSystemPreferredAuthenticationMethodEnabled property value. Indicates whether the credential preferences of the system are enabled.
        Returns: Optional[bool]
        """
        return self._is_system_preferred_authentication_method_enabled
    
    @is_system_preferred_authentication_method_enabled.setter
    def is_system_preferred_authentication_method_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSystemPreferredAuthenticationMethodEnabled property value. Indicates whether the credential preferences of the system are enabled.
        Args:
            value: Value to set for the is_system_preferred_authentication_method_enabled property.
        """
        self._is_system_preferred_authentication_method_enabled = value
    
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
        writer.write_bool_value("isSystemPreferredAuthenticationMethodEnabled", self.is_system_preferred_authentication_method_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    
