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

cancel_request_builder = lazy_import('msgraph.generated.governance_role_assignment_requests.item.cancel.cancel_request_builder')
resource_request_builder = lazy_import('msgraph.generated.governance_role_assignment_requests.item.resource.resource_request_builder')
role_definition_request_builder = lazy_import('msgraph.generated.governance_role_assignment_requests.item.role_definition.role_definition_request_builder')
subject_request_builder = lazy_import('msgraph.generated.governance_role_assignment_requests.item.subject.subject_request_builder')
update_request_request_builder = lazy_import('msgraph.generated.governance_role_assignment_requests.item.update_request.update_request_request_builder')
governance_role_assignment_request = lazy_import('msgraph.generated.models.governance_role_assignment_request')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class GovernanceRoleAssignmentRequestItemRequestBuilder():
    """
    Provides operations to manage the collection of governanceRoleAssignmentRequest entities.
    """
    @property
    def cancel(self) -> cancel_request_builder.CancelRequestBuilder:
        """
        Provides operations to call the cancel method.
        """
        return cancel_request_builder.CancelRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resource(self) -> resource_request_builder.ResourceRequestBuilder:
        """
        Provides operations to manage the resource property of the microsoft.graph.governanceRoleAssignmentRequest entity.
        """
        return resource_request_builder.ResourceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_definition(self) -> role_definition_request_builder.RoleDefinitionRequestBuilder:
        """
        Provides operations to manage the roleDefinition property of the microsoft.graph.governanceRoleAssignmentRequest entity.
        """
        return role_definition_request_builder.RoleDefinitionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def subject(self) -> subject_request_builder.SubjectRequestBuilder:
        """
        Provides operations to manage the subject property of the microsoft.graph.governanceRoleAssignmentRequest entity.
        """
        return subject_request_builder.SubjectRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def update_request(self) -> update_request_request_builder.UpdateRequestRequestBuilder:
        """
        Provides operations to call the updateRequest method.
        """
        return update_request_request_builder.UpdateRequestRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new GovernanceRoleAssignmentRequestItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/governanceRoleAssignmentRequests/{governanceRoleAssignmentRequest%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[GovernanceRoleAssignmentRequestItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete entity from governanceRoleAssignmentRequests
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
    
    async def get(self,request_configuration: Optional[GovernanceRoleAssignmentRequestItemRequestBuilderGetRequestConfiguration] = None) -> Optional[governance_role_assignment_request.GovernanceRoleAssignmentRequest]:
        """
        Get entity from governanceRoleAssignmentRequests by key
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[governance_role_assignment_request.GovernanceRoleAssignmentRequest]
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
        return await self.request_adapter.send_async(request_info, governance_role_assignment_request.GovernanceRoleAssignmentRequest, error_mapping)
    
    async def patch(self,body: Optional[governance_role_assignment_request.GovernanceRoleAssignmentRequest] = None, request_configuration: Optional[GovernanceRoleAssignmentRequestItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[governance_role_assignment_request.GovernanceRoleAssignmentRequest]:
        """
        Update entity in governanceRoleAssignmentRequests
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[governance_role_assignment_request.GovernanceRoleAssignmentRequest]
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
        return await self.request_adapter.send_async(request_info, governance_role_assignment_request.GovernanceRoleAssignmentRequest, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[GovernanceRoleAssignmentRequestItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete entity from governanceRoleAssignmentRequests
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
    
    def to_get_request_information(self,request_configuration: Optional[GovernanceRoleAssignmentRequestItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get entity from governanceRoleAssignmentRequests by key
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
    
    def to_patch_request_information(self,body: Optional[governance_role_assignment_request.GovernanceRoleAssignmentRequest] = None, request_configuration: Optional[GovernanceRoleAssignmentRequestItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update entity in governanceRoleAssignmentRequests
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
    class GovernanceRoleAssignmentRequestItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class GovernanceRoleAssignmentRequestItemRequestBuilderGetQueryParameters():
        """
        Get entity from governanceRoleAssignmentRequests by key
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
    class GovernanceRoleAssignmentRequestItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[GovernanceRoleAssignmentRequestItemRequestBuilder.GovernanceRoleAssignmentRequestItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class GovernanceRoleAssignmentRequestItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

