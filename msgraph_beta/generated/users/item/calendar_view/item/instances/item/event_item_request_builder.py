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
    from .......models.event import Event
    from .......models.o_data_errors.o_data_error import ODataError
    from .accept.accept_request_builder import AcceptRequestBuilder
    from .attachments.attachments_request_builder import AttachmentsRequestBuilder
    from .calendar.calendar_request_builder import CalendarRequestBuilder
    from .cancel.cancel_request_builder import CancelRequestBuilder
    from .decline.decline_request_builder import DeclineRequestBuilder
    from .dismiss_reminder.dismiss_reminder_request_builder import DismissReminderRequestBuilder
    from .exception_occurrences.exception_occurrences_request_builder import ExceptionOccurrencesRequestBuilder
    from .extensions.extensions_request_builder import ExtensionsRequestBuilder
    from .forward.forward_request_builder import ForwardRequestBuilder
    from .snooze_reminder.snooze_reminder_request_builder import SnoozeReminderRequestBuilder
    from .tentatively_accept.tentatively_accept_request_builder import TentativelyAcceptRequestBuilder

class EventItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the instances property of the microsoft.graph.event entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new EventItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/calendarView/{event%2Did}/instances/{event%2Did1}{?startDateTime*,endDateTime*,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[EventItemRequestBuilderGetRequestConfiguration] = None) -> Optional[Event]:
        """
        The occurrences of a recurring series, if the event is a series master. This property includes occurrences that are part of the recurrence pattern, and exceptions that have been modified, but does not include occurrences that have been cancelled from the series. Navigation property. Read-only. Nullable.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Event]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.event import Event

        return await self.request_adapter.send_async(request_info, Event, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[EventItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The occurrences of a recurring series, if the event is a series master. This property includes occurrences that are part of the recurrence pattern, and exceptions that have been modified, but does not include occurrences that have been cancelled from the series. Navigation property. Read-only. Nullable.
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
    
    def with_url(self,raw_url: Optional[str] = None) -> EventItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: EventItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return EventItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def accept(self) -> AcceptRequestBuilder:
        """
        Provides operations to call the accept method.
        """
        from .accept.accept_request_builder import AcceptRequestBuilder

        return AcceptRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def attachments(self) -> AttachmentsRequestBuilder:
        """
        Provides operations to manage the attachments property of the microsoft.graph.event entity.
        """
        from .attachments.attachments_request_builder import AttachmentsRequestBuilder

        return AttachmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def calendar(self) -> CalendarRequestBuilder:
        """
        Provides operations to manage the calendar property of the microsoft.graph.event entity.
        """
        from .calendar.calendar_request_builder import CalendarRequestBuilder

        return CalendarRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cancel(self) -> CancelRequestBuilder:
        """
        Provides operations to call the cancel method.
        """
        from .cancel.cancel_request_builder import CancelRequestBuilder

        return CancelRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def decline(self) -> DeclineRequestBuilder:
        """
        Provides operations to call the decline method.
        """
        from .decline.decline_request_builder import DeclineRequestBuilder

        return DeclineRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dismiss_reminder(self) -> DismissReminderRequestBuilder:
        """
        Provides operations to call the dismissReminder method.
        """
        from .dismiss_reminder.dismiss_reminder_request_builder import DismissReminderRequestBuilder

        return DismissReminderRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def exception_occurrences(self) -> ExceptionOccurrencesRequestBuilder:
        """
        Provides operations to manage the exceptionOccurrences property of the microsoft.graph.event entity.
        """
        from .exception_occurrences.exception_occurrences_request_builder import ExceptionOccurrencesRequestBuilder

        return ExceptionOccurrencesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def extensions(self) -> ExtensionsRequestBuilder:
        """
        Provides operations to manage the extensions property of the microsoft.graph.event entity.
        """
        from .extensions.extensions_request_builder import ExtensionsRequestBuilder

        return ExtensionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def forward(self) -> ForwardRequestBuilder:
        """
        Provides operations to call the forward method.
        """
        from .forward.forward_request_builder import ForwardRequestBuilder

        return ForwardRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def snooze_reminder(self) -> SnoozeReminderRequestBuilder:
        """
        Provides operations to call the snoozeReminder method.
        """
        from .snooze_reminder.snooze_reminder_request_builder import SnoozeReminderRequestBuilder

        return SnoozeReminderRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tentatively_accept(self) -> TentativelyAcceptRequestBuilder:
        """
        Provides operations to call the tentativelyAccept method.
        """
        from .tentatively_accept.tentatively_accept_request_builder import TentativelyAcceptRequestBuilder

        return TentativelyAcceptRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class EventItemRequestBuilderGetQueryParameters():
        """
        The occurrences of a recurring series, if the event is a series master. This property includes occurrences that are part of the recurrence pattern, and exceptions that have been modified, but does not include occurrences that have been cancelled from the series. Navigation property. Read-only. Nullable.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "end_date_time":
                return "endDateTime"
            if original_name == "select":
                return "%24select"
            if original_name == "start_date_time":
                return "startDateTime"
            return original_name
        
        # The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
        end_date_time: Optional[str] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        # The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00
        start_date_time: Optional[str] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class EventItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[EventItemRequestBuilder.EventItemRequestBuilderGetQueryParameters] = None

    
