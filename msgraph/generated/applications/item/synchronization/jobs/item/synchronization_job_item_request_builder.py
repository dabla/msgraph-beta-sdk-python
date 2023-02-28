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

pause_request_builder = lazy_import('msgraph.generated.applications.item.synchronization.jobs.item.pause.pause_request_builder')
provision_on_demand_request_builder = lazy_import('msgraph.generated.applications.item.synchronization.jobs.item.provision_on_demand.provision_on_demand_request_builder')
restart_request_builder = lazy_import('msgraph.generated.applications.item.synchronization.jobs.item.restart.restart_request_builder')
schema_request_builder = lazy_import('msgraph.generated.applications.item.synchronization.jobs.item.schema.schema_request_builder')
start_request_builder = lazy_import('msgraph.generated.applications.item.synchronization.jobs.item.start.start_request_builder')
stop_request_builder = lazy_import('msgraph.generated.applications.item.synchronization.jobs.item.stop.stop_request_builder')
validate_credentials_request_builder = lazy_import('msgraph.generated.applications.item.synchronization.jobs.item.validate_credentials.validate_credentials_request_builder')
synchronization_job = lazy_import('msgraph.generated.models.synchronization_job')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class SynchronizationJobItemRequestBuilder():
    """
    Provides operations to manage the jobs property of the microsoft.graph.synchronization entity.
    """
    @property
    def pause(self) -> pause_request_builder.PauseRequestBuilder:
        """
        Provides operations to call the pause method.
        """
        return pause_request_builder.PauseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def provision_on_demand(self) -> provision_on_demand_request_builder.ProvisionOnDemandRequestBuilder:
        """
        Provides operations to call the provisionOnDemand method.
        """
        return provision_on_demand_request_builder.ProvisionOnDemandRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restart(self) -> restart_request_builder.RestartRequestBuilder:
        """
        Provides operations to call the restart method.
        """
        return restart_request_builder.RestartRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def schema(self) -> schema_request_builder.SchemaRequestBuilder:
        """
        Provides operations to manage the schema property of the microsoft.graph.synchronizationJob entity.
        """
        return schema_request_builder.SchemaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def start(self) -> start_request_builder.StartRequestBuilder:
        """
        Provides operations to call the start method.
        """
        return start_request_builder.StartRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def stop(self) -> stop_request_builder.StopRequestBuilder:
        """
        Provides operations to call the stop method.
        """
        return stop_request_builder.StopRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def validate_credentials(self) -> validate_credentials_request_builder.ValidateCredentialsRequestBuilder:
        """
        Provides operations to call the validateCredentials method.
        """
        return validate_credentials_request_builder.ValidateCredentialsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new SynchronizationJobItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/applications/{application%2Did}/synchronization/jobs/{synchronizationJob%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[SynchronizationJobItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property jobs for applications
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
    
    async def get(self,request_configuration: Optional[SynchronizationJobItemRequestBuilderGetRequestConfiguration] = None) -> Optional[synchronization_job.SynchronizationJob]:
        """
        Performs synchronization by periodically running in the background, polling for changes in one directory, and pushing them to another directory.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[synchronization_job.SynchronizationJob]
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
        return await self.request_adapter.send_async(request_info, synchronization_job.SynchronizationJob, error_mapping)
    
    async def patch(self,body: Optional[synchronization_job.SynchronizationJob] = None, request_configuration: Optional[SynchronizationJobItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[synchronization_job.SynchronizationJob]:
        """
        Update the navigation property jobs in applications
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[synchronization_job.SynchronizationJob]
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
        return await self.request_adapter.send_async(request_info, synchronization_job.SynchronizationJob, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[SynchronizationJobItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property jobs for applications
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
    
    def to_get_request_information(self,request_configuration: Optional[SynchronizationJobItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Performs synchronization by periodically running in the background, polling for changes in one directory, and pushing them to another directory.
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
    
    def to_patch_request_information(self,body: Optional[synchronization_job.SynchronizationJob] = None, request_configuration: Optional[SynchronizationJobItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property jobs in applications
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
    class SynchronizationJobItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class SynchronizationJobItemRequestBuilderGetQueryParameters():
        """
        Performs synchronization by periodically running in the background, polling for changes in one directory, and pushing them to another directory.
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
    class SynchronizationJobItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[SynchronizationJobItemRequestBuilder.SynchronizationJobItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class SynchronizationJobItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

