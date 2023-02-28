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

recommended_settings_request_builder = lazy_import('msgraph.generated.device_management.templates.item.migratable_to.item.categories.item.recommended_settings.recommended_settings_request_builder')
device_management_setting_instance_item_request_builder = lazy_import('msgraph.generated.device_management.templates.item.migratable_to.item.categories.item.recommended_settings.item.device_management_setting_instance_item_request_builder')
device_management_template_setting_category = lazy_import('msgraph.generated.models.device_management_template_setting_category')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class DeviceManagementTemplateSettingCategoryItemRequestBuilder():
    """
    Provides operations to manage the categories property of the microsoft.graph.deviceManagementTemplate entity.
    """
    @property
    def recommended_settings(self) -> recommended_settings_request_builder.RecommendedSettingsRequestBuilder:
        """
        Provides operations to manage the recommendedSettings property of the microsoft.graph.deviceManagementTemplateSettingCategory entity.
        """
        return recommended_settings_request_builder.RecommendedSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DeviceManagementTemplateSettingCategoryItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/templates/{deviceManagementTemplate%2Did}/migratableTo/{deviceManagementTemplate%2Did1}/categories/{deviceManagementTemplateSettingCategory%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[DeviceManagementTemplateSettingCategoryItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property categories for deviceManagement
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
    
    async def get(self,request_configuration: Optional[DeviceManagementTemplateSettingCategoryItemRequestBuilderGetRequestConfiguration] = None) -> Optional[device_management_template_setting_category.DeviceManagementTemplateSettingCategory]:
        """
        Collection of setting categories within the template
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[device_management_template_setting_category.DeviceManagementTemplateSettingCategory]
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
        return await self.request_adapter.send_async(request_info, device_management_template_setting_category.DeviceManagementTemplateSettingCategory, error_mapping)
    
    async def patch(self,body: Optional[device_management_template_setting_category.DeviceManagementTemplateSettingCategory] = None, request_configuration: Optional[DeviceManagementTemplateSettingCategoryItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[device_management_template_setting_category.DeviceManagementTemplateSettingCategory]:
        """
        Update the navigation property categories in deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[device_management_template_setting_category.DeviceManagementTemplateSettingCategory]
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
        return await self.request_adapter.send_async(request_info, device_management_template_setting_category.DeviceManagementTemplateSettingCategory, error_mapping)
    
    def recommended_settings_by_id(self,id: str) -> device_management_setting_instance_item_request_builder.DeviceManagementSettingInstanceItemRequestBuilder:
        """
        Provides operations to manage the recommendedSettings property of the microsoft.graph.deviceManagementTemplateSettingCategory entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_setting_instance_item_request_builder.DeviceManagementSettingInstanceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementSettingInstance%2Did"] = id
        return device_management_setting_instance_item_request_builder.DeviceManagementSettingInstanceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[DeviceManagementTemplateSettingCategoryItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property categories for deviceManagement
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
    
    def to_get_request_information(self,request_configuration: Optional[DeviceManagementTemplateSettingCategoryItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Collection of setting categories within the template
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
    
    def to_patch_request_information(self,body: Optional[device_management_template_setting_category.DeviceManagementTemplateSettingCategory] = None, request_configuration: Optional[DeviceManagementTemplateSettingCategoryItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property categories in deviceManagement
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
    class DeviceManagementTemplateSettingCategoryItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class DeviceManagementTemplateSettingCategoryItemRequestBuilderGetQueryParameters():
        """
        Collection of setting categories within the template
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
    class DeviceManagementTemplateSettingCategoryItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[DeviceManagementTemplateSettingCategoryItemRequestBuilder.DeviceManagementTemplateSettingCategoryItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class DeviceManagementTemplateSettingCategoryItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

