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

app_diagnostics_with_upn_response = lazy_import('msgraph.generated.device_management.managed_devices.app_diagnostics_with_upn.app_diagnostics_with_upn_response')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class AppDiagnosticsWithUpnRequestBuilder():
    """
    Provides operations to call the appDiagnostics method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None, upn: Optional[str] = None) -> None:
        """
        Instantiates a new AppDiagnosticsWithUpnRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
            upn: Usage: upn='{upn}'
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/managedDevices/appDiagnostics(upn='{upn}'){?%24top,%24skip,%24search,%24filter,%24count}"

        url_tpl_params = get_path_parameters(path_parameters)
        url_tpl_params[""] = upn
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def get(self,request_configuration: Optional[AppDiagnosticsWithUpnRequestBuilderGetRequestConfiguration] = None) -> Optional[app_diagnostics_with_upn_response.AppDiagnosticsWithUpnResponse]:
        """
        Invoke function appDiagnostics
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[app_diagnostics_with_upn_response.AppDiagnosticsWithUpnResponse]
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
        return await self.request_adapter.send_async(request_info, app_diagnostics_with_upn_response.AppDiagnosticsWithUpnResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[AppDiagnosticsWithUpnRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Invoke function appDiagnostics
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
    
    @dataclass
    class AppDiagnosticsWithUpnRequestBuilderGetQueryParameters():
        """
        Invoke function appDiagnostics
        """
        # Include count of items
        count: Optional[bool] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Search items by search phrases
        search: Optional[str] = None

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
            if original_name == "search":
                return "%24search"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
    
    @dataclass
    class AppDiagnosticsWithUpnRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[AppDiagnosticsWithUpnRequestBuilder.AppDiagnosticsWithUpnRequestBuilderGetQueryParameters] = None

    

