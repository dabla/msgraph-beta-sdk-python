from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models import access_package_assignment_policy
    from .....models.o_data_errors import o_data_error
    from .access_package import access_package_request_builder
    from .access_package_catalog import access_package_catalog_request_builder
    from .custom_extension_handlers import custom_extension_handlers_request_builder
    from .custom_extension_stage_settings import custom_extension_stage_settings_request_builder

class AccessPackageAssignmentPolicyItemRequestBuilder():
    """
    Provides operations to manage the accessPackageAssignmentPolicies property of the microsoft.graph.entitlementManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AccessPackageAssignmentPolicyItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/identityGovernance/entitlementManagement/accessPackageAssignmentPolicies/{accessPackageAssignmentPolicy%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[AccessPackageAssignmentPolicyItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property accessPackageAssignmentPolicies for identityGovernance
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[AccessPackageAssignmentPolicyItemRequestBuilderGetRequestConfiguration] = None) -> Optional[access_package_assignment_policy.AccessPackageAssignmentPolicy]:
        """
        Represents the policy that governs which subjects can request or be assigned an access package via an access package assignment.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[access_package_assignment_policy.AccessPackageAssignmentPolicy]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models import access_package_assignment_policy

        return await self.request_adapter.send_async(request_info, access_package_assignment_policy.AccessPackageAssignmentPolicy, error_mapping)
    
    async def put(self,body: Optional[access_package_assignment_policy.AccessPackageAssignmentPolicy] = None, request_configuration: Optional[AccessPackageAssignmentPolicyItemRequestBuilderPutRequestConfiguration] = None) -> Optional[access_package_assignment_policy.AccessPackageAssignmentPolicy]:
        """
        Update the navigation property accessPackageAssignmentPolicies in identityGovernance
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[access_package_assignment_policy.AccessPackageAssignmentPolicy]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models import access_package_assignment_policy

        return await self.request_adapter.send_async(request_info, access_package_assignment_policy.AccessPackageAssignmentPolicy, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[AccessPackageAssignmentPolicyItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property accessPackageAssignmentPolicies for identityGovernance
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[AccessPackageAssignmentPolicyItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Represents the policy that governs which subjects can request or be assigned an access package via an access package assignment.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_put_request_information(self,body: Optional[access_package_assignment_policy.AccessPackageAssignmentPolicy] = None, request_configuration: Optional[AccessPackageAssignmentPolicyItemRequestBuilderPutRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property accessPackageAssignmentPolicies in identityGovernance
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PUT
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def access_package(self) -> access_package_request_builder.AccessPackageRequestBuilder:
        """
        Provides operations to manage the accessPackage property of the microsoft.graph.accessPackageAssignmentPolicy entity.
        """
        from .access_package import access_package_request_builder

        return access_package_request_builder.AccessPackageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def access_package_catalog(self) -> access_package_catalog_request_builder.AccessPackageCatalogRequestBuilder:
        """
        Provides operations to manage the accessPackageCatalog property of the microsoft.graph.accessPackageAssignmentPolicy entity.
        """
        from .access_package_catalog import access_package_catalog_request_builder

        return access_package_catalog_request_builder.AccessPackageCatalogRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def custom_extension_handlers(self) -> custom_extension_handlers_request_builder.CustomExtensionHandlersRequestBuilder:
        """
        Provides operations to manage the customExtensionHandlers property of the microsoft.graph.accessPackageAssignmentPolicy entity.
        """
        from .custom_extension_handlers import custom_extension_handlers_request_builder

        return custom_extension_handlers_request_builder.CustomExtensionHandlersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def custom_extension_stage_settings(self) -> custom_extension_stage_settings_request_builder.CustomExtensionStageSettingsRequestBuilder:
        """
        Provides operations to manage the customExtensionStageSettings property of the microsoft.graph.accessPackageAssignmentPolicy entity.
        """
        from .custom_extension_stage_settings import custom_extension_stage_settings_request_builder

        return custom_extension_stage_settings_request_builder.CustomExtensionStageSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AccessPackageAssignmentPolicyItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class AccessPackageAssignmentPolicyItemRequestBuilderGetQueryParameters():
        """
        Represents the policy that governs which subjects can request or be assigned an access package via an access package assignment.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class AccessPackageAssignmentPolicyItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[AccessPackageAssignmentPolicyItemRequestBuilder.AccessPackageAssignmentPolicyItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class AccessPackageAssignmentPolicyItemRequestBuilderPutRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

