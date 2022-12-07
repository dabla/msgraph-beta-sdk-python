from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

comms_operation = lazy_import('msgraph.generated.models.comms_operation')
play_prompt_completion_reason = lazy_import('msgraph.generated.models.play_prompt_completion_reason')

class PlayPromptOperation(comms_operation.CommsOperation):
    @property
    def completion_reason(self,) -> Optional[play_prompt_completion_reason.PlayPromptCompletionReason]:
        """
        Gets the completionReason property value. Possible values are: unknown, completedSuccessfully, mediaOperationCanceled.
        Returns: Optional[play_prompt_completion_reason.PlayPromptCompletionReason]
        """
        return self._completion_reason
    
    @completion_reason.setter
    def completion_reason(self,value: Optional[play_prompt_completion_reason.PlayPromptCompletionReason] = None) -> None:
        """
        Sets the completionReason property value. Possible values are: unknown, completedSuccessfully, mediaOperationCanceled.
        Args:
            value: Value to set for the completionReason property.
        """
        self._completion_reason = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new PlayPromptOperation and sets the default values.
        """
        super().__init__()
        # Possible values are: unknown, completedSuccessfully, mediaOperationCanceled.
        self._completion_reason: Optional[play_prompt_completion_reason.PlayPromptCompletionReason] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlayPromptOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlayPromptOperation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PlayPromptOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "completion_reason": lambda n : setattr(self, 'completion_reason', n.get_enum_value(play_prompt_completion_reason.PlayPromptCompletionReason)),
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
        writer.write_enum_value("completionReason", self.completion_reason)
    

