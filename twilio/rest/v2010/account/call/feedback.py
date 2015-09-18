# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource


class FeedbackContext(InstanceContext):

    def __init__(self, domain, account_sid, call_sid):
        super(FeedbackContext, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'account_sid': account_sid,
            'call_sid': call_sid,
        }
        self._uri = "/Accounts/{account_sid}/Calls/{call_sid}/Feedback.json".format(**self._instance_kwargs)

    def create(self, quality_score, issue=values.unset):
        data = values.of({
            "QualityScore": quality_score,
            "Issue": issue,
        })
        
        return self._domain.create(
            FeedbackInstance,
            self._instance_kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def fetch(self):
        return self._domain.fetch(
            FeedbackInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
        )

    def update(self, quality_score, issue=values.unset):
        data = values.of({
            "QualityScore": quality_score,
            "Issue": issue,
        })
        
        return self._domain.update(
            FeedbackInstance,
            self._instance_kwargs,
            'POST',
            self._uri,
            data=data,
        )


class FeedbackInstance(InstanceResource):

    def __init__(self, domain, payload, account_sid=None, call_sid=None):
        super(FeedbackInstance, self).__init__(domain)
        
        # Marshaled Properties
        self._account_sid = payload['account_sid']
        self._date_created = deserialize.iso8601_datetime(payload['date_created'])
        self._date_updated = deserialize.iso8601_datetime(payload['date_updated'])
        self._issues = payload['issues']
        self._quality_score = payload['quality_score']
        self._sid = payload['sid']
        
        # Context
        self._lazy_context = None
        self._context_account_sid = account_sid or self._account_sid
        self._context_call_sid = call_sid or self._call_sid

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = FeedbackContext(
                self._domain,
                self._context_account_sid,
                self._context_call_sid,
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The account_sid """
        return self._account_sid

    @property
    def date_created(self):
        """ The date_created """
        return self._date_created

    @property
    def date_updated(self):
        """ The date_updated """
        return self._date_updated

    @property
    def issues(self):
        """ The issues """
        return self._issues

    @property
    def quality_score(self):
        """ 1 to 5 quality score """
        return self._quality_score

    @property
    def sid(self):
        """ The sid """
        return self._sid

    def create(self, quality_score, issue=values.unset):
        self._context.create(
            quality_score,
            issue=issue,
        )

    def fetch(self):
        self._context.fetch()

    def update(self, quality_score, issue=values.unset):
        self._context.update(
            quality_score,
            issue=issue,
        )