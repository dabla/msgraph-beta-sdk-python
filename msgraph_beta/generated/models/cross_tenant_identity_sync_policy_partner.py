from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cross_tenant_user_sync_inbound import CrossTenantUserSyncInbound

@dataclass
class CrossTenantIdentitySyncPolicyPartner(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Display name for the cross-tenant user synchronization policy. Use the name of the partner Microsoft Entra tenant to easily identify the policy. Optional.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Tenant identifier for the partner Microsoft Entra organization. Read-only.
    tenant_id: Optional[str] = None
    # Defines whether users can be synchronized from the partner tenant. Key.
    user_sync_inbound: Optional[CrossTenantUserSyncInbound] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CrossTenantIdentitySyncPolicyPartner:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CrossTenantIdentitySyncPolicyPartner
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CrossTenantIdentitySyncPolicyPartner()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cross_tenant_user_sync_inbound import CrossTenantUserSyncInbound

        from .cross_tenant_user_sync_inbound import CrossTenantUserSyncInbound

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "userSyncInbound": lambda n : setattr(self, 'user_sync_inbound', n.get_object_value(CrossTenantUserSyncInbound)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_object_value("userSyncInbound", self.user_sync_inbound)
        writer.write_additional_data_value(self.additional_data)
    
