from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class PreAuthorizedApplication(AdditionalDataHolder, Parsable):
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
    def app_id(self,) -> Optional[str]:
        """
        Gets the appId property value. The unique identifier for the client application.
        Returns: Optional[str]
        """
        return self._app_id
    
    @app_id.setter
    def app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appId property value. The unique identifier for the client application.
        Args:
            value: Value to set for the app_id property.
        """
        self._app_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new preAuthorizedApplication and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The unique identifier for the client application.
        self._app_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The unique identifier for the scopes the client application is granted.
        self._permission_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PreAuthorizedApplication:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PreAuthorizedApplication
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PreAuthorizedApplication()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "permissionIds": lambda n : setattr(self, 'permission_ids', n.get_collection_of_primitive_values(str)),
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
    
    @property
    def permission_ids(self,) -> Optional[List[str]]:
        """
        Gets the permissionIds property value. The unique identifier for the scopes the client application is granted.
        Returns: Optional[List[str]]
        """
        return self._permission_ids
    
    @permission_ids.setter
    def permission_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the permissionIds property value. The unique identifier for the scopes the client application is granted.
        Args:
            value: Value to set for the permission_ids property.
        """
        self._permission_ids = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("permissionIds", self.permission_ids)
        writer.write_additional_data_value(self.additional_data)
    

