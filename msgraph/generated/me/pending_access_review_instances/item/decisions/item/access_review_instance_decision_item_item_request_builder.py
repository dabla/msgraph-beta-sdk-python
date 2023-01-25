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

insights_request_builder = lazy_import('msgraph.generated.me.pending_access_review_instances.item.decisions.item.insights.insights_request_builder')
governance_insight_item_request_builder = lazy_import('msgraph.generated.me.pending_access_review_instances.item.decisions.item.insights.item.governance_insight_item_request_builder')
instance_request_builder = lazy_import('msgraph.generated.me.pending_access_review_instances.item.decisions.item.instance.instance_request_builder')
access_review_instance_decision_item = lazy_import('msgraph.generated.models.access_review_instance_decision_item')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class AccessReviewInstanceDecisionItemItemRequestBuilder():
    """
    Provides operations to manage the decisions property of the microsoft.graph.accessReviewInstance entity.
    """
    @property
    def insights(self) -> insights_request_builder.InsightsRequestBuilder:
        """
        Provides operations to manage the insights property of the microsoft.graph.accessReviewInstanceDecisionItem entity.
        """
        return insights_request_builder.InsightsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def instance(self) -> instance_request_builder.InstanceRequestBuilder:
        """
        Provides operations to manage the instance property of the microsoft.graph.accessReviewInstanceDecisionItem entity.
        """
        return instance_request_builder.InstanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AccessReviewInstanceDecisionItemItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/me/pendingAccessReviewInstances/{accessReviewInstance%2Did}/decisions/{accessReviewInstanceDecisionItem%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[AccessReviewInstanceDecisionItemItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property decisions for me
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
    
    async def get(self,request_configuration: Optional[AccessReviewInstanceDecisionItemItemRequestBuilderGetRequestConfiguration] = None) -> Optional[access_review_instance_decision_item.AccessReviewInstanceDecisionItem]:
        """
        Each user reviewed in an accessReviewInstance has a decision item representing if they were approved, denied, or not yet reviewed.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[access_review_instance_decision_item.AccessReviewInstanceDecisionItem]
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
        return await self.request_adapter.send_async(request_info, access_review_instance_decision_item.AccessReviewInstanceDecisionItem, error_mapping)
    
    def insights_by_id(self,id: str) -> governance_insight_item_request_builder.GovernanceInsightItemRequestBuilder:
        """
        Provides operations to manage the insights property of the microsoft.graph.accessReviewInstanceDecisionItem entity.
        Args:
            id: Unique identifier of the item
        Returns: governance_insight_item_request_builder.GovernanceInsightItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["governanceInsight%2Did"] = id
        return governance_insight_item_request_builder.GovernanceInsightItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[access_review_instance_decision_item.AccessReviewInstanceDecisionItem] = None, request_configuration: Optional[AccessReviewInstanceDecisionItemItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[access_review_instance_decision_item.AccessReviewInstanceDecisionItem]:
        """
        Update the navigation property decisions in me
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[access_review_instance_decision_item.AccessReviewInstanceDecisionItem]
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
        return await self.request_adapter.send_async(request_info, access_review_instance_decision_item.AccessReviewInstanceDecisionItem, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[AccessReviewInstanceDecisionItemItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property decisions for me
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
    
    def to_get_request_information(self,request_configuration: Optional[AccessReviewInstanceDecisionItemItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Each user reviewed in an accessReviewInstance has a decision item representing if they were approved, denied, or not yet reviewed.
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
    
    def to_patch_request_information(self,body: Optional[access_review_instance_decision_item.AccessReviewInstanceDecisionItem] = None, request_configuration: Optional[AccessReviewInstanceDecisionItemItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property decisions in me
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
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @dataclass
    class AccessReviewInstanceDecisionItemItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class AccessReviewInstanceDecisionItemItemRequestBuilderGetQueryParameters():
        """
        Each user reviewed in an accessReviewInstance has a decision item representing if they were approved, denied, or not yet reviewed.
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
    class AccessReviewInstanceDecisionItemItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[AccessReviewInstanceDecisionItemItemRequestBuilder.AccessReviewInstanceDecisionItemItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class AccessReviewInstanceDecisionItemItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

