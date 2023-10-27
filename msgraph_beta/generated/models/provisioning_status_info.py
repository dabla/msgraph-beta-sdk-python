from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .provisioning_error_info import ProvisioningErrorInfo
    from .provisioning_result import ProvisioningResult

@dataclass
class ProvisioningStatusInfo(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # If status isn't success/ skipped details for the error are contained in this.
    error_information: Optional[ProvisioningErrorInfo] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Possible values are: success, failure, skipped, warning, unknownFutureValue. Supports $filter (eq, contains).
    status: Optional[ProvisioningResult] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ProvisioningStatusInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProvisioningStatusInfo
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ProvisioningStatusInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .provisioning_error_info import ProvisioningErrorInfo
        from .provisioning_result import ProvisioningResult

        from .provisioning_error_info import ProvisioningErrorInfo
        from .provisioning_result import ProvisioningResult

        fields: Dict[str, Callable[[Any], None]] = {
            "errorInformation": lambda n : setattr(self, 'error_information', n.get_object_value(ProvisioningErrorInfo)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ProvisioningResult)),
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
        writer.write_object_value("errorInformation", self.error_information)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    
