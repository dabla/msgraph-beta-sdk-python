from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.o_data_errors.o_data_error import ODataError
    from .....models.unified_role_eligibility_schedule_request import UnifiedRoleEligibilityScheduleRequest
    from .app_scope.app_scope_request_builder import AppScopeRequestBuilder
    from .cancel.cancel_request_builder import CancelRequestBuilder
    from .directory_scope.directory_scope_request_builder import DirectoryScopeRequestBuilder
    from .principal.principal_request_builder import PrincipalRequestBuilder
    from .role_definition.role_definition_request_builder import RoleDefinitionRequestBuilder
    from .target_schedule.target_schedule_request_builder import TargetScheduleRequestBuilder

class UnifiedRoleEligibilityScheduleRequestItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the roleEligibilityScheduleRequests property of the microsoft.graph.rbacApplication entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new UnifiedRoleEligibilityScheduleRequestItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/roleManagement/directory/roleEligibilityScheduleRequests/{unifiedRoleEligibilityScheduleRequest%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[UnifiedRoleEligibilityScheduleRequestItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property roleEligibilityScheduleRequests for roleManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[UnifiedRoleEligibilityScheduleRequestItemRequestBuilderGetRequestConfiguration] = None) -> Optional[UnifiedRoleEligibilityScheduleRequest]:
        """
        Read the properties and relationships of an unifiedRoleEligibilityScheduleRequest object. This API is available in the following national cloud deployments.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[UnifiedRoleEligibilityScheduleRequest]
        Find more info here: https://learn.microsoft.com/graph/api/unifiedroleeligibilityschedulerequest-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.unified_role_eligibility_schedule_request import UnifiedRoleEligibilityScheduleRequest

        return await self.request_adapter.send_async(request_info, UnifiedRoleEligibilityScheduleRequest, error_mapping)
    
    async def patch(self,body: Optional[UnifiedRoleEligibilityScheduleRequest] = None, request_configuration: Optional[UnifiedRoleEligibilityScheduleRequestItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[UnifiedRoleEligibilityScheduleRequest]:
        """
        Update the navigation property roleEligibilityScheduleRequests in roleManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[UnifiedRoleEligibilityScheduleRequest]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.unified_role_eligibility_schedule_request import UnifiedRoleEligibilityScheduleRequest

        return await self.request_adapter.send_async(request_info, UnifiedRoleEligibilityScheduleRequest, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[UnifiedRoleEligibilityScheduleRequestItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property roleEligibilityScheduleRequests for roleManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        request_info.headers.try_add("Accept", "application/json, application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[UnifiedRoleEligibilityScheduleRequestItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Read the properties and relationships of an unifiedRoleEligibilityScheduleRequest object. This API is available in the following national cloud deployments.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json;q=1")
        return request_info
    
    def to_patch_request_information(self,body: Optional[UnifiedRoleEligibilityScheduleRequest] = None, request_configuration: Optional[UnifiedRoleEligibilityScheduleRequestItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property roleEligibilityScheduleRequests in roleManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers.try_add("Accept", "application/json;q=1")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> UnifiedRoleEligibilityScheduleRequestItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: UnifiedRoleEligibilityScheduleRequestItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return UnifiedRoleEligibilityScheduleRequestItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def app_scope(self) -> AppScopeRequestBuilder:
        """
        Provides operations to manage the appScope property of the microsoft.graph.unifiedRoleEligibilityScheduleRequest entity.
        """
        from .app_scope.app_scope_request_builder import AppScopeRequestBuilder

        return AppScopeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cancel(self) -> CancelRequestBuilder:
        """
        Provides operations to call the cancel method.
        """
        from .cancel.cancel_request_builder import CancelRequestBuilder

        return CancelRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def directory_scope(self) -> DirectoryScopeRequestBuilder:
        """
        Provides operations to manage the directoryScope property of the microsoft.graph.unifiedRoleEligibilityScheduleRequest entity.
        """
        from .directory_scope.directory_scope_request_builder import DirectoryScopeRequestBuilder

        return DirectoryScopeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def principal(self) -> PrincipalRequestBuilder:
        """
        Provides operations to manage the principal property of the microsoft.graph.unifiedRoleEligibilityScheduleRequest entity.
        """
        from .principal.principal_request_builder import PrincipalRequestBuilder

        return PrincipalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_definition(self) -> RoleDefinitionRequestBuilder:
        """
        Provides operations to manage the roleDefinition property of the microsoft.graph.unifiedRoleEligibilityScheduleRequest entity.
        """
        from .role_definition.role_definition_request_builder import RoleDefinitionRequestBuilder

        return RoleDefinitionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def target_schedule(self) -> TargetScheduleRequestBuilder:
        """
        Provides operations to manage the targetSchedule property of the microsoft.graph.unifiedRoleEligibilityScheduleRequest entity.
        """
        from .target_schedule.target_schedule_request_builder import TargetScheduleRequestBuilder

        return TargetScheduleRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class UnifiedRoleEligibilityScheduleRequestItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class UnifiedRoleEligibilityScheduleRequestItemRequestBuilderGetQueryParameters():
        """
        Read the properties and relationships of an unifiedRoleEligibilityScheduleRequest object. This API is available in the following national cloud deployments.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class UnifiedRoleEligibilityScheduleRequestItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[UnifiedRoleEligibilityScheduleRequestItemRequestBuilder.UnifiedRoleEligibilityScheduleRequestItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class UnifiedRoleEligibilityScheduleRequestItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
