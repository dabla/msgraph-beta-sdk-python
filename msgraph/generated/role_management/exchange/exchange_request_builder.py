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
    from ...models import unified_rbac_application
    from ...models.o_data_errors import o_data_error
    from .resource_namespaces import resource_namespaces_request_builder
    from .resource_namespaces.item import unified_rbac_resource_namespace_item_request_builder
    from .role_assignments import role_assignments_request_builder
    from .role_assignments.item import unified_role_assignment_item_request_builder
    from .role_definitions import role_definitions_request_builder
    from .role_definitions.item import unified_role_definition_item_request_builder
    from .transitive_role_assignments import transitive_role_assignments_request_builder
    from .transitive_role_assignments.item import unified_role_assignment_item_request_builder

class ExchangeRequestBuilder():
    """
    Provides operations to manage the exchange property of the microsoft.graph.roleManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ExchangeRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/roleManagement/exchange{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[ExchangeRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property exchange for roleManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[ExchangeRequestBuilderGetRequestConfiguration] = None) -> Optional[unified_rbac_application.UnifiedRbacApplication]:
        """
        Get exchange from roleManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[unified_rbac_application.UnifiedRbacApplication]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import unified_rbac_application

        return await self.request_adapter.send_async(request_info, unified_rbac_application.UnifiedRbacApplication, error_mapping)
    
    async def patch(self,body: Optional[unified_rbac_application.UnifiedRbacApplication] = None, request_configuration: Optional[ExchangeRequestBuilderPatchRequestConfiguration] = None) -> Optional[unified_rbac_application.UnifiedRbacApplication]:
        """
        Update the navigation property exchange in roleManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[unified_rbac_application.UnifiedRbacApplication]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import unified_rbac_application

        return await self.request_adapter.send_async(request_info, unified_rbac_application.UnifiedRbacApplication, error_mapping)
    
    def resource_namespaces_by_id(self,id: str) -> unified_rbac_resource_namespace_item_request_builder.UnifiedRbacResourceNamespaceItemRequestBuilder:
        """
        Provides operations to manage the resourceNamespaces property of the microsoft.graph.unifiedRbacApplication entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_rbac_resource_namespace_item_request_builder.UnifiedRbacResourceNamespaceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .resource_namespaces.item import unified_rbac_resource_namespace_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRbacResourceNamespace%2Did"] = id
        return unified_rbac_resource_namespace_item_request_builder.UnifiedRbacResourceNamespaceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def role_assignments_by_id(self,id: str) -> unified_role_assignment_item_request_builder.UnifiedRoleAssignmentItemRequestBuilder:
        """
        Provides operations to manage the roleAssignments property of the microsoft.graph.unifiedRbacApplication entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_role_assignment_item_request_builder.UnifiedRoleAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .role_assignments.item import unified_role_assignment_item_request_builder
        from .transitive_role_assignments.item import unified_role_assignment_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRoleAssignment%2Did"] = id
        return unified_role_assignment_item_request_builder.UnifiedRoleAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def role_definitions_by_id(self,id: str) -> unified_role_definition_item_request_builder.UnifiedRoleDefinitionItemRequestBuilder:
        """
        Provides operations to manage the roleDefinitions property of the microsoft.graph.unifiedRbacApplication entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_role_definition_item_request_builder.UnifiedRoleDefinitionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .role_definitions.item import unified_role_definition_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRoleDefinition%2Did"] = id
        return unified_role_definition_item_request_builder.UnifiedRoleDefinitionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[ExchangeRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property exchange for roleManagement
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
    
    def to_get_request_information(self,request_configuration: Optional[ExchangeRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get exchange from roleManagement
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
    
    def to_patch_request_information(self,body: Optional[unified_rbac_application.UnifiedRbacApplication] = None, request_configuration: Optional[ExchangeRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property exchange in roleManagement
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
    
    def transitive_role_assignments_by_id(self,id: str) -> unified_role_assignment_item_request_builder.UnifiedRoleAssignmentItemRequestBuilder:
        """
        Provides operations to manage the transitiveRoleAssignments property of the microsoft.graph.unifiedRbacApplication entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_role_assignment_item_request_builder.UnifiedRoleAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .role_assignments.item import unified_role_assignment_item_request_builder
        from .transitive_role_assignments.item import unified_role_assignment_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRoleAssignment%2Did"] = id
        return unified_role_assignment_item_request_builder.UnifiedRoleAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def resource_namespaces(self) -> resource_namespaces_request_builder.ResourceNamespacesRequestBuilder:
        """
        Provides operations to manage the resourceNamespaces property of the microsoft.graph.unifiedRbacApplication entity.
        """
        from .resource_namespaces import resource_namespaces_request_builder

        return resource_namespaces_request_builder.ResourceNamespacesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_assignments(self) -> role_assignments_request_builder.RoleAssignmentsRequestBuilder:
        """
        Provides operations to manage the roleAssignments property of the microsoft.graph.unifiedRbacApplication entity.
        """
        from .role_assignments import role_assignments_request_builder

        return role_assignments_request_builder.RoleAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_definitions(self) -> role_definitions_request_builder.RoleDefinitionsRequestBuilder:
        """
        Provides operations to manage the roleDefinitions property of the microsoft.graph.unifiedRbacApplication entity.
        """
        from .role_definitions import role_definitions_request_builder

        return role_definitions_request_builder.RoleDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def transitive_role_assignments(self) -> transitive_role_assignments_request_builder.TransitiveRoleAssignmentsRequestBuilder:
        """
        Provides operations to manage the transitiveRoleAssignments property of the microsoft.graph.unifiedRbacApplication entity.
        """
        from .transitive_role_assignments import transitive_role_assignments_request_builder

        return transitive_role_assignments_request_builder.TransitiveRoleAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ExchangeRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ExchangeRequestBuilderGetQueryParameters():
        """
        Get exchange from roleManagement
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
    class ExchangeRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ExchangeRequestBuilder.ExchangeRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ExchangeRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
