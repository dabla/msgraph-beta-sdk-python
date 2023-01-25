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

play_prompt_post_request_body = lazy_import('msgraph.generated.communications.calls.item.play_prompt.play_prompt_post_request_body')
play_prompt_operation = lazy_import('msgraph.generated.models.play_prompt_operation')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class PlayPromptRequestBuilder():
    """
    Provides operations to call the playPrompt method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new PlayPromptRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/communications/calls/{call%2Did}/microsoft.graph.playPrompt"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def post(self,body: Optional[play_prompt_post_request_body.PlayPromptPostRequestBody] = None, request_configuration: Optional[PlayPromptRequestBuilderPostRequestConfiguration] = None) -> Optional[play_prompt_operation.PlayPromptOperation]:
        """
        Play a prompt in the call. For more information about how to handle operations, see commsOperation
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[play_prompt_operation.PlayPromptOperation]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, play_prompt_operation.PlayPromptOperation, error_mapping)
    
    def to_post_request_information(self,body: Optional[play_prompt_post_request_body.PlayPromptPostRequestBody] = None, request_configuration: Optional[PlayPromptRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Play a prompt in the call. For more information about how to handle operations, see commsOperation
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
        request_info.http_method = Method.POST
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @dataclass
    class PlayPromptRequestBuilderPostRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

