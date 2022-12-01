from enum import Enum

class MessageEventType(Enum):
    Received = "received",
    Sent = "sent",
    Delivered = "delivered",
    Failed = "failed",
    ProcessingFailed = "processingFailed",
    DistributionGroupExpanded = "distributionGroupExpanded",
    Submitted = "submitted",
    Delayed = "delayed",
    Redirected = "redirected",
    Resolved = "resolved",
    Dropped = "dropped",
    RecipientsAdded = "recipientsAdded",
    MalwareDetected = "malwareDetected",
    MalwareDetectedInMessage = "malwareDetectedInMessage",
    MalwareDetectedInAttachment = "malwareDetectedInAttachment",
    TtZapped = "ttZapped",
    TtDelivered = "ttDelivered",
    SpamDetected = "spamDetected",
    TransportRuleTriggered = "transportRuleTriggered",
    DlpRuleTriggered = "dlpRuleTriggered",
    Journaled = "journaled",
    UnknownFutureValue = "unknownFutureValue",
