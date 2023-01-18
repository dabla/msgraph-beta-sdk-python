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

cancel_request_builder = lazy_import('msgraph.generated.identity_governance.privileged_access.group.eligibility_schedule_requests.item.cancel.cancel_request_builder')
group_request_builder = lazy_import('msgraph.generated.identity_governance.privileged_access.group.eligibility_schedule_requests.item.group.group_request_builder')
principal_request_builder = lazy_import('msgraph.generated.identity_governance.privileged_access.group.eligibility_schedule_requests.item.principal.principal_request_builder')
target_schedule_request_builder = lazy_import('msgraph.generated.identity_governance.privileged_access.group.eligibility_schedule_requests.item.target_schedule.target_schedule_request_builder')
privileged_access_group_eligibility_schedule_request = lazy_import('msgraph.generated.models.privileged_access_group_eligibility_schedule_request')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class PrivilegedAccessGroupEligibilityScheduleRequestItemRequestBuilder():
    """
    Provides operations to manage the eligibilityScheduleRequests property of the microsoft.graph.privilegedAccessGroup entity.
    """
    @property
    def cancel(self) -> cancel_request_builder.CancelRequestBuilder:
        """
        Provides operations to call the cancel method.
        """
        return cancel_request_builder.CancelRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group(self) -> group_request_builder.GroupRequestBuilder:
        """
        Provides operations to manage the group property of the microsoft.graph.privilegedAccessGroupEligibilityScheduleRequest entity.
        """
        return group_request_builder.GroupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def principal(self) -> principal_request_builder.PrincipalRequestBuilder:
        """
        Provides operations to manage the principal property of the microsoft.graph.privilegedAccessGroupEligibilityScheduleRequest entity.
        """
        return principal_request_builder.PrincipalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def target_schedule(self) -> target_schedule_request_builder.TargetScheduleRequestBuilder:
        """
        Provides operations to manage the targetSchedule property of the microsoft.graph.privilegedAccessGroupEligibilityScheduleRequest entity.
        """
        return target_schedule_request_builder.TargetScheduleRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new PrivilegedAccessGroupEligibilityScheduleRequestItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/identityGovernance/privilegedAccess/group/eligibilityScheduleRequests/{privilegedAccessGroupEligibilityScheduleRequest%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[PrivilegedAccessGroupEligibilityScheduleRequestItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property eligibilityScheduleRequests for identityGovernance
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
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
        return await self.request_adapter.send_no_response_content_async(request_info, response_handler, error_mapping)
    
    async def get(self,request_configuration: Optional[PrivilegedAccessGroupEligibilityScheduleRequestItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[privileged_access_group_eligibility_schedule_request.PrivilegedAccessGroupEligibilityScheduleRequest]:
        """
        Get eligibilityScheduleRequests from identityGovernance
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[privileged_access_group_eligibility_schedule_request.PrivilegedAccessGroupEligibilityScheduleRequest]
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
        return await self.request_adapter.send_async(request_info, privileged_access_group_eligibility_schedule_request.PrivilegedAccessGroupEligibilityScheduleRequest, response_handler, error_mapping)
    
    async def patch(self,body: Optional[privileged_access_group_eligibility_schedule_request.PrivilegedAccessGroupEligibilityScheduleRequest] = None, request_configuration: Optional[PrivilegedAccessGroupEligibilityScheduleRequestItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[privileged_access_group_eligibility_schedule_request.PrivilegedAccessGroupEligibilityScheduleRequest]:
        """
        Update the navigation property eligibilityScheduleRequests in identityGovernance
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[privileged_access_group_eligibility_schedule_request.PrivilegedAccessGroupEligibilityScheduleRequest]
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
        return await self.request_adapter.send_async(request_info, privileged_access_group_eligibility_schedule_request.PrivilegedAccessGroupEligibilityScheduleRequest, response_handler, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[PrivilegedAccessGroupEligibilityScheduleRequestItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property eligibilityScheduleRequests for identityGovernance
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
    
    def to_get_request_information(self,request_configuration: Optional[PrivilegedAccessGroupEligibilityScheduleRequestItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get eligibilityScheduleRequests from identityGovernance
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[privileged_access_group_eligibility_schedule_request.PrivilegedAccessGroupEligibilityScheduleRequest] = None, request_configuration: Optional[PrivilegedAccessGroupEligibilityScheduleRequestItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property eligibilityScheduleRequests in identityGovernance
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
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @dataclass
    class PrivilegedAccessGroupEligibilityScheduleRequestItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class PrivilegedAccessGroupEligibilityScheduleRequestItemRequestBuilderGetQueryParameters():
        """
        Get eligibilityScheduleRequests from identityGovernance
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
    class PrivilegedAccessGroupEligibilityScheduleRequestItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[PrivilegedAccessGroupEligibilityScheduleRequestItemRequestBuilder.PrivilegedAccessGroupEligibilityScheduleRequestItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class PrivilegedAccessGroupEligibilityScheduleRequestItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

