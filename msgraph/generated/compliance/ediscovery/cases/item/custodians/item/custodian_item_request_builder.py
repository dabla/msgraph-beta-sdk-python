from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, Union

from .......models.ediscovery import custodian
from .......models.o_data_errors import o_data_error
from .activate import activate_request_builder
from .apply_hold import apply_hold_request_builder
from .release import release_request_builder
from .remove_hold import remove_hold_request_builder
from .site_sources import site_sources_request_builder
from .site_sources.item import site_source_item_request_builder
from .unified_group_sources import unified_group_sources_request_builder
from .unified_group_sources.item import unified_group_source_item_request_builder
from .update_index import update_index_request_builder
from .user_sources import user_sources_request_builder
from .user_sources.item import user_source_item_request_builder

class CustodianItemRequestBuilder():
    """
    Provides operations to manage the custodians property of the microsoft.graph.ediscovery.case entity.
    """
    def activate(self) -> activate_request_builder.ActivateRequestBuilder:
        """
        Provides operations to call the activate method.
        """
        return activate_request_builder.ActivateRequestBuilder(self.request_adapter, self.path_parameters)
    
    def apply_hold(self) -> apply_hold_request_builder.ApplyHoldRequestBuilder:
        """
        Provides operations to call the applyHold method.
        """
        return apply_hold_request_builder.ApplyHoldRequestBuilder(self.request_adapter, self.path_parameters)
    
    def release(self) -> release_request_builder.ReleaseRequestBuilder:
        """
        Provides operations to call the release method.
        """
        return release_request_builder.ReleaseRequestBuilder(self.request_adapter, self.path_parameters)
    
    def remove_hold(self) -> remove_hold_request_builder.RemoveHoldRequestBuilder:
        """
        Provides operations to call the removeHold method.
        """
        return remove_hold_request_builder.RemoveHoldRequestBuilder(self.request_adapter, self.path_parameters)
    
    def site_sources(self) -> site_sources_request_builder.SiteSourcesRequestBuilder:
        """
        Provides operations to manage the siteSources property of the microsoft.graph.ediscovery.custodian entity.
        """
        return site_sources_request_builder.SiteSourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def unified_group_sources(self) -> unified_group_sources_request_builder.UnifiedGroupSourcesRequestBuilder:
        """
        Provides operations to manage the unifiedGroupSources property of the microsoft.graph.ediscovery.custodian entity.
        """
        return unified_group_sources_request_builder.UnifiedGroupSourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def update_index(self) -> update_index_request_builder.UpdateIndexRequestBuilder:
        """
        Provides operations to call the updateIndex method.
        """
        return update_index_request_builder.UpdateIndexRequestBuilder(self.request_adapter, self.path_parameters)
    
    def user_sources(self) -> user_sources_request_builder.UserSourcesRequestBuilder:
        """
        Provides operations to manage the userSources property of the microsoft.graph.ediscovery.custodian entity.
        """
        return user_sources_request_builder.UserSourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new CustodianItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/compliance/ediscovery/cases/{case%2Did}/custodians/{custodian%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[CustodianItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property custodians for compliance
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
    
    def create_get_request_information(self,request_configuration: Optional[CustodianItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Returns a list of case custodian objects for this case.  Nullable.
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
    
    def create_patch_request_information(self,body: Optional[custodian.Custodian] = None, request_configuration: Optional[CustodianItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property custodians in compliance
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
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    async def delete(self,request_configuration: Optional[CustodianItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property custodians for compliance
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        """
        request_info = self.create_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, response_handler, error_mapping)
    
    async def get(self,request_configuration: Optional[CustodianItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[custodian.Custodian]:
        """
        Returns a list of case custodian objects for this case.  Nullable.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[custodian.Custodian]
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
        return await self.request_adapter.send_async(request_info, custodian.Custodian, response_handler, error_mapping)
    
    async def patch(self,body: Optional[custodian.Custodian] = None, request_configuration: Optional[CustodianItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[custodian.Custodian]:
        """
        Update the navigation property custodians in compliance
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[custodian.Custodian]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, custodian.Custodian, response_handler, error_mapping)
    
    def site_sources_by_id(self,id: str) -> site_source_item_request_builder.SiteSourceItemRequestBuilder:
        """
        Provides operations to manage the siteSources property of the microsoft.graph.ediscovery.custodian entity.
        Args:
            id: Unique identifier of the item
        Returns: site_source_item_request_builder.SiteSourceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["siteSource%2Did"] = id
        return site_source_item_request_builder.SiteSourceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def unified_group_sources_by_id(self,id: str) -> unified_group_source_item_request_builder.UnifiedGroupSourceItemRequestBuilder:
        """
        Provides operations to manage the unifiedGroupSources property of the microsoft.graph.ediscovery.custodian entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_group_source_item_request_builder.UnifiedGroupSourceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedGroupSource%2Did"] = id
        return unified_group_source_item_request_builder.UnifiedGroupSourceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_sources_by_id(self,id: str) -> user_source_item_request_builder.UserSourceItemRequestBuilder:
        """
        Provides operations to manage the userSources property of the microsoft.graph.ediscovery.custodian entity.
        Args:
            id: Unique identifier of the item
        Returns: user_source_item_request_builder.UserSourceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userSource%2Did"] = id
        return user_source_item_request_builder.UserSourceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class CustodianItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class CustodianItemRequestBuilderGetQueryParameters():
        """
        Returns a list of case custodian objects for this case.  Nullable.
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
    class CustodianItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[CustodianItemRequestBuilder.CustodianItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class CustodianItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
