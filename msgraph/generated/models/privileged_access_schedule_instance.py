from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class PrivilegedAccessScheduleInstance(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new privilegedAccessScheduleInstance and sets the default values.
        """
        super().__init__()
        # The endDateTime property
        self._end_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The startDateTime property
        self._start_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrivilegedAccessScheduleInstance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedAccessScheduleInstance
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrivilegedAccessScheduleInstance()
    
    @property
    def end_date_time(self,) -> Optional[datetime]:
        """
        Gets the endDateTime property value. The endDateTime property
        Returns: Optional[datetime]
        """
        return self._end_date_time
    
    @end_date_time.setter
    def end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the endDateTime property value. The endDateTime property
        Args:
            value: Value to set for the endDateTime property.
        """
        self._end_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "end_date_time": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
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
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_datetime_value("startDateTime", self.start_date_time)
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. The startDateTime property
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. The startDateTime property
        Args:
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value
    
