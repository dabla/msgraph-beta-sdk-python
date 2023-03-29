from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class Configuration(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new configuration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The authorizedAppIds property
        self._authorized_app_ids: Optional[List[str]] = None
        # The authorizedApps property
        self._authorized_apps: Optional[List[str]] = None
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
    
    @property
    def authorized_app_ids(self,) -> Optional[List[str]]:
        """
        Gets the authorizedAppIds property value. The authorizedAppIds property
        Returns: Optional[List[str]]
        """
        return self._authorized_app_ids
    
    @authorized_app_ids.setter
    def authorized_app_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the authorizedAppIds property value. The authorizedAppIds property
        Args:
            value: Value to set for the authorized_app_ids property.
        """
        self._authorized_app_ids = value
    
    @property
    def authorized_apps(self,) -> Optional[List[str]]:
        """
        Gets the authorizedApps property value. The authorizedApps property
        Returns: Optional[List[str]]
        """
        return self._authorized_apps
    
    @authorized_apps.setter
    def authorized_apps(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the authorizedApps property value. The authorizedApps property
        Args:
            value: Value to set for the authorized_apps property.
        """
        self._authorized_apps = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Configuration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Configuration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Configuration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "authorizedApps": lambda n : setattr(self, 'authorized_apps', n.get_collection_of_primitive_values(str)),
            "authorizedAppIds": lambda n : setattr(self, 'authorized_app_ids', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("authorizedApps", self.authorized_apps)
        writer.write_collection_of_primitive_values("authorizedAppIds", self.authorized_app_ids)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

