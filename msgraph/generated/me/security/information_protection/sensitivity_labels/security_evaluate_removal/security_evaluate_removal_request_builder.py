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
    from . import evaluate_removal_post_request_body, evaluate_removal_response
    from ......models.o_data_errors import o_data_error

class SecurityEvaluateRemovalRequestBuilder():
    """
    Provides operations to call the evaluateRemoval method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new SecurityEvaluateRemovalRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/me/security/informationProtection/sensitivityLabels/security.evaluateRemoval"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def post(self,body: Optional[evaluate_removal_post_request_body.EvaluateRemovalPostRequestBody] = None, request_configuration: Optional[SecurityEvaluateRemovalRequestBuilderPostRequestConfiguration] = None) -> Optional[evaluate_removal_response.EvaluateRemovalResponse]:
        """
        Indicate to the consuming application what actions it should take to remove the label information. Given contentInfo as an input, which includes existing content metadata key-value pairs, the API returns an informationProtectionAction that contains some combination of one or more of the following: 
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[evaluate_removal_response.EvaluateRemovalResponse]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from . import evaluate_removal_response

        return await self.request_adapter.send_async(request_info, evaluate_removal_response.EvaluateRemovalResponse, error_mapping)
    
    def to_post_request_information(self,body: Optional[evaluate_removal_post_request_body.EvaluateRemovalPostRequestBody] = None, request_configuration: Optional[SecurityEvaluateRemovalRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Indicate to the consuming application what actions it should take to remove the label information. Given contentInfo as an input, which includes existing content metadata key-value pairs, the API returns an informationProtectionAction that contains some combination of one or more of the following: 
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
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @dataclass
    class SecurityEvaluateRemovalRequestBuilderPostRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
