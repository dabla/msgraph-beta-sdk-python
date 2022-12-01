from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import authentication_app_admin_configuration, authentication_app_evaluation, authentication_app_policy_status

class AuthenticationAppPolicyDetails(AdditionalDataHolder, Parsable):
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
    
    @property
    def admin_configuration(self,) -> Optional[authentication_app_admin_configuration.AuthenticationAppAdminConfiguration]:
        """
        Gets the adminConfiguration property value. The adminConfiguration property
        Returns: Optional[authentication_app_admin_configuration.AuthenticationAppAdminConfiguration]
        """
        return self._admin_configuration
    
    @admin_configuration.setter
    def admin_configuration(self,value: Optional[authentication_app_admin_configuration.AuthenticationAppAdminConfiguration] = None) -> None:
        """
        Sets the adminConfiguration property value. The adminConfiguration property
        Args:
            value: Value to set for the adminConfiguration property.
        """
        self._admin_configuration = value
    
    @property
    def authentication_evaluation(self,) -> Optional[authentication_app_evaluation.AuthenticationAppEvaluation]:
        """
        Gets the authenticationEvaluation property value. The authenticationEvaluation property
        Returns: Optional[authentication_app_evaluation.AuthenticationAppEvaluation]
        """
        return self._authentication_evaluation
    
    @authentication_evaluation.setter
    def authentication_evaluation(self,value: Optional[authentication_app_evaluation.AuthenticationAppEvaluation] = None) -> None:
        """
        Sets the authenticationEvaluation property value. The authenticationEvaluation property
        Args:
            value: Value to set for the authenticationEvaluation property.
        """
        self._authentication_evaluation = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new authenticationAppPolicyDetails and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The adminConfiguration property
        self._admin_configuration: Optional[authentication_app_admin_configuration.AuthenticationAppAdminConfiguration] = None
        # The authenticationEvaluation property
        self._authentication_evaluation: Optional[authentication_app_evaluation.AuthenticationAppEvaluation] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The policyName property
        self._policy_name: Optional[str] = None
        # The status property
        self._status: Optional[authentication_app_policy_status.AuthenticationAppPolicyStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationAppPolicyDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationAppPolicyDetails
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuthenticationAppPolicyDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "admin_configuration": lambda n : setattr(self, 'admin_configuration', n.get_enum_value(authentication_app_admin_configuration.AuthenticationAppAdminConfiguration)),
            "authentication_evaluation": lambda n : setattr(self, 'authentication_evaluation', n.get_enum_value(authentication_app_evaluation.AuthenticationAppEvaluation)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "policy_name": lambda n : setattr(self, 'policy_name', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(authentication_app_policy_status.AuthenticationAppPolicyStatus)),
        }
        return fields
    
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
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def policy_name(self,) -> Optional[str]:
        """
        Gets the policyName property value. The policyName property
        Returns: Optional[str]
        """
        return self._policy_name
    
    @policy_name.setter
    def policy_name(self,value: Optional[str] = None) -> None:
        """
        Sets the policyName property value. The policyName property
        Args:
            value: Value to set for the policyName property.
        """
        self._policy_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("adminConfiguration", self.admin_configuration)
        writer.write_enum_value("authenticationEvaluation", self.authentication_evaluation)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("policyName", self.policy_name)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def status(self,) -> Optional[authentication_app_policy_status.AuthenticationAppPolicyStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[authentication_app_policy_status.AuthenticationAppPolicyStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[authentication_app_policy_status.AuthenticationAppPolicyStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
