from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .......models.education_module import EducationModule
    from .......models.o_data_errors.o_data_error import ODataError

class PinRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the pin method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new PinRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/education/classes/{educationClass%2Did}/modules/{educationModule%2Did}/pin", path_parameters)
    
    async def post(self,request_configuration: Optional[PinRequestBuilderPostRequestConfiguration] = None) -> Optional[EducationModule]:
        """
        Pin an educationModule in the classwork list. This action sets the isPinned property to true for an educationModule. Only teachers can perform this action and only one module at a time can be pinned in the classwork list.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EducationModule]
        Find more info here: https://learn.microsoft.com/graph/api/educationmodule-pin?view=graph-rest-1.0
        """
        request_info = self.to_post_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.education_module import EducationModule

        return await self.request_adapter.send_async(request_info, EducationModule, error_mapping)
    
    def to_post_request_information(self,request_configuration: Optional[PinRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Pin an educationModule in the classwork list. This action sets the isPinned property to true for an educationModule. Only teachers can perform this action and only one module at a time can be pinned in the classwork list.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.POST
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> PinRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PinRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return PinRequestBuilder(raw_url, self.request_adapter)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class PinRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
