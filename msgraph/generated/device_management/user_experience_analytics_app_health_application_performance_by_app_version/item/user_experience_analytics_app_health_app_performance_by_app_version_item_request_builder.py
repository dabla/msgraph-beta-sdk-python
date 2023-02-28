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

user_experience_analytics_app_health_app_performance_by_app_version = lazy_import('msgraph.generated.models.user_experience_analytics_app_health_app_performance_by_app_version')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionItemRequestBuilder():
    """
    Provides operations to manage the userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersion property of the microsoft.graph.deviceManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersion/{userExperienceAnalyticsAppHealthAppPerformanceByAppVersion%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersion for deviceManagement
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
    
    async def get(self,request_configuration: Optional[UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionItemRequestBuilderGetRequestConfiguration] = None) -> Optional[user_experience_analytics_app_health_app_performance_by_app_version.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion]:
        """
        User experience analytics appHealth Application Performance by App Version
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[user_experience_analytics_app_health_app_performance_by_app_version.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion]
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
        return await self.request_adapter.send_async(request_info, user_experience_analytics_app_health_app_performance_by_app_version.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion, error_mapping)
    
    async def patch(self,body: Optional[user_experience_analytics_app_health_app_performance_by_app_version.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion] = None, request_configuration: Optional[UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[user_experience_analytics_app_health_app_performance_by_app_version.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion]:
        """
        Update the navigation property userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersion in deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[user_experience_analytics_app_health_app_performance_by_app_version.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion]
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
        return await self.request_adapter.send_async(request_info, user_experience_analytics_app_health_app_performance_by_app_version.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersion for deviceManagement
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
    
    def to_get_request_information(self,request_configuration: Optional[UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        User experience analytics appHealth Application Performance by App Version
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
    
    def to_patch_request_information(self,body: Optional[user_experience_analytics_app_health_app_performance_by_app_version.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion] = None, request_configuration: Optional[UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersion in deviceManagement
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
    class UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionItemRequestBuilderGetQueryParameters():
        """
        User experience analytics appHealth Application Performance by App Version
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
    class UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionItemRequestBuilder.UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

