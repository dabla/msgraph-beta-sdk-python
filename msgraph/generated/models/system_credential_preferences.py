from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import advanced_config_state, exclude_target, include_target

class SystemCredentialPreferences(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new systemCredentialPreferences and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Users and groups excluded from the preferred authentication method experience of the system.
        self._exclude_targets: Optional[List[exclude_target.ExcludeTarget]] = None
        # Users and groups included in the preferred authentication method experience of the system.
        self._include_targets: Optional[List[include_target.IncludeTarget]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The state property
        self._state: Optional[advanced_config_state.AdvancedConfigState] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SystemCredentialPreferences:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SystemCredentialPreferences
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SystemCredentialPreferences()
    
    @property
    def exclude_targets(self,) -> Optional[List[exclude_target.ExcludeTarget]]:
        """
        Gets the excludeTargets property value. Users and groups excluded from the preferred authentication method experience of the system.
        Returns: Optional[List[exclude_target.ExcludeTarget]]
        """
        return self._exclude_targets
    
    @exclude_targets.setter
    def exclude_targets(self,value: Optional[List[exclude_target.ExcludeTarget]] = None) -> None:
        """
        Sets the excludeTargets property value. Users and groups excluded from the preferred authentication method experience of the system.
        Args:
            value: Value to set for the exclude_targets property.
        """
        self._exclude_targets = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import advanced_config_state, exclude_target, include_target

        fields: Dict[str, Callable[[Any], None]] = {
            "excludeTargets": lambda n : setattr(self, 'exclude_targets', n.get_collection_of_object_values(exclude_target.ExcludeTarget)),
            "includeTargets": lambda n : setattr(self, 'include_targets', n.get_collection_of_object_values(include_target.IncludeTarget)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(advanced_config_state.AdvancedConfigState)),
        }
        return fields
    
    @property
    def include_targets(self,) -> Optional[List[include_target.IncludeTarget]]:
        """
        Gets the includeTargets property value. Users and groups included in the preferred authentication method experience of the system.
        Returns: Optional[List[include_target.IncludeTarget]]
        """
        return self._include_targets
    
    @include_targets.setter
    def include_targets(self,value: Optional[List[include_target.IncludeTarget]] = None) -> None:
        """
        Sets the includeTargets property value. Users and groups included in the preferred authentication method experience of the system.
        Args:
            value: Value to set for the include_targets property.
        """
        self._include_targets = value
    
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("excludeTargets", self.exclude_targets)
        writer.write_collection_of_object_values("includeTargets", self.include_targets)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def state(self,) -> Optional[advanced_config_state.AdvancedConfigState]:
        """
        Gets the state property value. The state property
        Returns: Optional[advanced_config_state.AdvancedConfigState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[advanced_config_state.AdvancedConfigState] = None) -> None:
        """
        Sets the state property value. The state property
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    
