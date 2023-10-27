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
    from ....models.call import Call
    from ....models.o_data_errors.o_data_error import ODataError
    from .add_large_gallery_view.add_large_gallery_view_request_builder import AddLargeGalleryViewRequestBuilder
    from .answer.answer_request_builder import AnswerRequestBuilder
    from .audio_routing_groups.audio_routing_groups_request_builder import AudioRoutingGroupsRequestBuilder
    from .cancel_media_processing.cancel_media_processing_request_builder import CancelMediaProcessingRequestBuilder
    from .change_screen_sharing_role.change_screen_sharing_role_request_builder import ChangeScreenSharingRoleRequestBuilder
    from .content_sharing_sessions.content_sharing_sessions_request_builder import ContentSharingSessionsRequestBuilder
    from .keep_alive.keep_alive_request_builder import KeepAliveRequestBuilder
    from .mute.mute_request_builder import MuteRequestBuilder
    from .operations.operations_request_builder import OperationsRequestBuilder
    from .participants.participants_request_builder import ParticipantsRequestBuilder
    from .play_prompt.play_prompt_request_builder import PlayPromptRequestBuilder
    from .record.record_request_builder import RecordRequestBuilder
    from .record_response.record_response_request_builder import RecordResponseRequestBuilder
    from .redirect.redirect_request_builder import RedirectRequestBuilder
    from .reject.reject_request_builder import RejectRequestBuilder
    from .subscribe_to_tone.subscribe_to_tone_request_builder import SubscribeToToneRequestBuilder
    from .transfer.transfer_request_builder import TransferRequestBuilder
    from .unmute.unmute_request_builder import UnmuteRequestBuilder
    from .update_recording_status.update_recording_status_request_builder import UpdateRecordingStatusRequestBuilder

class CallItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the calls property of the microsoft.graph.cloudCommunications entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new CallItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/communications/calls/{call%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[CallItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete or hang up an active call. For group calls, this will only delete your call leg and the underlying group call will still continue. This API is available in the following national cloud deployments.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/call-delete?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[CallItemRequestBuilderGetRequestConfiguration] = None) -> Optional[Call]:
        """
        Retrieve the properties and relationships of a call object. This API is available in the following national cloud deployments.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Call]
        Find more info here: https://learn.microsoft.com/graph/api/call-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.call import Call

        return await self.request_adapter.send_async(request_info, Call, error_mapping)
    
    async def patch(self,body: Optional[Call] = None, request_configuration: Optional[CallItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[Call]:
        """
        Update the navigation property calls in communications
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Call]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.call import Call

        return await self.request_adapter.send_async(request_info, Call, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[CallItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete or hang up an active call. For group calls, this will only delete your call leg and the underlying group call will still continue. This API is available in the following national cloud deployments.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        request_info.headers.try_add("Accept", "application/json, application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[CallItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of a call object. This API is available in the following national cloud deployments.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json;q=1")
        return request_info
    
    def to_patch_request_information(self,body: Optional[Call] = None, request_configuration: Optional[CallItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property calls in communications
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers.try_add("Accept", "application/json;q=1")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> CallItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CallItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return CallItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def add_large_gallery_view(self) -> AddLargeGalleryViewRequestBuilder:
        """
        Provides operations to call the addLargeGalleryView method.
        """
        from .add_large_gallery_view.add_large_gallery_view_request_builder import AddLargeGalleryViewRequestBuilder

        return AddLargeGalleryViewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def answer(self) -> AnswerRequestBuilder:
        """
        Provides operations to call the answer method.
        """
        from .answer.answer_request_builder import AnswerRequestBuilder

        return AnswerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def audio_routing_groups(self) -> AudioRoutingGroupsRequestBuilder:
        """
        Provides operations to manage the audioRoutingGroups property of the microsoft.graph.call entity.
        """
        from .audio_routing_groups.audio_routing_groups_request_builder import AudioRoutingGroupsRequestBuilder

        return AudioRoutingGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cancel_media_processing(self) -> CancelMediaProcessingRequestBuilder:
        """
        Provides operations to call the cancelMediaProcessing method.
        """
        from .cancel_media_processing.cancel_media_processing_request_builder import CancelMediaProcessingRequestBuilder

        return CancelMediaProcessingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def change_screen_sharing_role(self) -> ChangeScreenSharingRoleRequestBuilder:
        """
        Provides operations to call the changeScreenSharingRole method.
        """
        from .change_screen_sharing_role.change_screen_sharing_role_request_builder import ChangeScreenSharingRoleRequestBuilder

        return ChangeScreenSharingRoleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def content_sharing_sessions(self) -> ContentSharingSessionsRequestBuilder:
        """
        Provides operations to manage the contentSharingSessions property of the microsoft.graph.call entity.
        """
        from .content_sharing_sessions.content_sharing_sessions_request_builder import ContentSharingSessionsRequestBuilder

        return ContentSharingSessionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def keep_alive(self) -> KeepAliveRequestBuilder:
        """
        Provides operations to call the keepAlive method.
        """
        from .keep_alive.keep_alive_request_builder import KeepAliveRequestBuilder

        return KeepAliveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mute(self) -> MuteRequestBuilder:
        """
        Provides operations to call the mute method.
        """
        from .mute.mute_request_builder import MuteRequestBuilder

        return MuteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.call entity.
        """
        from .operations.operations_request_builder import OperationsRequestBuilder

        return OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def participants(self) -> ParticipantsRequestBuilder:
        """
        Provides operations to manage the participants property of the microsoft.graph.call entity.
        """
        from .participants.participants_request_builder import ParticipantsRequestBuilder

        return ParticipantsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def play_prompt(self) -> PlayPromptRequestBuilder:
        """
        Provides operations to call the playPrompt method.
        """
        from .play_prompt.play_prompt_request_builder import PlayPromptRequestBuilder

        return PlayPromptRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def record(self) -> RecordRequestBuilder:
        """
        Provides operations to call the record method.
        """
        from .record.record_request_builder import RecordRequestBuilder

        return RecordRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def record_response(self) -> RecordResponseRequestBuilder:
        """
        Provides operations to call the recordResponse method.
        """
        from .record_response.record_response_request_builder import RecordResponseRequestBuilder

        return RecordResponseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def redirect(self) -> RedirectRequestBuilder:
        """
        Provides operations to call the redirect method.
        """
        from .redirect.redirect_request_builder import RedirectRequestBuilder

        return RedirectRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reject(self) -> RejectRequestBuilder:
        """
        Provides operations to call the reject method.
        """
        from .reject.reject_request_builder import RejectRequestBuilder

        return RejectRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def subscribe_to_tone(self) -> SubscribeToToneRequestBuilder:
        """
        Provides operations to call the subscribeToTone method.
        """
        from .subscribe_to_tone.subscribe_to_tone_request_builder import SubscribeToToneRequestBuilder

        return SubscribeToToneRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def transfer(self) -> TransferRequestBuilder:
        """
        Provides operations to call the transfer method.
        """
        from .transfer.transfer_request_builder import TransferRequestBuilder

        return TransferRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unmute(self) -> UnmuteRequestBuilder:
        """
        Provides operations to call the unmute method.
        """
        from .unmute.unmute_request_builder import UnmuteRequestBuilder

        return UnmuteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def update_recording_status(self) -> UpdateRecordingStatusRequestBuilder:
        """
        Provides operations to call the updateRecordingStatus method.
        """
        from .update_recording_status.update_recording_status_request_builder import UpdateRecordingStatusRequestBuilder

        return UpdateRecordingStatusRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class CallItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class CallItemRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of a call object. This API is available in the following national cloud deployments.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class CallItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[CallItemRequestBuilder.CallItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class CallItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
