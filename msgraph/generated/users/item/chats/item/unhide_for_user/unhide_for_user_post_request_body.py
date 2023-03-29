from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models import teamwork_user_identity

class UnhideForUserPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new unhideForUserPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The tenantId property
        self._tenant_id: Optional[str] = None
        # The user property
        self._user: Optional[teamwork_user_identity.TeamworkUserIdentity] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnhideForUserPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnhideForUserPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnhideForUserPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ......models import teamwork_user_identity

        fields: Dict[str, Callable[[Any], None]] = {
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "user": lambda n : setattr(self, 'user', n.get_object_value(teamwork_user_identity.TeamworkUserIdentity)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_object_value("user", self.user)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The tenantId property
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The tenantId property
        Args:
            value: Value to set for the tenant_id property.
        """
        self._tenant_id = value
    
    @property
    def user(self,) -> Optional[teamwork_user_identity.TeamworkUserIdentity]:
        """
        Gets the user property value. The user property
        Returns: Optional[teamwork_user_identity.TeamworkUserIdentity]
        """
        return self._user
    
    @user.setter
    def user(self,value: Optional[teamwork_user_identity.TeamworkUserIdentity] = None) -> None:
        """
        Sets the user property value. The user property
        Args:
            value: Value to set for the user property.
        """
        self._user = value
    

