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

printer_share = lazy_import('msgraph.generated.models.printer_share')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
allowed_groups_request_builder = lazy_import('msgraph.generated.print.printer_shares.item.allowed_groups.allowed_groups_request_builder')
group_item_request_builder = lazy_import('msgraph.generated.print.printer_shares.item.allowed_groups.item.group_item_request_builder')
allowed_users_request_builder = lazy_import('msgraph.generated.print.printer_shares.item.allowed_users.allowed_users_request_builder')
user_item_request_builder = lazy_import('msgraph.generated.print.printer_shares.item.allowed_users.item.user_item_request_builder')
printer_request_builder = lazy_import('msgraph.generated.print.printer_shares.item.printer.printer_request_builder')

class PrinterShareItemRequestBuilder():
    """
    Provides operations to manage the printerShares property of the microsoft.graph.print entity.
    """
    @property
    def allowed_groups(self) -> allowed_groups_request_builder.AllowedGroupsRequestBuilder:
        """
        Provides operations to manage the allowedGroups property of the microsoft.graph.printerShare entity.
        """
        return allowed_groups_request_builder.AllowedGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def allowed_users(self) -> allowed_users_request_builder.AllowedUsersRequestBuilder:
        """
        Provides operations to manage the allowedUsers property of the microsoft.graph.printerShare entity.
        """
        return allowed_users_request_builder.AllowedUsersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def printer(self) -> printer_request_builder.PrinterRequestBuilder:
        """
        Provides operations to manage the printer property of the microsoft.graph.printerShare entity.
        """
        return printer_request_builder.PrinterRequestBuilder(self.request_adapter, self.path_parameters)
    
    def allowed_groups_by_id(self,id: str) -> group_item_request_builder.GroupItemRequestBuilder:
        """
        Gets an item from the msgraph.generated.print.printerShares.item.allowedGroups.item collection
        Args:
            id: Unique identifier of the item
        Returns: group_item_request_builder.GroupItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["group%2Did"] = id
        return group_item_request_builder.GroupItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def allowed_users_by_id(self,id: str) -> user_item_request_builder.UserItemRequestBuilder:
        """
        Gets an item from the msgraph.generated.print.printerShares.item.allowedUsers.item collection
        Args:
            id: Unique identifier of the item
        Returns: user_item_request_builder.UserItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["user%2Did"] = id
        return user_item_request_builder.UserItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new PrinterShareItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/print/printerShares/{printerShare%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[PrinterShareItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property printerShares for print
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
    
    async def get(self,request_configuration: Optional[PrinterShareItemRequestBuilderGetRequestConfiguration] = None) -> Optional[printer_share.PrinterShare]:
        """
        Get printerShares from print
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[printer_share.PrinterShare]
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
        return await self.request_adapter.send_async(request_info, printer_share.PrinterShare, error_mapping)
    
    async def patch(self,body: Optional[printer_share.PrinterShare] = None, request_configuration: Optional[PrinterShareItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[printer_share.PrinterShare]:
        """
        Update the navigation property printerShares in print
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[printer_share.PrinterShare]
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
        return await self.request_adapter.send_async(request_info, printer_share.PrinterShare, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[PrinterShareItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property printerShares for print
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
    
    def to_get_request_information(self,request_configuration: Optional[PrinterShareItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get printerShares from print
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
    
    def to_patch_request_information(self,body: Optional[printer_share.PrinterShare] = None, request_configuration: Optional[PrinterShareItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property printerShares in print
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
    class PrinterShareItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class PrinterShareItemRequestBuilderGetQueryParameters():
        """
        Get printerShares from print
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
    class PrinterShareItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[PrinterShareItemRequestBuilder.PrinterShareItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class PrinterShareItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

