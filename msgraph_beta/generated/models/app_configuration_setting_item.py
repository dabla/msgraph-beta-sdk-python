from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mdm_app_config_key_type import MdmAppConfigKeyType

@dataclass
class AppConfigurationSettingItem(AdditionalDataHolder, BackedModel, Parsable):
    """
    Contains properties for App configuration setting item.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # app configuration key.
    app_config_key: Optional[str] = None
    # App configuration key types.
    app_config_key_type: Optional[MdmAppConfigKeyType] = None
    # app configuration key value.
    app_config_key_value: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppConfigurationSettingItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AppConfigurationSettingItem
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AppConfigurationSettingItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .mdm_app_config_key_type import MdmAppConfigKeyType

        from .mdm_app_config_key_type import MdmAppConfigKeyType

        fields: Dict[str, Callable[[Any], None]] = {
            "appConfigKey": lambda n : setattr(self, 'app_config_key', n.get_str_value()),
            "appConfigKeyType": lambda n : setattr(self, 'app_config_key_type', n.get_enum_value(MdmAppConfigKeyType)),
            "appConfigKeyValue": lambda n : setattr(self, 'app_config_key_value', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("appConfigKey", self.app_config_key)
        writer.write_enum_value("appConfigKeyType", self.app_config_key_type)
        writer.write_str_value("appConfigKeyValue", self.app_config_key_value)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    
