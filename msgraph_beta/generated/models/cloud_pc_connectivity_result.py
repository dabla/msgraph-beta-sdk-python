from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_connectivity_status import CloudPcConnectivityStatus
    from .cloud_pc_health_check_item import CloudPcHealthCheckItem

@dataclass
class CloudPcConnectivityResult(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # A list of failed health check items. If the status property is available, this property will be empty.
    failed_health_check_items: Optional[List[CloudPcHealthCheckItem]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[CloudPcConnectivityStatus] = None
    # Datetime when the status was updated. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 appears as 2014-01-01T00:00:00Z.
    updated_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcConnectivityResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcConnectivityResult
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CloudPcConnectivityResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_connectivity_status import CloudPcConnectivityStatus
        from .cloud_pc_health_check_item import CloudPcHealthCheckItem

        from .cloud_pc_connectivity_status import CloudPcConnectivityStatus
        from .cloud_pc_health_check_item import CloudPcHealthCheckItem

        fields: Dict[str, Callable[[Any], None]] = {
            "failedHealthCheckItems": lambda n : setattr(self, 'failed_health_check_items', n.get_collection_of_object_values(CloudPcHealthCheckItem)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(CloudPcConnectivityStatus)),
            "updatedDateTime": lambda n : setattr(self, 'updated_date_time', n.get_datetime_value()),
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
        writer.write_collection_of_object_values("failedHealthCheckItems", self.failed_health_check_items)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_datetime_value("updatedDateTime", self.updated_date_time)
        writer.write_additional_data_value(self.additional_data)
    
