from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_review_policy import AccessReviewPolicy
    from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
    from .admin_consent_request_policy import AdminConsentRequestPolicy
    from .app_management_policy import AppManagementPolicy
    from .authentication_flows_policy import AuthenticationFlowsPolicy
    from .authentication_methods_policy import AuthenticationMethodsPolicy
    from .authentication_strength_policy import AuthenticationStrengthPolicy
    from .authorization_policy import AuthorizationPolicy
    from .b2c_authentication_methods_policy import B2cAuthenticationMethodsPolicy
    from .claims_mapping_policy import ClaimsMappingPolicy
    from .conditional_access_policy import ConditionalAccessPolicy
    from .cross_tenant_access_policy import CrossTenantAccessPolicy
    from .device_registration_policy import DeviceRegistrationPolicy
    from .directory_role_access_review_policy import DirectoryRoleAccessReviewPolicy
    from .external_identities_policy import ExternalIdentitiesPolicy
    from .feature_rollout_policy import FeatureRolloutPolicy
    from .federated_token_validation_policy import FederatedTokenValidationPolicy
    from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
    from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy
    from .mobility_management_policy import MobilityManagementPolicy
    from .permission_grant_policy import PermissionGrantPolicy
    from .service_principal_creation_policy import ServicePrincipalCreationPolicy
    from .tenant_app_management_policy import TenantAppManagementPolicy
    from .token_issuance_policy import TokenIssuancePolicy
    from .token_lifetime_policy import TokenLifetimePolicy
    from .unified_role_management_policy import UnifiedRoleManagementPolicy
    from .unified_role_management_policy_assignment import UnifiedRoleManagementPolicyAssignment

@dataclass
class PolicyRoot(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The policy that contains directory-level access review settings.
    access_review_policy: Optional[AccessReviewPolicy] = None
    # The policy that controls the idle time-out for web sessions for applications.
    activity_based_timeout_policies: Optional[List[ActivityBasedTimeoutPolicy]] = None
    # The policy by which consent requests are created and managed for the entire tenant.
    admin_consent_request_policy: Optional[AdminConsentRequestPolicy] = None
    # The policies that enforce app management restrictions for specific applications and service principals, overriding the defaultAppManagementPolicy.
    app_management_policies: Optional[List[AppManagementPolicy]] = None
    # The policy configuration of the self-service sign-up experience of guests.
    authentication_flows_policy: Optional[AuthenticationFlowsPolicy] = None
    # The authentication methods and the users that are allowed to use them to sign in and perform multifactor authentication (MFA) in Microsoft Entra ID.
    authentication_methods_policy: Optional[AuthenticationMethodsPolicy] = None
    # The authentication method combinations that are to be used in scenarios defined by Microsoft Entra Conditional Access.
    authentication_strength_policies: Optional[List[AuthenticationStrengthPolicy]] = None
    # The policy that controls Microsoft Entra authorization settings.
    authorization_policy: Optional[List[AuthorizationPolicy]] = None
    # The Azure AD B2C policies that define how end users register via local accounts.
    b2c_authentication_methods_policy: Optional[B2cAuthenticationMethodsPolicy] = None
    # The claim-mapping policies for WS-Fed, SAML, OAuth 2.0, and OpenID Connect protocols, for tokens issued to a specific application.
    claims_mapping_policies: Optional[List[ClaimsMappingPolicy]] = None
    # The custom rules that define an access scenario.
    conditional_access_policies: Optional[List[ConditionalAccessPolicy]] = None
    # The custom rules that define an access scenario when interacting with external Microsoft Entra tenants.
    cross_tenant_access_policy: Optional[CrossTenantAccessPolicy] = None
    # The tenant-wide policy that enforces app management restrictions for all applications and service principals.
    default_app_management_policy: Optional[TenantAppManagementPolicy] = None
    # The deviceRegistrationPolicy property
    device_registration_policy: Optional[DeviceRegistrationPolicy] = None
    # The directoryRoleAccessReviewPolicy property
    directory_role_access_review_policy: Optional[DirectoryRoleAccessReviewPolicy] = None
    # Represents the tenant-wide policy that controls whether guests can leave a Microsoft Entra tenant via self-service controls.
    external_identities_policy: Optional[ExternalIdentitiesPolicy] = None
    # The feature rollout policy associated with a directory object.
    feature_rollout_policies: Optional[List[FeatureRolloutPolicy]] = None
    # The federatedTokenValidationPolicy property
    federated_token_validation_policy: Optional[FederatedTokenValidationPolicy] = None
    # The policy to control Microsoft Entra authentication behavior for federated users.
    home_realm_discovery_policies: Optional[List[HomeRealmDiscoveryPolicy]] = None
    # The policy that represents the security defaults that protect against common attacks.
    identity_security_defaults_enforcement_policy: Optional[IdentitySecurityDefaultsEnforcementPolicy] = None
    # The policy that defines autoenrollment configuration for a mobility management (MDM or MAM) application.
    mobile_app_management_policies: Optional[List[MobilityManagementPolicy]] = None
    # The mobileDeviceManagementPolicies property
    mobile_device_management_policies: Optional[List[MobilityManagementPolicy]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The policy that specifies the conditions under which consent can be granted.
    permission_grant_policies: Optional[List[PermissionGrantPolicy]] = None
    # Represents the role management policies.
    role_management_policies: Optional[List[UnifiedRoleManagementPolicy]] = None
    # Represents the role management policy assignments.
    role_management_policy_assignments: Optional[List[UnifiedRoleManagementPolicyAssignment]] = None
    # The servicePrincipalCreationPolicies property
    service_principal_creation_policies: Optional[List[ServicePrincipalCreationPolicy]] = None
    # The policy that specifies the characteristics of SAML tokens issued by Microsoft Entra ID.
    token_issuance_policies: Optional[List[TokenIssuancePolicy]] = None
    # The policy that controls the lifetime of a JWT access token, an ID token, or a SAML 1.1/2.0 token issued by Microsoft Entra ID.
    token_lifetime_policies: Optional[List[TokenLifetimePolicy]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PolicyRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PolicyRoot
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PolicyRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .access_review_policy import AccessReviewPolicy
        from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
        from .admin_consent_request_policy import AdminConsentRequestPolicy
        from .app_management_policy import AppManagementPolicy
        from .authentication_flows_policy import AuthenticationFlowsPolicy
        from .authentication_methods_policy import AuthenticationMethodsPolicy
        from .authentication_strength_policy import AuthenticationStrengthPolicy
        from .authorization_policy import AuthorizationPolicy
        from .b2c_authentication_methods_policy import B2cAuthenticationMethodsPolicy
        from .claims_mapping_policy import ClaimsMappingPolicy
        from .conditional_access_policy import ConditionalAccessPolicy
        from .cross_tenant_access_policy import CrossTenantAccessPolicy
        from .device_registration_policy import DeviceRegistrationPolicy
        from .directory_role_access_review_policy import DirectoryRoleAccessReviewPolicy
        from .external_identities_policy import ExternalIdentitiesPolicy
        from .feature_rollout_policy import FeatureRolloutPolicy
        from .federated_token_validation_policy import FederatedTokenValidationPolicy
        from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
        from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy
        from .mobility_management_policy import MobilityManagementPolicy
        from .permission_grant_policy import PermissionGrantPolicy
        from .service_principal_creation_policy import ServicePrincipalCreationPolicy
        from .tenant_app_management_policy import TenantAppManagementPolicy
        from .token_issuance_policy import TokenIssuancePolicy
        from .token_lifetime_policy import TokenLifetimePolicy
        from .unified_role_management_policy import UnifiedRoleManagementPolicy
        from .unified_role_management_policy_assignment import UnifiedRoleManagementPolicyAssignment

        from .access_review_policy import AccessReviewPolicy
        from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
        from .admin_consent_request_policy import AdminConsentRequestPolicy
        from .app_management_policy import AppManagementPolicy
        from .authentication_flows_policy import AuthenticationFlowsPolicy
        from .authentication_methods_policy import AuthenticationMethodsPolicy
        from .authentication_strength_policy import AuthenticationStrengthPolicy
        from .authorization_policy import AuthorizationPolicy
        from .b2c_authentication_methods_policy import B2cAuthenticationMethodsPolicy
        from .claims_mapping_policy import ClaimsMappingPolicy
        from .conditional_access_policy import ConditionalAccessPolicy
        from .cross_tenant_access_policy import CrossTenantAccessPolicy
        from .device_registration_policy import DeviceRegistrationPolicy
        from .directory_role_access_review_policy import DirectoryRoleAccessReviewPolicy
        from .external_identities_policy import ExternalIdentitiesPolicy
        from .feature_rollout_policy import FeatureRolloutPolicy
        from .federated_token_validation_policy import FederatedTokenValidationPolicy
        from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
        from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy
        from .mobility_management_policy import MobilityManagementPolicy
        from .permission_grant_policy import PermissionGrantPolicy
        from .service_principal_creation_policy import ServicePrincipalCreationPolicy
        from .tenant_app_management_policy import TenantAppManagementPolicy
        from .token_issuance_policy import TokenIssuancePolicy
        from .token_lifetime_policy import TokenLifetimePolicy
        from .unified_role_management_policy import UnifiedRoleManagementPolicy
        from .unified_role_management_policy_assignment import UnifiedRoleManagementPolicyAssignment

        fields: Dict[str, Callable[[Any], None]] = {
            "accessReviewPolicy": lambda n : setattr(self, 'access_review_policy', n.get_object_value(AccessReviewPolicy)),
            "activityBasedTimeoutPolicies": lambda n : setattr(self, 'activity_based_timeout_policies', n.get_collection_of_object_values(ActivityBasedTimeoutPolicy)),
            "adminConsentRequestPolicy": lambda n : setattr(self, 'admin_consent_request_policy', n.get_object_value(AdminConsentRequestPolicy)),
            "appManagementPolicies": lambda n : setattr(self, 'app_management_policies', n.get_collection_of_object_values(AppManagementPolicy)),
            "authenticationFlowsPolicy": lambda n : setattr(self, 'authentication_flows_policy', n.get_object_value(AuthenticationFlowsPolicy)),
            "authenticationMethodsPolicy": lambda n : setattr(self, 'authentication_methods_policy', n.get_object_value(AuthenticationMethodsPolicy)),
            "authenticationStrengthPolicies": lambda n : setattr(self, 'authentication_strength_policies', n.get_collection_of_object_values(AuthenticationStrengthPolicy)),
            "authorizationPolicy": lambda n : setattr(self, 'authorization_policy', n.get_collection_of_object_values(AuthorizationPolicy)),
            "b2cAuthenticationMethodsPolicy": lambda n : setattr(self, 'b2c_authentication_methods_policy', n.get_object_value(B2cAuthenticationMethodsPolicy)),
            "claimsMappingPolicies": lambda n : setattr(self, 'claims_mapping_policies', n.get_collection_of_object_values(ClaimsMappingPolicy)),
            "conditionalAccessPolicies": lambda n : setattr(self, 'conditional_access_policies', n.get_collection_of_object_values(ConditionalAccessPolicy)),
            "crossTenantAccessPolicy": lambda n : setattr(self, 'cross_tenant_access_policy', n.get_object_value(CrossTenantAccessPolicy)),
            "defaultAppManagementPolicy": lambda n : setattr(self, 'default_app_management_policy', n.get_object_value(TenantAppManagementPolicy)),
            "deviceRegistrationPolicy": lambda n : setattr(self, 'device_registration_policy', n.get_object_value(DeviceRegistrationPolicy)),
            "directoryRoleAccessReviewPolicy": lambda n : setattr(self, 'directory_role_access_review_policy', n.get_object_value(DirectoryRoleAccessReviewPolicy)),
            "externalIdentitiesPolicy": lambda n : setattr(self, 'external_identities_policy', n.get_object_value(ExternalIdentitiesPolicy)),
            "featureRolloutPolicies": lambda n : setattr(self, 'feature_rollout_policies', n.get_collection_of_object_values(FeatureRolloutPolicy)),
            "federatedTokenValidationPolicy": lambda n : setattr(self, 'federated_token_validation_policy', n.get_object_value(FederatedTokenValidationPolicy)),
            "homeRealmDiscoveryPolicies": lambda n : setattr(self, 'home_realm_discovery_policies', n.get_collection_of_object_values(HomeRealmDiscoveryPolicy)),
            "identitySecurityDefaultsEnforcementPolicy": lambda n : setattr(self, 'identity_security_defaults_enforcement_policy', n.get_object_value(IdentitySecurityDefaultsEnforcementPolicy)),
            "mobileAppManagementPolicies": lambda n : setattr(self, 'mobile_app_management_policies', n.get_collection_of_object_values(MobilityManagementPolicy)),
            "mobileDeviceManagementPolicies": lambda n : setattr(self, 'mobile_device_management_policies', n.get_collection_of_object_values(MobilityManagementPolicy)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "permissionGrantPolicies": lambda n : setattr(self, 'permission_grant_policies', n.get_collection_of_object_values(PermissionGrantPolicy)),
            "roleManagementPolicies": lambda n : setattr(self, 'role_management_policies', n.get_collection_of_object_values(UnifiedRoleManagementPolicy)),
            "roleManagementPolicyAssignments": lambda n : setattr(self, 'role_management_policy_assignments', n.get_collection_of_object_values(UnifiedRoleManagementPolicyAssignment)),
            "servicePrincipalCreationPolicies": lambda n : setattr(self, 'service_principal_creation_policies', n.get_collection_of_object_values(ServicePrincipalCreationPolicy)),
            "tokenIssuancePolicies": lambda n : setattr(self, 'token_issuance_policies', n.get_collection_of_object_values(TokenIssuancePolicy)),
            "tokenLifetimePolicies": lambda n : setattr(self, 'token_lifetime_policies', n.get_collection_of_object_values(TokenLifetimePolicy)),
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
        writer.write_object_value("accessReviewPolicy", self.access_review_policy)
        writer.write_collection_of_object_values("activityBasedTimeoutPolicies", self.activity_based_timeout_policies)
        writer.write_object_value("adminConsentRequestPolicy", self.admin_consent_request_policy)
        writer.write_collection_of_object_values("appManagementPolicies", self.app_management_policies)
        writer.write_object_value("authenticationFlowsPolicy", self.authentication_flows_policy)
        writer.write_object_value("authenticationMethodsPolicy", self.authentication_methods_policy)
        writer.write_collection_of_object_values("authenticationStrengthPolicies", self.authentication_strength_policies)
        writer.write_collection_of_object_values("authorizationPolicy", self.authorization_policy)
        writer.write_object_value("b2cAuthenticationMethodsPolicy", self.b2c_authentication_methods_policy)
        writer.write_collection_of_object_values("claimsMappingPolicies", self.claims_mapping_policies)
        writer.write_collection_of_object_values("conditionalAccessPolicies", self.conditional_access_policies)
        writer.write_object_value("crossTenantAccessPolicy", self.cross_tenant_access_policy)
        writer.write_object_value("defaultAppManagementPolicy", self.default_app_management_policy)
        writer.write_object_value("deviceRegistrationPolicy", self.device_registration_policy)
        writer.write_object_value("directoryRoleAccessReviewPolicy", self.directory_role_access_review_policy)
        writer.write_object_value("externalIdentitiesPolicy", self.external_identities_policy)
        writer.write_collection_of_object_values("featureRolloutPolicies", self.feature_rollout_policies)
        writer.write_object_value("federatedTokenValidationPolicy", self.federated_token_validation_policy)
        writer.write_collection_of_object_values("homeRealmDiscoveryPolicies", self.home_realm_discovery_policies)
        writer.write_object_value("identitySecurityDefaultsEnforcementPolicy", self.identity_security_defaults_enforcement_policy)
        writer.write_collection_of_object_values("mobileAppManagementPolicies", self.mobile_app_management_policies)
        writer.write_collection_of_object_values("mobileDeviceManagementPolicies", self.mobile_device_management_policies)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("permissionGrantPolicies", self.permission_grant_policies)
        writer.write_collection_of_object_values("roleManagementPolicies", self.role_management_policies)
        writer.write_collection_of_object_values("roleManagementPolicyAssignments", self.role_management_policy_assignments)
        writer.write_collection_of_object_values("servicePrincipalCreationPolicies", self.service_principal_creation_policies)
        writer.write_collection_of_object_values("tokenIssuancePolicies", self.token_issuance_policies)
        writer.write_collection_of_object_values("tokenLifetimePolicies", self.token_lifetime_policies)
        writer.write_additional_data_value(self.additional_data)
    

