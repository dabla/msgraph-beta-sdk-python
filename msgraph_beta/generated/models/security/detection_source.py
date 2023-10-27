from enum import Enum

class DetectionSource(str, Enum):
    Unknown = "unknown",
    MicrosoftDefenderForEndpoint = "microsoftDefenderForEndpoint",
    Antivirus = "antivirus",
    SmartScreen = "smartScreen",
    CustomTi = "customTi",
    MicrosoftDefenderForOffice365 = "microsoftDefenderForOffice365",
    AutomatedInvestigation = "automatedInvestigation",
    MicrosoftThreatExperts = "microsoftThreatExperts",
    CustomDetection = "customDetection",
    MicrosoftDefenderForIdentity = "microsoftDefenderForIdentity",
    CloudAppSecurity = "cloudAppSecurity",
    Microsoft365Defender = "microsoft365Defender",
    AzureAdIdentityProtection = "azureAdIdentityProtection",
    Manual = "manual",
    MicrosoftDataLossPrevention = "microsoftDataLossPrevention",
    AppGovernancePolicy = "appGovernancePolicy",
    AppGovernanceDetection = "appGovernanceDetection",
    UnknownFutureValue = "unknownFutureValue",
    MicrosoftDefenderForCloud = "microsoftDefenderForCloud",
    MicrosoftDefenderForIoT = "microsoftDefenderForIoT",
    MicrosoftDefenderForServers = "microsoftDefenderForServers",
    MicrosoftDefenderForStorage = "microsoftDefenderForStorage",
    MicrosoftDefenderForDNS = "microsoftDefenderForDNS",
    MicrosoftDefenderForDatabases = "microsoftDefenderForDatabases",
    MicrosoftDefenderForContainers = "microsoftDefenderForContainers",
    MicrosoftDefenderForNetwork = "microsoftDefenderForNetwork",
    MicrosoftDefenderForAppService = "microsoftDefenderForAppService",
    MicrosoftDefenderForKeyVault = "microsoftDefenderForKeyVault",
    MicrosoftDefenderForResourceManager = "microsoftDefenderForResourceManager",
    MicrosoftDefenderForApiManagement = "microsoftDefenderForApiManagement",
    NrtAlerts = "nrtAlerts",
    ScheduledAlerts = "scheduledAlerts",
    MicrosoftDefenderThreatIntelligenceAnalytics = "microsoftDefenderThreatIntelligenceAnalytics",
    BuiltInMl = "builtInMl",
    MicrosoftSentinel = "microsoftSentinel",
