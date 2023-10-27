from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .recommended_action import RecommendedAction
    from .simulation_events_content import SimulationEventsContent
    from .training_events_content import TrainingEventsContent

@dataclass
class SimulationReportOverview(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # List of recommended actions for a tenant to improve its security posture based on the attack simulation and training campaign attack type.
    recommended_actions: Optional[List[RecommendedAction]] = None
    # Number of valid users in the attack simulation and training campaign.
    resolved_targets_count: Optional[int] = None
    # Summary of simulation events in the attack simulation and training campaign.
    simulation_events_content: Optional[SimulationEventsContent] = None
    # Summary of assigned trainings in the attack simulation and training campaign.
    training_events_content: Optional[TrainingEventsContent] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SimulationReportOverview:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SimulationReportOverview
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SimulationReportOverview()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .recommended_action import RecommendedAction
        from .simulation_events_content import SimulationEventsContent
        from .training_events_content import TrainingEventsContent

        from .recommended_action import RecommendedAction
        from .simulation_events_content import SimulationEventsContent
        from .training_events_content import TrainingEventsContent

        fields: Dict[str, Callable[[Any], None]] = {
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recommendedActions": lambda n : setattr(self, 'recommended_actions', n.get_collection_of_object_values(RecommendedAction)),
            "resolvedTargetsCount": lambda n : setattr(self, 'resolved_targets_count', n.get_int_value()),
            "simulationEventsContent": lambda n : setattr(self, 'simulation_events_content', n.get_object_value(SimulationEventsContent)),
            "trainingEventsContent": lambda n : setattr(self, 'training_events_content', n.get_object_value(TrainingEventsContent)),
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
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_collection_of_object_values("recommendedActions", self.recommended_actions)
        writer.write_int_value("resolvedTargetsCount", self.resolved_targets_count)
        writer.write_object_value("simulationEventsContent", self.simulation_events_content)
        writer.write_object_value("trainingEventsContent", self.training_events_content)
        writer.write_additional_data_value(self.additional_data)
    
