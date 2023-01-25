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

group_collection_response = lazy_import('msgraph.generated.models.group_collection_response')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
delta_request_builder = lazy_import('msgraph.generated.users.item.joined_groups.delta.delta_request_builder')
evaluate_dynamic_membership_request_builder = lazy_import('msgraph.generated.users.item.joined_groups.evaluate_dynamic_membership.evaluate_dynamic_membership_request_builder')
get_by_ids_request_builder = lazy_import('msgraph.generated.users.item.joined_groups.get_by_ids.get_by_ids_request_builder')
get_user_owned_objects_request_builder = lazy_import('msgraph.generated.users.item.joined_groups.get_user_owned_objects.get_user_owned_objects_request_builder')
validate_properties_request_builder = lazy_import('msgraph.generated.users.item.joined_groups.validate_properties.validate_properties_request_builder')

class JoinedGroupsRequestBuilder():
    """
    Provides operations to manage the joinedGroups property of the microsoft.graph.user entity.
    """
    @property
    def evaluate_dynamic_membership(self) -> evaluate_dynamic_membership_request_builder.EvaluateDynamicMembershipRequestBuilder:
        """
        Provides operations to call the evaluateDynamicMembership method.
        """
        return evaluate_dynamic_membership_request_builder.EvaluateDynamicMembershipRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_by_ids(self) -> get_by_ids_request_builder.GetByIdsRequestBuilder:
        """
        Provides operations to call the getByIds method.
        """
        return get_by_ids_request_builder.GetByIdsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_user_owned_objects(self) -> get_user_owned_objects_request_builder.GetUserOwnedObjectsRequestBuilder:
        """
        Provides operations to call the getUserOwnedObjects method.
        """
        return get_user_owned_objects_request_builder.GetUserOwnedObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def validate_properties(self) -> validate_properties_request_builder.ValidatePropertiesRequestBuilder:
        """
        Provides operations to call the validateProperties method.
        """
        return validate_properties_request_builder.ValidatePropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new JoinedGroupsRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/users/{user%2Did}/joinedGroups{?%24top,%24skip,%24filter,%24count,%24orderby,%24select}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def delta(self,) -> delta_request_builder.DeltaRequestBuilder:
        """
        Provides operations to call the delta method.
        Returns: delta_request_builder.DeltaRequestBuilder
        """
        return delta_request_builder.DeltaRequestBuilder(self.request_adapter, self.path_parameters)
    
    async def get(self,request_configuration: Optional[JoinedGroupsRequestBuilderGetRequestConfiguration] = None) -> Optional[group_collection_response.GroupCollectionResponse]:
        """
        Get joinedGroups from users
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[group_collection_response.GroupCollectionResponse]
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
        return await self.request_adapter.send_async(request_info, group_collection_response.GroupCollectionResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[JoinedGroupsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get joinedGroups from users
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
    
    @dataclass
    class JoinedGroupsRequestBuilderGetQueryParameters():
        """
        Get joinedGroups from users
        """
        # Include count of items
        count: Optional[bool] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[List[str]] = None

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
            if original_name == "filter":
                return "%24filter"
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "select":
                return "%24select"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
    
    @dataclass
    class JoinedGroupsRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[JoinedGroupsRequestBuilder.JoinedGroupsRequestBuilderGetQueryParameters] = None

    

