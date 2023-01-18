from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

attack_simulation_operation_type = lazy_import('msgraph.generated.models.attack_simulation_operation_type')
long_running_operation = lazy_import('msgraph.generated.models.long_running_operation')

class AttackSimulationOperation(long_running_operation.LongRunningOperation):
    def __init__(self,) -> None:
        """
        Instantiates a new AttackSimulationOperation and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The percentageCompleted property
        self._percentage_completed: Optional[int] = None
        # The tenantId property
        self._tenant_id: Optional[str] = None
        # The type property
        self._type: Optional[attack_simulation_operation_type.AttackSimulationOperationType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AttackSimulationOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AttackSimulationOperation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AttackSimulationOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "percentage_completed": lambda n : setattr(self, 'percentage_completed', n.get_int_value()),
            "tenant_id": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(attack_simulation_operation_type.AttackSimulationOperationType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def percentage_completed(self,) -> Optional[int]:
        """
        Gets the percentageCompleted property value. The percentageCompleted property
        Returns: Optional[int]
        """
        return self._percentage_completed
    
    @percentage_completed.setter
    def percentage_completed(self,value: Optional[int] = None) -> None:
        """
        Sets the percentageCompleted property value. The percentageCompleted property
        Args:
            value: Value to set for the percentageCompleted property.
        """
        self._percentage_completed = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("percentageCompleted", self.percentage_completed)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_enum_value("type", self.type)
    
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
            value: Value to set for the tenantId property.
        """
        self._tenant_id = value
    
    @property
    def type(self,) -> Optional[attack_simulation_operation_type.AttackSimulationOperationType]:
        """
        Gets the type property value. The type property
        Returns: Optional[attack_simulation_operation_type.AttackSimulationOperationType]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[attack_simulation_operation_type.AttackSimulationOperationType] = None) -> None:
        """
        Sets the type property value. The type property
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

