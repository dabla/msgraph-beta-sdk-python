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

count_request_builder = lazy_import('msgraph.generated.directory_setting_templates.count.count_request_builder')
get_by_ids_request_builder = lazy_import('msgraph.generated.directory_setting_templates.get_by_ids.get_by_ids_request_builder')
get_user_owned_objects_request_builder = lazy_import('msgraph.generated.directory_setting_templates.get_user_owned_objects.get_user_owned_objects_request_builder')
validate_properties_request_builder = lazy_import('msgraph.generated.directory_setting_templates.validate_properties.validate_properties_request_builder')
directory_setting_template = lazy_import('msgraph.generated.models.directory_setting_template')
directory_setting_template_collection_response = lazy_import('msgraph.generated.models.directory_setting_template_collection_response')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class DirectorySettingTemplatesRequestBuilder():
    """
    Provides operations to manage the collection of directorySettingTemplate entities.
    """
    def count(self) -> count_request_builder.CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        return count_request_builder.CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_by_ids(self) -> get_by_ids_request_builder.GetByIdsRequestBuilder:
        """
        Provides operations to call the getByIds method.
        """
        return get_by_ids_request_builder.GetByIdsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_user_owned_objects(self) -> get_user_owned_objects_request_builder.GetUserOwnedObjectsRequestBuilder:
        """
        Provides operations to call the getUserOwnedObjects method.
        """
        return get_user_owned_objects_request_builder.GetUserOwnedObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def validate_properties(self) -> validate_properties_request_builder.ValidatePropertiesRequestBuilder:
        """
        Provides operations to call the validateProperties method.
        """
        return validate_properties_request_builder.ValidatePropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DirectorySettingTemplatesRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/directorySettingTemplates{?%24top,%24skip,%24search,%24filter,%24count,%24orderby,%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_get_request_information(self,request_configuration: Optional[DirectorySettingTemplatesRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Directory setting templates represents a set of templates of directory settings, from which directory settings may be created and used within a tenant.  This operation retrieves the list of available **directorySettingTemplates** objects.
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
    
    def create_post_request_information(self,body: Optional[directory_setting_template.DirectorySettingTemplate] = None, request_configuration: Optional[DirectorySettingTemplatesRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Add new entity to directorySettingTemplates
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.POST
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    async def get(self,request_configuration: Optional[DirectorySettingTemplatesRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[directory_setting_template_collection_response.DirectorySettingTemplateCollectionResponse]:
        """
        Directory setting templates represents a set of templates of directory settings, from which directory settings may be created and used within a tenant.  This operation retrieves the list of available **directorySettingTemplates** objects.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[directory_setting_template_collection_response.DirectorySettingTemplateCollectionResponse]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, directory_setting_template_collection_response.DirectorySettingTemplateCollectionResponse, response_handler, error_mapping)
    
    async def post(self,body: Optional[directory_setting_template.DirectorySettingTemplate] = None, request_configuration: Optional[DirectorySettingTemplatesRequestBuilderPostRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[directory_setting_template.DirectorySettingTemplate]:
        """
        Add new entity to directorySettingTemplates
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[directory_setting_template.DirectorySettingTemplate]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_post_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, directory_setting_template.DirectorySettingTemplate, response_handler, error_mapping)
    
    @dataclass
    class DirectorySettingTemplatesRequestBuilderGetQueryParameters():
        """
        Directory setting templates represents a set of templates of directory settings, from which directory settings may be created and used within a tenant.  This operation retrieves the list of available **directorySettingTemplates** objects.
        """
        # Include count of items
        count: Optional[bool] = None

        # Expand related entities
        expand: Optional[List[str]] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[List[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "count":
                return "%24count"
            if original_name == "expand":
                return "%24expand"
            if original_name == "filter":
                return "%24filter"
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "search":
                return "%24search"
            if original_name == "select":
                return "%24select"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
    
    @dataclass
    class DirectorySettingTemplatesRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[DirectorySettingTemplatesRequestBuilder.DirectorySettingTemplatesRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class DirectorySettingTemplatesRequestBuilderPostRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

