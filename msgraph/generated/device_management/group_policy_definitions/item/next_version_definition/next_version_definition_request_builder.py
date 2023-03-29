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
    from .....models import group_policy_definition
    from .....models.o_data_errors import o_data_error
    from .category import category_request_builder
    from .definition_file import definition_file_request_builder
    from .presentations import presentations_request_builder
    from .presentations.item import group_policy_presentation_item_request_builder
    from .previous_version_definition import previous_version_definition_request_builder

class NextVersionDefinitionRequestBuilder():
    """
    Provides operations to manage the nextVersionDefinition property of the microsoft.graph.groupPolicyDefinition entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new NextVersionDefinitionRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/groupPolicyDefinitions/{groupPolicyDefinition%2Did}/nextVersionDefinition{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[NextVersionDefinitionRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property nextVersionDefinition for deviceManagement
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
    
    async def get(self,request_configuration: Optional[NextVersionDefinitionRequestBuilderGetRequestConfiguration] = None) -> Optional[group_policy_definition.GroupPolicyDefinition]:
        """
        Definition of the next version of this definition
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[group_policy_definition.GroupPolicyDefinition]
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
        from .....models import group_policy_definition

        return await self.request_adapter.send_async(request_info, group_policy_definition.GroupPolicyDefinition, error_mapping)
    
    async def patch(self,body: Optional[group_policy_definition.GroupPolicyDefinition] = None, request_configuration: Optional[NextVersionDefinitionRequestBuilderPatchRequestConfiguration] = None) -> Optional[group_policy_definition.GroupPolicyDefinition]:
        """
        Update the navigation property nextVersionDefinition in deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[group_policy_definition.GroupPolicyDefinition]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models import group_policy_definition

        return await self.request_adapter.send_async(request_info, group_policy_definition.GroupPolicyDefinition, error_mapping)
    
    def presentations_by_id(self,id: str) -> group_policy_presentation_item_request_builder.GroupPolicyPresentationItemRequestBuilder:
        """
        Provides operations to manage the presentations property of the microsoft.graph.groupPolicyDefinition entity.
        Args:
            id: Unique identifier of the item
        Returns: group_policy_presentation_item_request_builder.GroupPolicyPresentationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .presentations.item import group_policy_presentation_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["groupPolicyPresentation%2Did"] = id
        return group_policy_presentation_item_request_builder.GroupPolicyPresentationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[NextVersionDefinitionRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property nextVersionDefinition for deviceManagement
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
    
    def to_get_request_information(self,request_configuration: Optional[NextVersionDefinitionRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Definition of the next version of this definition
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
    
    def to_patch_request_information(self,body: Optional[group_policy_definition.GroupPolicyDefinition] = None, request_configuration: Optional[NextVersionDefinitionRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property nextVersionDefinition in deviceManagement
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
    
    @property
    def category(self) -> category_request_builder.CategoryRequestBuilder:
        """
        Provides operations to manage the category property of the microsoft.graph.groupPolicyDefinition entity.
        """
        from .category import category_request_builder

        return category_request_builder.CategoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def definition_file(self) -> definition_file_request_builder.DefinitionFileRequestBuilder:
        """
        Provides operations to manage the definitionFile property of the microsoft.graph.groupPolicyDefinition entity.
        """
        from .definition_file import definition_file_request_builder

        return definition_file_request_builder.DefinitionFileRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def presentations(self) -> presentations_request_builder.PresentationsRequestBuilder:
        """
        Provides operations to manage the presentations property of the microsoft.graph.groupPolicyDefinition entity.
        """
        from .presentations import presentations_request_builder

        return presentations_request_builder.PresentationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def previous_version_definition(self) -> previous_version_definition_request_builder.PreviousVersionDefinitionRequestBuilder:
        """
        Provides operations to manage the previousVersionDefinition property of the microsoft.graph.groupPolicyDefinition entity.
        """
        from .previous_version_definition import previous_version_definition_request_builder

        return previous_version_definition_request_builder.PreviousVersionDefinitionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class NextVersionDefinitionRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class NextVersionDefinitionRequestBuilderGetQueryParameters():
        """
        Definition of the next version of this definition
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
    class NextVersionDefinitionRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[NextVersionDefinitionRequestBuilder.NextVersionDefinitionRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class NextVersionDefinitionRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

