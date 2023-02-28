from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_action_result = lazy_import('msgraph.generated.models.device_action_result')

class ResetPasscodeActionResult(device_action_result.DeviceActionResult):
    def __init__(self,) -> None:
        """
        Instantiates a new ResetPasscodeActionResult and sets the default values.
        """
        super().__init__()
        # RotateBitLockerKeys action error code. Valid values 0 to 2147483647
        self._error_code: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Newly generated passcode for the device
        self._passcode: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ResetPasscodeActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ResetPasscodeActionResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ResetPasscodeActionResult()
    
    @property
    def error_code(self,) -> Optional[int]:
        """
        Gets the errorCode property value. RotateBitLockerKeys action error code. Valid values 0 to 2147483647
        Returns: Optional[int]
        """
        return self._error_code
    
    @error_code.setter
    def error_code(self,value: Optional[int] = None) -> None:
        """
        Sets the errorCode property value. RotateBitLockerKeys action error code. Valid values 0 to 2147483647
        Args:
            value: Value to set for the error_code property.
        """
        self._error_code = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "errorCode": lambda n : setattr(self, 'error_code', n.get_int_value()),
            "passcode": lambda n : setattr(self, 'passcode', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def passcode(self,) -> Optional[str]:
        """
        Gets the passcode property value. Newly generated passcode for the device
        Returns: Optional[str]
        """
        return self._passcode
    
    @passcode.setter
    def passcode(self,value: Optional[str] = None) -> None:
        """
        Sets the passcode property value. Newly generated passcode for the device
        Args:
            value: Value to set for the passcode property.
        """
        self._passcode = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("errorCode", self.error_code)
        writer.write_str_value("passcode", self.passcode)
    

