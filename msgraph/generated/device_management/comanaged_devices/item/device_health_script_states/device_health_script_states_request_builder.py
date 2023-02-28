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

count_request_builder = lazy_import('msgraph.generated.device_management.comanaged_devices.item.device_health_script_states.count.count_request_builder')
with_id_with_policy_id_with_device_id_request_builder = lazy_import('msgraph.generated.device_management.comanaged_devices.item.device_health_script_states.with_id_with_policy_id_with_device_id.with_id_with_policy_id_with_device_id_request_builder')
device_health_script_policy_state_collection_response = lazy_import('msgraph.generated.models.device_health_script_policy_state_collection_response')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class DeviceHealthScriptStatesRequestBuilder():
    """
    Provides operations to manage the deviceHealthScriptStates property of the microsoft.graph.managedDevice entity.
    """
    @property
    def count(self) -> count_request_builder.CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        return count_request_builder.CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DeviceHealthScriptStatesRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/comanagedDevices/{managedDevice%2Did}/deviceHealthScriptStates{?%24top,%24skip,%24search,%24filter,%24count,%24orderby,%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def get(self,request_configuration: Optional[DeviceHealthScriptStatesRequestBuilderGetRequestConfiguration] = None) -> Optional[device_health_script_policy_state_collection_response.DeviceHealthScriptPolicyStateCollectionResponse]:
        """
        Results of device health scripts that ran for this device. Default is empty list. This property is read-only.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[device_health_script_policy_state_collection_response.DeviceHealthScriptPolicyStateCollectionResponse]
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
        return await self.request_adapter.send_async(request_info, device_health_script_policy_state_collection_response.DeviceHealthScriptPolicyStateCollectionResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[DeviceHealthScriptStatesRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Results of device health scripts that ran for this device. Default is empty list. This property is read-only.
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
    
    def with_id_with_policy_id_with_device_id(self,device_id: Optional[str] = None, id: Optional[str] = None, policy_id: Optional[str] = None) -> with_id_with_policy_id_with_device_id_request_builder.WithIdWithPolicyIdWithDeviceIdRequestBuilder:
        """
        Provides operations to manage the deviceHealthScriptStates property of the microsoft.graph.managedDevice entity.
        Args:
            deviceId: Property in multi-part unique identifier of deviceHealthScriptPolicyState
            id: Property in multi-part unique identifier of deviceHealthScriptPolicyState
            policyId: Property in multi-part unique identifier of deviceHealthScriptPolicyState
        Returns: with_id_with_policy_id_with_device_id_request_builder.WithIdWithPolicyIdWithDeviceIdRequestBuilder
        """
        if device_id is None:
            raise Exception("device_id cannot be undefined")
        if id is None:
            raise Exception("id cannot be undefined")
        if policy_id is None:
            raise Exception("policy_id cannot be undefined")
        return with_id_with_policy_id_with_device_id_request_builder.WithIdWithPolicyIdWithDeviceIdRequestBuilder(self.request_adapter, self.path_parameters, deviceId, id, policyId)
    
    @dataclass
    class DeviceHealthScriptStatesRequestBuilderGetQueryParameters():
        """
        Results of device health scripts that ran for this device. Default is empty list. This property is read-only.
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
    class DeviceHealthScriptStatesRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[DeviceHealthScriptStatesRequestBuilder.DeviceHealthScriptStatesRequestBuilderGetQueryParameters] = None

    

