from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .dlp_action_info import DlpActionInfo
    from .rule_mode import RuleMode

@dataclass
class MatchingDlpRule(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The actions property
    actions: Optional[List[DlpActionInfo]] = None
    # The isMostRestrictive property
    is_most_restrictive: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The policyId property
    policy_id: Optional[str] = None
    # The policyName property
    policy_name: Optional[str] = None
    # The priority property
    priority: Optional[int] = None
    # The ruleId property
    rule_id: Optional[str] = None
    # The ruleMode property
    rule_mode: Optional[RuleMode] = None
    # The ruleName property
    rule_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MatchingDlpRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MatchingDlpRule
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MatchingDlpRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .dlp_action_info import DlpActionInfo
        from .rule_mode import RuleMode

        from .dlp_action_info import DlpActionInfo
        from .rule_mode import RuleMode

        fields: Dict[str, Callable[[Any], None]] = {
            "actions": lambda n : setattr(self, 'actions', n.get_collection_of_object_values(DlpActionInfo)),
            "isMostRestrictive": lambda n : setattr(self, 'is_most_restrictive', n.get_bool_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "policyId": lambda n : setattr(self, 'policy_id', n.get_str_value()),
            "policyName": lambda n : setattr(self, 'policy_name', n.get_str_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "ruleId": lambda n : setattr(self, 'rule_id', n.get_str_value()),
            "ruleMode": lambda n : setattr(self, 'rule_mode', n.get_enum_value(RuleMode)),
            "ruleName": lambda n : setattr(self, 'rule_name', n.get_str_value()),
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
        writer.write_collection_of_object_values("actions", self.actions)
        writer.write_bool_value("isMostRestrictive", self.is_most_restrictive)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("policyId", self.policy_id)
        writer.write_str_value("policyName", self.policy_name)
        writer.write_int_value("priority", self.priority)
        writer.write_str_value("ruleId", self.rule_id)
        writer.write_enum_value("ruleMode", self.rule_mode)
        writer.write_str_value("ruleName", self.rule_name)
        writer.write_additional_data_value(self.additional_data)
    
