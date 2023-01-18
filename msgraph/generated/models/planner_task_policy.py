from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

planner_task_role_based_rule = lazy_import('msgraph.generated.models.planner_task_role_based_rule')

class PlannerTaskPolicy(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new plannerTaskPolicy and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The rules that should be enforced on the tasks when they are being changed outside of the scenario, based on the role of the caller.
        self._rules: Optional[List[planner_task_role_based_rule.PlannerTaskRoleBasedRule]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerTaskPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerTaskPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PlannerTaskPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "rules": lambda n : setattr(self, 'rules', n.get_collection_of_object_values(planner_task_role_based_rule.PlannerTaskRoleBasedRule)),
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
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def rules(self,) -> Optional[List[planner_task_role_based_rule.PlannerTaskRoleBasedRule]]:
        """
        Gets the rules property value. The rules that should be enforced on the tasks when they are being changed outside of the scenario, based on the role of the caller.
        Returns: Optional[List[planner_task_role_based_rule.PlannerTaskRoleBasedRule]]
        """
        return self._rules
    
    @rules.setter
    def rules(self,value: Optional[List[planner_task_role_based_rule.PlannerTaskRoleBasedRule]] = None) -> None:
        """
        Sets the rules property value. The rules that should be enforced on the tasks when they are being changed outside of the scenario, based on the role of the caller.
        Args:
            value: Value to set for the rules property.
        """
        self._rules = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("rules", self.rules)
        writer.write_additional_data_value(self.additional_data)
    

