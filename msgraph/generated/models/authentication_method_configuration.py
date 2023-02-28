from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

authentication_method_state = lazy_import('msgraph.generated.models.authentication_method_state')
entity = lazy_import('msgraph.generated.models.entity')
exclude_target = lazy_import('msgraph.generated.models.exclude_target')

class AuthenticationMethodConfiguration(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new authenticationMethodConfiguration and sets the default values.
        """
        super().__init__()
        # Groups of users that are excluded from a policy.
        self._exclude_targets: Optional[List[exclude_target.ExcludeTarget]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The state of the policy. Possible values are: enabled, disabled.
        self._state: Optional[authentication_method_state.AuthenticationMethodState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationMethodConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationMethodConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuthenticationMethodConfiguration()
    
    @property
    def exclude_targets(self,) -> Optional[List[exclude_target.ExcludeTarget]]:
        """
        Gets the excludeTargets property value. Groups of users that are excluded from a policy.
        Returns: Optional[List[exclude_target.ExcludeTarget]]
        """
        return self._exclude_targets
    
    @exclude_targets.setter
    def exclude_targets(self,value: Optional[List[exclude_target.ExcludeTarget]] = None) -> None:
        """
        Sets the excludeTargets property value. Groups of users that are excluded from a policy.
        Args:
            value: Value to set for the exclude_targets property.
        """
        self._exclude_targets = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "excludeTargets": lambda n : setattr(self, 'exclude_targets', n.get_collection_of_object_values(exclude_target.ExcludeTarget)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(authentication_method_state.AuthenticationMethodState)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("excludeTargets", self.exclude_targets)
        writer.write_enum_value("state", self.state)
    
    @property
    def state(self,) -> Optional[authentication_method_state.AuthenticationMethodState]:
        """
        Gets the state property value. The state of the policy. Possible values are: enabled, disabled.
        Returns: Optional[authentication_method_state.AuthenticationMethodState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[authentication_method_state.AuthenticationMethodState] = None) -> None:
        """
        Sets the state property value. The state of the policy. Possible values are: enabled, disabled.
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    

