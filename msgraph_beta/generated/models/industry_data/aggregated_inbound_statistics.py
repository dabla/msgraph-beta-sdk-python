from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .industry_data_run_role_count_metric import IndustryDataRunRoleCountMetric

@dataclass
class AggregatedInboundStatistics(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The aggregate count of errors encountered by activities during this run.
    errors: Optional[int] = None
    # The aggregate count of active inbound groups processed during the run.
    groups: Optional[int] = None
    # The aggregate count of active people matched to a Microsoft Entra user, by role.
    matched_people_by_role: Optional[List[IndustryDataRunRoleCountMetric]] = None
    # The aggregate count of active inbound memberships processed during the run.
    memberships: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The aggregate count of active inbound organizations processed during the run.
    organizations: Optional[int] = None
    # The aggregate count of active inbound people processed during the run.
    people: Optional[int] = None
    # The aggregate count of active people not matched to a Microsoft Entra user, by role.
    unmatched_people_by_role: Optional[List[IndustryDataRunRoleCountMetric]] = None
    # The aggregate count of warnings generated by activities during this run.
    warnings: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AggregatedInboundStatistics:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AggregatedInboundStatistics
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AggregatedInboundStatistics()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .industry_data_run_role_count_metric import IndustryDataRunRoleCountMetric

        from .industry_data_run_role_count_metric import IndustryDataRunRoleCountMetric

        fields: Dict[str, Callable[[Any], None]] = {
            "errors": lambda n : setattr(self, 'errors', n.get_int_value()),
            "groups": lambda n : setattr(self, 'groups', n.get_int_value()),
            "matchedPeopleByRole": lambda n : setattr(self, 'matched_people_by_role', n.get_collection_of_object_values(IndustryDataRunRoleCountMetric)),
            "memberships": lambda n : setattr(self, 'memberships', n.get_int_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "organizations": lambda n : setattr(self, 'organizations', n.get_int_value()),
            "people": lambda n : setattr(self, 'people', n.get_int_value()),
            "unmatchedPeopleByRole": lambda n : setattr(self, 'unmatched_people_by_role', n.get_collection_of_object_values(IndustryDataRunRoleCountMetric)),
            "warnings": lambda n : setattr(self, 'warnings', n.get_int_value()),
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
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    
