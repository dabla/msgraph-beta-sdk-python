from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .giphy_rating_type import GiphyRatingType

@dataclass
class TeamFunSettings(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # If set to true, enables users to include custom memes.
    allow_custom_memes: Optional[bool] = None
    # If set to true, enables Giphy use.
    allow_giphy: Optional[bool] = None
    # If set to true, enables users to include stickers and memes.
    allow_stickers_and_memes: Optional[bool] = None
    # Giphy content rating. Possible values are: moderate, strict.
    giphy_content_rating: Optional[GiphyRatingType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamFunSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamFunSettings
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TeamFunSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .giphy_rating_type import GiphyRatingType

        from .giphy_rating_type import GiphyRatingType

        fields: Dict[str, Callable[[Any], None]] = {
            "allowCustomMemes": lambda n : setattr(self, 'allow_custom_memes', n.get_bool_value()),
            "allowGiphy": lambda n : setattr(self, 'allow_giphy', n.get_bool_value()),
            "allowStickersAndMemes": lambda n : setattr(self, 'allow_stickers_and_memes', n.get_bool_value()),
            "giphyContentRating": lambda n : setattr(self, 'giphy_content_rating', n.get_enum_value(GiphyRatingType)),
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
        writer.write_bool_value("allowCustomMemes", self.allow_custom_memes)
        writer.write_bool_value("allowGiphy", self.allow_giphy)
        writer.write_bool_value("allowStickersAndMemes", self.allow_stickers_and_memes)
        writer.write_enum_value("giphyContentRating", self.giphy_content_rating)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    
