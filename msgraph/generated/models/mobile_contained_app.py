from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, microsoft_store_for_business_contained_app, windows_universal_app_x_contained_app

from . import entity

class MobileContainedApp(entity.Entity):
    """
    An abstract class that represents a contained app in a mobileApp acting as a package.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new mobileContainedApp and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileContainedApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MobileContainedApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.microsoftStoreForBusinessContainedApp":
                from . import microsoft_store_for_business_contained_app

                return microsoft_store_for_business_contained_app.MicrosoftStoreForBusinessContainedApp()
            if mapping_value == "#microsoft.graph.windowsUniversalAppXContainedApp":
                from . import windows_universal_app_x_contained_app

                return windows_universal_app_x_contained_app.WindowsUniversalAppXContainedApp()
        return MobileContainedApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, microsoft_store_for_business_contained_app, windows_universal_app_x_contained_app

        fields: Dict[str, Callable[[Any], None]] = {
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
    

