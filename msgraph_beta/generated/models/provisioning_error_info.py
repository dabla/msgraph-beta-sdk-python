from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .provisioning_status_error_category import ProvisioningStatusErrorCategory

@dataclass
class ProvisioningErrorInfo(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Additional details if there is error.
    additional_details: Optional[str] = None
    # Categorizes the error code. Possible values are failure, nonServiceFailure, success, unknownFutureValue
    error_category: Optional[ProvisioningStatusErrorCategory] = None
    # Unique error code if any occurred. Learn more
    error_code: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Summarizes the status and describes why the status happened.
    reason: Optional[str] = None
    # Provides the resolution for the corresponding error.
    recommended_action: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ProvisioningErrorInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProvisioningErrorInfo
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ProvisioningErrorInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .provisioning_status_error_category import ProvisioningStatusErrorCategory

        from .provisioning_status_error_category import ProvisioningStatusErrorCategory

        fields: Dict[str, Callable[[Any], None]] = {
            "additionalDetails": lambda n : setattr(self, 'additional_details', n.get_str_value()),
            "errorCategory": lambda n : setattr(self, 'error_category', n.get_enum_value(ProvisioningStatusErrorCategory)),
            "errorCode": lambda n : setattr(self, 'error_code', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "recommendedAction": lambda n : setattr(self, 'recommended_action', n.get_str_value()),
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
        writer.write_str_value("additionalDetails", self.additional_details)
        writer.write_enum_value("errorCategory", self.error_category)
        writer.write_str_value("errorCode", self.error_code)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("reason", self.reason)
        writer.write_str_value("recommendedAction", self.recommended_action)
        writer.write_additional_data_value(self.additional_data)
    

