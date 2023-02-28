from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

apps_request_builder = lazy_import('msgraph.generated.device_app_management.windows_managed_app_protections.item.apps.apps_request_builder')
managed_mobile_app_item_request_builder = lazy_import('msgraph.generated.device_app_management.windows_managed_app_protections.item.apps.item.managed_mobile_app_item_request_builder')
assign_request_builder = lazy_import('msgraph.generated.device_app_management.windows_managed_app_protections.item.assign.assign_request_builder')
assignments_request_builder = lazy_import('msgraph.generated.device_app_management.windows_managed_app_protections.item.assignments.assignments_request_builder')
targeted_managed_app_policy_assignment_item_request_builder = lazy_import('msgraph.generated.device_app_management.windows_managed_app_protections.item.assignments.item.targeted_managed_app_policy_assignment_item_request_builder')
target_apps_request_builder = lazy_import('msgraph.generated.device_app_management.windows_managed_app_protections.item.target_apps.target_apps_request_builder')
windows_managed_app_protection = lazy_import('msgraph.generated.models.windows_managed_app_protection')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class WindowsManagedAppProtectionItemRequestBuilder():
    """
    Provides operations to manage the windowsManagedAppProtections property of the microsoft.graph.deviceAppManagement entity.
    """
    @property
    def apps(self) -> apps_request_builder.AppsRequestBuilder:
        """
        Provides operations to manage the apps property of the microsoft.graph.windowsManagedAppProtection entity.
        """
        return apps_request_builder.AppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assign(self) -> assign_request_builder.AssignRequestBuilder:
        """
        Provides operations to call the assign method.
        """
        return assign_request_builder.AssignRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignments(self) -> assignments_request_builder.AssignmentsRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.windowsManagedAppProtection entity.
        """
        return assignments_request_builder.AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def target_apps(self) -> target_apps_request_builder.TargetAppsRequestBuilder:
        """
        Provides operations to call the targetApps method.
        """
        return target_apps_request_builder.TargetAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def apps_by_id(self,id: str) -> managed_mobile_app_item_request_builder.ManagedMobileAppItemRequestBuilder:
        """
        Provides operations to manage the apps property of the microsoft.graph.windowsManagedAppProtection entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_mobile_app_item_request_builder.ManagedMobileAppItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedMobileApp%2Did"] = id
        return managed_mobile_app_item_request_builder.ManagedMobileAppItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def assignments_by_id(self,id: str) -> targeted_managed_app_policy_assignment_item_request_builder.TargetedManagedAppPolicyAssignmentItemRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.windowsManagedAppProtection entity.
        Args:
            id: Unique identifier of the item
        Returns: targeted_managed_app_policy_assignment_item_request_builder.TargetedManagedAppPolicyAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["targetedManagedAppPolicyAssignment%2Did"] = id
        return targeted_managed_app_policy_assignment_item_request_builder.TargetedManagedAppPolicyAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new WindowsManagedAppProtectionItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceAppManagement/windowsManagedAppProtections/{windowsManagedAppProtection%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[WindowsManagedAppProtectionItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property windowsManagedAppProtections for deviceAppManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[WindowsManagedAppProtectionItemRequestBuilderGetRequestConfiguration] = None) -> Optional[windows_managed_app_protection.WindowsManagedAppProtection]:
        """
        Windows managed app policies.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[windows_managed_app_protection.WindowsManagedAppProtection]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, windows_managed_app_protection.WindowsManagedAppProtection, error_mapping)
    
    async def patch(self,body: Optional[windows_managed_app_protection.WindowsManagedAppProtection] = None, request_configuration: Optional[WindowsManagedAppProtectionItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[windows_managed_app_protection.WindowsManagedAppProtection]:
        """
        Update the navigation property windowsManagedAppProtections in deviceAppManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[windows_managed_app_protection.WindowsManagedAppProtection]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, windows_managed_app_protection.WindowsManagedAppProtection, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[WindowsManagedAppProtectionItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property windowsManagedAppProtections for deviceAppManagement
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
    
    def to_get_request_information(self,request_configuration: Optional[WindowsManagedAppProtectionItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Windows managed app policies.
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
    
    def to_patch_request_information(self,body: Optional[windows_managed_app_protection.WindowsManagedAppProtection] = None, request_configuration: Optional[WindowsManagedAppProtectionItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property windowsManagedAppProtections in deviceAppManagement
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
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @dataclass
    class WindowsManagedAppProtectionItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class WindowsManagedAppProtectionItemRequestBuilderGetQueryParameters():
        """
        Windows managed app policies.
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

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
        
    
    @dataclass
    class WindowsManagedAppProtectionItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[WindowsManagedAppProtectionItemRequestBuilder.WindowsManagedAppProtectionItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class WindowsManagedAppProtectionItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

