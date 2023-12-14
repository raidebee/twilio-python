r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Numbers
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import date
from typing import Any, Dict, List, Optional
from twilio.base import deserialize
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class PortingPortInFetchInstance(InstanceResource):

    """
    :ivar port_in_request_sid: The SID of the Port In request. This is a unique identifier of the port in request.
    :ivar url: The URL of this Port In request
    :ivar account_sid: The Account SID that the numbers will be added to after they are ported into Twilio.
    :ivar notification_emails: List of emails for getting notifications about the LOA signing process. Allowed Max 10 emails.
    :ivar target_port_in_date: Minimum number of days in the future (at least 2 days) needs to be established with the Ops team for validation.
    :ivar target_port_in_time_range_start: Minimum hour in the future needs to be established with the Ops team for validation.
    :ivar target_port_in_time_range_end: Maximum hour in the future needs to be established with the Ops team for validation.
    :ivar losing_carrier_information: The information for the losing carrier.
    :ivar phone_numbers: The list of phone numbers to Port in. Phone numbers are in E.164 format (e.g. +16175551212).
    :ivar documents: The list of documents SID referencing a utility bills
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        port_in_request_sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.port_in_request_sid: Optional[str] = payload.get("port_in_request_sid")
        self.url: Optional[str] = payload.get("url")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.notification_emails: Optional[List[str]] = payload.get(
            "notification_emails"
        )
        self.target_port_in_date: Optional[date] = deserialize.iso8601_date(
            payload.get("target_port_in_date")
        )
        self.target_port_in_time_range_start: Optional[str] = payload.get(
            "target_port_in_time_range_start"
        )
        self.target_port_in_time_range_end: Optional[str] = payload.get(
            "target_port_in_time_range_end"
        )
        self.losing_carrier_information: Optional[Dict[str, object]] = payload.get(
            "losing_carrier_information"
        )
        self.phone_numbers: Optional[List[object]] = payload.get("phone_numbers")
        self.documents: Optional[List[str]] = payload.get("documents")

        self._solution = {
            "port_in_request_sid": port_in_request_sid or self.port_in_request_sid,
        }
        self._context: Optional[PortingPortInFetchContext] = None

    @property
    def _proxy(self) -> "PortingPortInFetchContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: PortingPortInFetchContext for this PortingPortInFetchInstance
        """
        if self._context is None:
            self._context = PortingPortInFetchContext(
                self._version,
                port_in_request_sid=self._solution["port_in_request_sid"],
            )
        return self._context

    def fetch(self) -> "PortingPortInFetchInstance":
        """
        Fetch the PortingPortInFetchInstance


        :returns: The fetched PortingPortInFetchInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "PortingPortInFetchInstance":
        """
        Asynchronous coroutine to fetch the PortingPortInFetchInstance


        :returns: The fetched PortingPortInFetchInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Numbers.V1.PortingPortInFetchInstance {}>".format(context)


class PortingPortInFetchContext(InstanceContext):
    def __init__(self, version: Version, port_in_request_sid: str):
        """
        Initialize the PortingPortInFetchContext

        :param version: Version that contains the resource
        :param port_in_request_sid: The SID of the Port In request. This is a unique identifier of the port in request.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "port_in_request_sid": port_in_request_sid,
        }
        self._uri = "/Porting/PortIn/{port_in_request_sid}".format(**self._solution)

    def fetch(self) -> PortingPortInFetchInstance:
        """
        Fetch the PortingPortInFetchInstance


        :returns: The fetched PortingPortInFetchInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return PortingPortInFetchInstance(
            self._version,
            payload,
            port_in_request_sid=self._solution["port_in_request_sid"],
        )

    async def fetch_async(self) -> PortingPortInFetchInstance:
        """
        Asynchronous coroutine to fetch the PortingPortInFetchInstance


        :returns: The fetched PortingPortInFetchInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return PortingPortInFetchInstance(
            self._version,
            payload,
            port_in_request_sid=self._solution["port_in_request_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Numbers.V1.PortingPortInFetchContext {}>".format(context)


class PortingPortInFetchList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the PortingPortInFetchList

        :param version: Version that contains the resource

        """
        super().__init__(version)

    def get(self, port_in_request_sid: str) -> PortingPortInFetchContext:
        """
        Constructs a PortingPortInFetchContext

        :param port_in_request_sid: The SID of the Port In request. This is a unique identifier of the port in request.
        """
        return PortingPortInFetchContext(
            self._version, port_in_request_sid=port_in_request_sid
        )

    def __call__(self, port_in_request_sid: str) -> PortingPortInFetchContext:
        """
        Constructs a PortingPortInFetchContext

        :param port_in_request_sid: The SID of the Port In request. This is a unique identifier of the port in request.
        """
        return PortingPortInFetchContext(
            self._version, port_in_request_sid=port_in_request_sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Numbers.V1.PortingPortInFetchList>"
