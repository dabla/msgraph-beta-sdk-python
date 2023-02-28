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

master_categories_request_builder = lazy_import('msgraph.generated.me.outlook.master_categories.master_categories_request_builder')
outlook_category_item_request_builder = lazy_import('msgraph.generated.me.outlook.master_categories.item.outlook_category_item_request_builder')
supported_languages_request_builder = lazy_import('msgraph.generated.me.outlook.supported_languages.supported_languages_request_builder')
supported_time_zones_request_builder = lazy_import('msgraph.generated.me.outlook.supported_time_zones.supported_time_zones_request_builder')
supported_time_zones_with_time_zone_standard_request_builder = lazy_import('msgraph.generated.me.outlook.supported_time_zones_with_time_zone_standard.supported_time_zones_with_time_zone_standard_request_builder')
task_folders_request_builder = lazy_import('msgraph.generated.me.outlook.task_folders.task_folders_request_builder')
outlook_task_folder_item_request_builder = lazy_import('msgraph.generated.me.outlook.task_folders.item.outlook_task_folder_item_request_builder')
task_groups_request_builder = lazy_import('msgraph.generated.me.outlook.task_groups.task_groups_request_builder')
outlook_task_group_item_request_builder = lazy_import('msgraph.generated.me.outlook.task_groups.item.outlook_task_group_item_request_builder')
tasks_request_builder = lazy_import('msgraph.generated.me.outlook.tasks.tasks_request_builder')
outlook_task_item_request_builder = lazy_import('msgraph.generated.me.outlook.tasks.item.outlook_task_item_request_builder')
outlook_user = lazy_import('msgraph.generated.models.outlook_user')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class OutlookRequestBuilder():
    """
    Provides operations to manage the outlook property of the microsoft.graph.user entity.
    """
    @property
    def master_categories(self) -> master_categories_request_builder.MasterCategoriesRequestBuilder:
        """
        Provides operations to manage the masterCategories property of the microsoft.graph.outlookUser entity.
        """
        return master_categories_request_builder.MasterCategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def supported_languages(self) -> supported_languages_request_builder.SupportedLanguagesRequestBuilder:
        """
        Provides operations to call the supportedLanguages method.
        """
        return supported_languages_request_builder.SupportedLanguagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def supported_time_zones(self) -> supported_time_zones_request_builder.SupportedTimeZonesRequestBuilder:
        """
        Provides operations to call the supportedTimeZones method.
        """
        return supported_time_zones_request_builder.SupportedTimeZonesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def task_folders(self) -> task_folders_request_builder.TaskFoldersRequestBuilder:
        """
        Provides operations to manage the taskFolders property of the microsoft.graph.outlookUser entity.
        """
        return task_folders_request_builder.TaskFoldersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def task_groups(self) -> task_groups_request_builder.TaskGroupsRequestBuilder:
        """
        Provides operations to manage the taskGroups property of the microsoft.graph.outlookUser entity.
        """
        return task_groups_request_builder.TaskGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tasks(self) -> tasks_request_builder.TasksRequestBuilder:
        """
        Provides operations to manage the tasks property of the microsoft.graph.outlookUser entity.
        """
        return tasks_request_builder.TasksRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new OutlookRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/me/outlook{?%24select}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def get(self,request_configuration: Optional[OutlookRequestBuilderGetRequestConfiguration] = None) -> Optional[outlook_user.OutlookUser]:
        """
        Selective Outlook services available to the user. Read-only. Nullable.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[outlook_user.OutlookUser]
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
        return await self.request_adapter.send_async(request_info, outlook_user.OutlookUser, error_mapping)
    
    def master_categories_by_id(self,id: str) -> outlook_category_item_request_builder.OutlookCategoryItemRequestBuilder:
        """
        Provides operations to manage the masterCategories property of the microsoft.graph.outlookUser entity.
        Args:
            id: Unique identifier of the item
        Returns: outlook_category_item_request_builder.OutlookCategoryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["outlookCategory%2Did"] = id
        return outlook_category_item_request_builder.OutlookCategoryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def supported_time_zones_with_time_zone_standard(self,time_zone_standard: Optional[str] = None) -> supported_time_zones_with_time_zone_standard_request_builder.SupportedTimeZonesWithTimeZoneStandardRequestBuilder:
        """
        Provides operations to call the supportedTimeZones method.
        Args:
            TimeZoneStandard: Usage: TimeZoneStandard='{TimeZoneStandard}'
        Returns: supported_time_zones_with_time_zone_standard_request_builder.SupportedTimeZonesWithTimeZoneStandardRequestBuilder
        """
        if time_zone_standard is None:
            raise Exception("time_zone_standard cannot be undefined")
        return supported_time_zones_with_time_zone_standard_request_builder.SupportedTimeZonesWithTimeZoneStandardRequestBuilder(self.request_adapter, self.path_parameters, TimeZoneStandard)
    
    def task_folders_by_id(self,id: str) -> outlook_task_folder_item_request_builder.OutlookTaskFolderItemRequestBuilder:
        """
        Provides operations to manage the taskFolders property of the microsoft.graph.outlookUser entity.
        Args:
            id: Unique identifier of the item
        Returns: outlook_task_folder_item_request_builder.OutlookTaskFolderItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["outlookTaskFolder%2Did"] = id
        return outlook_task_folder_item_request_builder.OutlookTaskFolderItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def task_groups_by_id(self,id: str) -> outlook_task_group_item_request_builder.OutlookTaskGroupItemRequestBuilder:
        """
        Provides operations to manage the taskGroups property of the microsoft.graph.outlookUser entity.
        Args:
            id: Unique identifier of the item
        Returns: outlook_task_group_item_request_builder.OutlookTaskGroupItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["outlookTaskGroup%2Did"] = id
        return outlook_task_group_item_request_builder.OutlookTaskGroupItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def tasks_by_id(self,id: str) -> outlook_task_item_request_builder.OutlookTaskItemRequestBuilder:
        """
        Provides operations to manage the tasks property of the microsoft.graph.outlookUser entity.
        Args:
            id: Unique identifier of the item
        Returns: outlook_task_item_request_builder.OutlookTaskItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["outlookTask%2Did"] = id
        return outlook_task_item_request_builder.OutlookTaskItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_get_request_information(self,request_configuration: Optional[OutlookRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Selective Outlook services available to the user. Read-only. Nullable.
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
    class OutlookRequestBuilderGetQueryParameters():
        """
        Selective Outlook services available to the user. Read-only. Nullable.
        """
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
            if original_name == "select":
                return "%24select"
            return original_name
        
    
    @dataclass
    class OutlookRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[OutlookRequestBuilder.OutlookRequestBuilderGetQueryParameters] = None

    

