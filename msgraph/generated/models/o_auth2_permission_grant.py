from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class OAuth2PermissionGrant(Entity):
    # The object id (not appId) of the client service principal for the application that is authorized to act on behalf of a signed-in user when accessing an API. Required. Supports $filter (eq only).
    client_id: Optional[str] = None
    # Indicates whether authorization is granted for the client application to impersonate all users or only a specific user. AllPrincipals indicates authorization to impersonate all users. Principal indicates authorization to impersonate a specific user. Consent on behalf of all users can be granted by an administrator. Nonadmin users may be authorized to consent on behalf of themselves in some cases, for some delegated permissions. Required. Supports $filter (eq only).
    consent_type: Optional[str] = None
    # Currently, the end time value is ignored, but a value is required when creating an oAuth2PermissionGrant. Required.
    expiry_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The id of the user on behalf of whom the client is authorized to access the resource, when consentType is Principal. If consentType is AllPrincipals this value is null. Required when consentType is Principal. Supports $filter (eq only).
    principal_id: Optional[str] = None
    # The id of the resource service principal to which access is authorized. This identifies the API that the client is authorized to attempt to call on behalf of a signed-in user. Supports $filter (eq only).
    resource_id: Optional[str] = None
    # A space-separated list of the claim values for delegated permissions that should be included in access tokens for the resource application (the API). For example, openid User.Read GroupMember.Read.All. Each claim value should match the value field of one of the delegated permissions defined by the API, listed in the publishedPermissionScopes property of the resource service principal. Must not exceed 3850 characters in length.
    scope: Optional[str] = None
    # Currently, the start time value is ignored, but a value is required when creating an oAuth2PermissionGrant. Required.
    start_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OAuth2PermissionGrant:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OAuth2PermissionGrant
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return OAuth2PermissionGrant()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "clientId": lambda n : setattr(self, 'client_id', n.get_str_value()),
            "consentType": lambda n : setattr(self, 'consent_type', n.get_str_value()),
            "expiryTime": lambda n : setattr(self, 'expiry_time', n.get_datetime_value()),
            "principalId": lambda n : setattr(self, 'principal_id', n.get_str_value()),
            "resourceId": lambda n : setattr(self, 'resource_id', n.get_str_value()),
            "scope": lambda n : setattr(self, 'scope', n.get_str_value()),
            "startTime": lambda n : setattr(self, 'start_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("clientId", self.client_id)
        writer.write_str_value("consentType", self.consent_type)
        writer.write_datetime_value("expiryTime", self.expiry_time)
        writer.write_str_value("principalId", self.principal_id)
        writer.write_str_value("resourceId", self.resource_id)
        writer.write_str_value("scope", self.scope)
        writer.write_datetime_value("startTime", self.start_time)
    

