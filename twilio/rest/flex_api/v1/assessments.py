r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Flex
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class AssessmentsInstance(InstanceResource):

    """
    :ivar account_sid: The unique SID identifier of the Account.
    :ivar assessment_sid: The SID of the assessment
    :ivar offset: Offset of the conversation
    :ivar report: The flag indicating if this assessment is part of report
    :ivar weight: The weightage given to this comment
    :ivar agent_id: The id of the Agent
    :ivar segment_id: Segment Id of conversation
    :ivar user_name: The name of the user.
    :ivar user_email: The email id of the user.
    :ivar answer_text: The answer text selected by user
    :ivar answer_id: The id of the answer selected by user
    :ivar assessment: Assessment Details associated with an assessment
    :ivar timestamp:
    :ivar url:
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        assessment_sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.assessment_sid: Optional[str] = payload.get("assessment_sid")
        self.offset: Optional[float] = deserialize.decimal(payload.get("offset"))
        self.report: Optional[bool] = payload.get("report")
        self.weight: Optional[float] = deserialize.decimal(payload.get("weight"))
        self.agent_id: Optional[str] = payload.get("agent_id")
        self.segment_id: Optional[str] = payload.get("segment_id")
        self.user_name: Optional[str] = payload.get("user_name")
        self.user_email: Optional[str] = payload.get("user_email")
        self.answer_text: Optional[str] = payload.get("answer_text")
        self.answer_id: Optional[str] = payload.get("answer_id")
        self.assessment: Optional[Dict[str, object]] = payload.get("assessment")
        self.timestamp: Optional[float] = deserialize.decimal(payload.get("timestamp"))
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "assessment_sid": assessment_sid or self.assessment_sid,
        }
        self._context: Optional[AssessmentsContext] = None

    @property
    def _proxy(self) -> "AssessmentsContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AssessmentsContext for this AssessmentsInstance
        """
        if self._context is None:
            self._context = AssessmentsContext(
                self._version,
                assessment_sid=self._solution["assessment_sid"],
            )
        return self._context

    def update(
        self,
        offset: float,
        answer_text: str,
        answer_id: str,
        token: Union[str, object] = values.unset,
    ) -> "AssessmentsInstance":
        """
        Update the AssessmentsInstance

        :param offset: The offset of the conversation
        :param answer_text: The answer text selected by user
        :param answer_id: The id of the answer selected by user
        :param token: The Token HTTP request header

        :returns: The updated AssessmentsInstance
        """
        return self._proxy.update(
            offset=offset,
            answer_text=answer_text,
            answer_id=answer_id,
            token=token,
        )

    async def update_async(
        self,
        offset: float,
        answer_text: str,
        answer_id: str,
        token: Union[str, object] = values.unset,
    ) -> "AssessmentsInstance":
        """
        Asynchronous coroutine to update the AssessmentsInstance

        :param offset: The offset of the conversation
        :param answer_text: The answer text selected by user
        :param answer_id: The id of the answer selected by user
        :param token: The Token HTTP request header

        :returns: The updated AssessmentsInstance
        """
        return await self._proxy.update_async(
            offset=offset,
            answer_text=answer_text,
            answer_id=answer_id,
            token=token,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.FlexApi.V1.AssessmentsInstance {}>".format(context)


class AssessmentsContext(InstanceContext):
    def __init__(self, version: Version, assessment_sid: str):
        """
        Initialize the AssessmentsContext

        :param version: Version that contains the resource
        :param assessment_sid: The SID of the assessment to be modified
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "assessment_sid": assessment_sid,
        }
        self._uri = "/Insights/QualityManagement/Assessments/{assessment_sid}".format(
            **self._solution
        )

    def update(
        self,
        offset: float,
        answer_text: str,
        answer_id: str,
        token: Union[str, object] = values.unset,
    ) -> AssessmentsInstance:
        """
        Update the AssessmentsInstance

        :param offset: The offset of the conversation
        :param answer_text: The answer text selected by user
        :param answer_id: The id of the answer selected by user
        :param token: The Token HTTP request header

        :returns: The updated AssessmentsInstance
        """
        data = values.of(
            {
                "Offset": offset,
                "AnswerText": answer_text,
                "AnswerId": answer_id,
            }
        )
        headers = values.of(
            {
                "Token": token,
            }
        )

        payload = self._version.update(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return AssessmentsInstance(
            self._version, payload, assessment_sid=self._solution["assessment_sid"]
        )

    async def update_async(
        self,
        offset: float,
        answer_text: str,
        answer_id: str,
        token: Union[str, object] = values.unset,
    ) -> AssessmentsInstance:
        """
        Asynchronous coroutine to update the AssessmentsInstance

        :param offset: The offset of the conversation
        :param answer_text: The answer text selected by user
        :param answer_id: The id of the answer selected by user
        :param token: The Token HTTP request header

        :returns: The updated AssessmentsInstance
        """
        data = values.of(
            {
                "Offset": offset,
                "AnswerText": answer_text,
                "AnswerId": answer_id,
            }
        )
        headers = values.of(
            {
                "Token": token,
            }
        )

        payload = await self._version.update_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return AssessmentsInstance(
            self._version, payload, assessment_sid=self._solution["assessment_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.FlexApi.V1.AssessmentsContext {}>".format(context)


class AssessmentsPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> AssessmentsInstance:
        """
        Build an instance of AssessmentsInstance

        :param payload: Payload response from the API
        """
        return AssessmentsInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.FlexApi.V1.AssessmentsPage>"


class AssessmentsList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the AssessmentsList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Insights/QualityManagement/Assessments"

    def create(
        self,
        category_sid: str,
        category_name: str,
        segment_id: str,
        user_name: str,
        user_email: str,
        agent_id: str,
        offset: float,
        metric_id: str,
        metric_name: str,
        answer_text: str,
        answer_id: str,
        questionnaire_sid: str,
        token: Union[str, object] = values.unset,
    ) -> AssessmentsInstance:
        """
        Create the AssessmentsInstance

        :param category_sid: The SID of the category
        :param category_name: The name of the category
        :param segment_id: Segment Id of the conversation
        :param user_name: Name of the user assessing conversation
        :param user_email: Email of the user assessing conversation
        :param agent_id: The id of the Agent
        :param offset: The offset of the conversation.
        :param metric_id: The question SID selected for assessment
        :param metric_name: The question name of the assessment
        :param answer_text: The answer text selected by user
        :param answer_id: The id of the answer selected by user
        :param questionnaire_sid: Questionnaire SID of the associated question
        :param token: The Token HTTP request header

        :returns: The created AssessmentsInstance
        """
        data = values.of(
            {
                "CategorySid": category_sid,
                "CategoryName": category_name,
                "SegmentId": segment_id,
                "UserName": user_name,
                "UserEmail": user_email,
                "AgentId": agent_id,
                "Offset": offset,
                "MetricId": metric_id,
                "MetricName": metric_name,
                "AnswerText": answer_text,
                "AnswerId": answer_id,
                "QuestionnaireSid": questionnaire_sid,
            }
        )
        headers = values.of(
            {
                "Token": token,
            }
        )
        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return AssessmentsInstance(self._version, payload)

    async def create_async(
        self,
        category_sid: str,
        category_name: str,
        segment_id: str,
        user_name: str,
        user_email: str,
        agent_id: str,
        offset: float,
        metric_id: str,
        metric_name: str,
        answer_text: str,
        answer_id: str,
        questionnaire_sid: str,
        token: Union[str, object] = values.unset,
    ) -> AssessmentsInstance:
        """
        Asynchronously create the AssessmentsInstance

        :param category_sid: The SID of the category
        :param category_name: The name of the category
        :param segment_id: Segment Id of the conversation
        :param user_name: Name of the user assessing conversation
        :param user_email: Email of the user assessing conversation
        :param agent_id: The id of the Agent
        :param offset: The offset of the conversation.
        :param metric_id: The question SID selected for assessment
        :param metric_name: The question name of the assessment
        :param answer_text: The answer text selected by user
        :param answer_id: The id of the answer selected by user
        :param questionnaire_sid: Questionnaire SID of the associated question
        :param token: The Token HTTP request header

        :returns: The created AssessmentsInstance
        """
        data = values.of(
            {
                "CategorySid": category_sid,
                "CategoryName": category_name,
                "SegmentId": segment_id,
                "UserName": user_name,
                "UserEmail": user_email,
                "AgentId": agent_id,
                "Offset": offset,
                "MetricId": metric_id,
                "MetricName": metric_name,
                "AnswerText": answer_text,
                "AnswerId": answer_id,
                "QuestionnaireSid": questionnaire_sid,
            }
        )
        headers = values.of(
            {
                "Token": token,
            }
        )
        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return AssessmentsInstance(self._version, payload)

    def stream(
        self,
        token: Union[str, object] = values.unset,
        segment_id: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[AssessmentsInstance]:
        """
        Streams AssessmentsInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str token: The Token HTTP request header
        :param str segment_id: The id of the segment.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            token=token, segment_id=segment_id, page_size=limits["page_size"]
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        token: Union[str, object] = values.unset,
        segment_id: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[AssessmentsInstance]:
        """
        Asynchronously streams AssessmentsInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str token: The Token HTTP request header
        :param str segment_id: The id of the segment.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            token=token, segment_id=segment_id, page_size=limits["page_size"]
        )

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        token: Union[str, object] = values.unset,
        segment_id: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[AssessmentsInstance]:
        """
        Lists AssessmentsInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str token: The Token HTTP request header
        :param str segment_id: The id of the segment.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(
            self.stream(
                token=token,
                segment_id=segment_id,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        token: Union[str, object] = values.unset,
        segment_id: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[AssessmentsInstance]:
        """
        Asynchronously lists AssessmentsInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str token: The Token HTTP request header
        :param str segment_id: The id of the segment.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [
            record
            async for record in await self.stream_async(
                token=token,
                segment_id=segment_id,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        token: Union[str, object] = values.unset,
        segment_id: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> AssessmentsPage:
        """
        Retrieve a single page of AssessmentsInstance records from the API.
        Request is executed immediately

        :param token: The Token HTTP request header
        :param segment_id: The id of the segment.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AssessmentsInstance
        """
        data = values.of(
            {
                "Token": token,
                "SegmentId": segment_id,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return AssessmentsPage(self._version, response)

    async def page_async(
        self,
        token: Union[str, object] = values.unset,
        segment_id: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> AssessmentsPage:
        """
        Asynchronously retrieve a single page of AssessmentsInstance records from the API.
        Request is executed immediately

        :param token: The Token HTTP request header
        :param segment_id: The id of the segment.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AssessmentsInstance
        """
        data = values.of(
            {
                "Token": token,
                "SegmentId": segment_id,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return AssessmentsPage(self._version, response)

    def get_page(self, target_url: str) -> AssessmentsPage:
        """
        Retrieve a specific page of AssessmentsInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AssessmentsInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return AssessmentsPage(self._version, response)

    async def get_page_async(self, target_url: str) -> AssessmentsPage:
        """
        Asynchronously retrieve a specific page of AssessmentsInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AssessmentsInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return AssessmentsPage(self._version, response)

    def get(self, assessment_sid: str) -> AssessmentsContext:
        """
        Constructs a AssessmentsContext

        :param assessment_sid: The SID of the assessment to be modified
        """
        return AssessmentsContext(self._version, assessment_sid=assessment_sid)

    def __call__(self, assessment_sid: str) -> AssessmentsContext:
        """
        Constructs a AssessmentsContext

        :param assessment_sid: The SID of the assessment to be modified
        """
        return AssessmentsContext(self._version, assessment_sid=assessment_sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.FlexApi.V1.AssessmentsList>"
