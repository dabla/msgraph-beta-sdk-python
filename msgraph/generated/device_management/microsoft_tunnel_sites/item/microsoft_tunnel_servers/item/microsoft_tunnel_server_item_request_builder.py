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
    from ......models import microsoft_tunnel_server
    from ......models.o_data_errors import o_data_error
    from .create_server_log_collection_request import create_server_log_collection_request_request_builder
    from .generate_server_log_collection_request import generate_server_log_collection_request_request_builder
    from .get_health_metrics import get_health_metrics_request_builder
    from .get_health_metric_time_series import get_health_metric_time_series_request_builder

class MicrosoftTunnelServerItemRequestBuilder():
    """
    Provides operations to manage the microsoftTunnelServers property of the microsoft.graph.microsoftTunnelSite entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new MicrosoftTunnelServerItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/microsoftTunnelSites/{microsoftTunnelSite%2Did}/microsoftTunnelServers/{microsoftTunnelServer%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[MicrosoftTunnelServerItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property microsoftTunnelServers for deviceManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[MicrosoftTunnelServerItemRequestBuilderGetRequestConfiguration] = None) -> Optional[microsoft_tunnel_server.MicrosoftTunnelServer]:
        """
        A list of MicrosoftTunnelServers that are registered to this MicrosoftTunnelSite
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[microsoft_tunnel_server.MicrosoftTunnelServer]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models import microsoft_tunnel_server

        return await self.request_adapter.send_async(request_info, microsoft_tunnel_server.MicrosoftTunnelServer, error_mapping)
    
    async def patch(self,body: Optional[microsoft_tunnel_server.MicrosoftTunnelServer] = None, request_configuration: Optional[MicrosoftTunnelServerItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[microsoft_tunnel_server.MicrosoftTunnelServer]:
        """
        Update the navigation property microsoftTunnelServers in deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[microsoft_tunnel_server.MicrosoftTunnelServer]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models import microsoft_tunnel_server

        return await self.request_adapter.send_async(request_info, microsoft_tunnel_server.MicrosoftTunnelServer, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[MicrosoftTunnelServerItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property microsoftTunnelServers for deviceManagement
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
    
    def to_get_request_information(self,request_configuration: Optional[MicrosoftTunnelServerItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        A list of MicrosoftTunnelServers that are registered to this MicrosoftTunnelSite
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
    
    def to_patch_request_information(self,body: Optional[microsoft_tunnel_server.MicrosoftTunnelServer] = None, request_configuration: Optional[MicrosoftTunnelServerItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property microsoftTunnelServers in deviceManagement
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
    def create_server_log_collection_request(self) -> create_server_log_collection_request_request_builder.CreateServerLogCollectionRequestRequestBuilder:
        """
        Provides operations to call the createServerLogCollectionRequest method.
        """
        from .create_server_log_collection_request import create_server_log_collection_request_request_builder

        return create_server_log_collection_request_request_builder.CreateServerLogCollectionRequestRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def generate_server_log_collection_request(self) -> generate_server_log_collection_request_request_builder.GenerateServerLogCollectionRequestRequestBuilder:
        """
        Provides operations to call the generateServerLogCollectionRequest method.
        """
        from .generate_server_log_collection_request import generate_server_log_collection_request_request_builder

        return generate_server_log_collection_request_request_builder.GenerateServerLogCollectionRequestRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_health_metrics(self) -> get_health_metrics_request_builder.GetHealthMetricsRequestBuilder:
        """
        Provides operations to call the getHealthMetrics method.
        """
        from .get_health_metrics import get_health_metrics_request_builder

        return get_health_metrics_request_builder.GetHealthMetricsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_health_metric_time_series(self) -> get_health_metric_time_series_request_builder.GetHealthMetricTimeSeriesRequestBuilder:
        """
        Provides operations to call the getHealthMetricTimeSeries method.
        """
        from .get_health_metric_time_series import get_health_metric_time_series_request_builder

        return get_health_metric_time_series_request_builder.GetHealthMetricTimeSeriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class MicrosoftTunnelServerItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class MicrosoftTunnelServerItemRequestBuilderGetQueryParameters():
        """
        A list of MicrosoftTunnelServers that are registered to this MicrosoftTunnelSite
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
    class MicrosoftTunnelServerItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[MicrosoftTunnelServerItemRequestBuilder.MicrosoftTunnelServerItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class MicrosoftTunnelServerItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

