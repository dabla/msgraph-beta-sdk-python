from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import safeguard_profile

class SafeguardSettings(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new safeguardSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # List of safeguards to ignore per device.
        self._disabled_safeguard_profiles: Optional[List[safeguard_profile.SafeguardProfile]] = None
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SafeguardSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SafeguardSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SafeguardSettings()
    
    @property
    def disabled_safeguard_profiles(self,) -> Optional[List[safeguard_profile.SafeguardProfile]]:
        """
        Gets the disabledSafeguardProfiles property value. List of safeguards to ignore per device.
        Returns: Optional[List[safeguard_profile.SafeguardProfile]]
        """
        return self._disabled_safeguard_profiles
    
    @disabled_safeguard_profiles.setter
    def disabled_safeguard_profiles(self,value: Optional[List[safeguard_profile.SafeguardProfile]] = None) -> None:
        """
        Sets the disabledSafeguardProfiles property value. List of safeguards to ignore per device.
        Args:
            value: Value to set for the disabled_safeguard_profiles property.
        """
        self._disabled_safeguard_profiles = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import safeguard_profile

        fields: Dict[str, Callable[[Any], None]] = {
            "disabledSafeguardProfiles": lambda n : setattr(self, 'disabled_safeguard_profiles', n.get_collection_of_object_values(safeguard_profile.SafeguardProfile)),
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
        writer.write_collection_of_object_values("disabledSafeguardProfiles", self.disabled_safeguard_profiles)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

