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

attendance_records_request_builder = lazy_import('msgraph.generated.app.online_meetings.item.attendance_reports.item.attendance_records.attendance_records_request_builder')
attendance_record_item_request_builder = lazy_import('msgraph.generated.app.online_meetings.item.attendance_reports.item.attendance_records.item.attendance_record_item_request_builder')
meeting_attendance_report = lazy_import('msgraph.generated.models.meeting_attendance_report')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class MeetingAttendanceReportItemRequestBuilder():
    """
    Provides operations to manage the attendanceReports property of the microsoft.graph.onlineMeeting entity.
    """
    @property
    def attendance_records(self) -> attendance_records_request_builder.AttendanceRecordsRequestBuilder:
        """
        Provides operations to manage the attendanceRecords property of the microsoft.graph.meetingAttendanceReport entity.
        """
        return attendance_records_request_builder.AttendanceRecordsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def attendance_records_by_id(self,id: str) -> attendance_record_item_request_builder.AttendanceRecordItemRequestBuilder:
        """
        Provides operations to manage the attendanceRecords property of the microsoft.graph.meetingAttendanceReport entity.
        Args:
            id: Unique identifier of the item
        Returns: attendance_record_item_request_builder.AttendanceRecordItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["attendanceRecord%2Did"] = id
        return attendance_record_item_request_builder.AttendanceRecordItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new MeetingAttendanceReportItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/app/onlineMeetings/{onlineMeeting%2Did}/attendanceReports/{meetingAttendanceReport%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[MeetingAttendanceReportItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property attendanceReports for app
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
    
    async def get(self,request_configuration: Optional[MeetingAttendanceReportItemRequestBuilderGetRequestConfiguration] = None) -> Optional[meeting_attendance_report.MeetingAttendanceReport]:
        """
        The attendance reports of an online meeting. Read-only.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[meeting_attendance_report.MeetingAttendanceReport]
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
        return await self.request_adapter.send_async(request_info, meeting_attendance_report.MeetingAttendanceReport, error_mapping)
    
    async def patch(self,body: Optional[meeting_attendance_report.MeetingAttendanceReport] = None, request_configuration: Optional[MeetingAttendanceReportItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[meeting_attendance_report.MeetingAttendanceReport]:
        """
        Update the navigation property attendanceReports in app
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[meeting_attendance_report.MeetingAttendanceReport]
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
        return await self.request_adapter.send_async(request_info, meeting_attendance_report.MeetingAttendanceReport, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[MeetingAttendanceReportItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property attendanceReports for app
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
    
    def to_get_request_information(self,request_configuration: Optional[MeetingAttendanceReportItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The attendance reports of an online meeting. Read-only.
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
    
    def to_patch_request_information(self,body: Optional[meeting_attendance_report.MeetingAttendanceReport] = None, request_configuration: Optional[MeetingAttendanceReportItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property attendanceReports in app
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
    class MeetingAttendanceReportItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class MeetingAttendanceReportItemRequestBuilderGetQueryParameters():
        """
        The attendance reports of an online meeting. Read-only.
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
    class MeetingAttendanceReportItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[MeetingAttendanceReportItemRequestBuilder.MeetingAttendanceReportItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class MeetingAttendanceReportItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

