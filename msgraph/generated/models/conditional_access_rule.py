from enum import Enum

class ConditionalAccessRule(Enum):
    AllApps = "allApps",
    FirstPartyApps = "firstPartyApps",
    Office365 = "office365",
    AppId = "appId",
    Acr = "acr",
    AppFilter = "appFilter",
    AllUsers = "allUsers",
    Guest = "guest",
    GroupId = "groupId",
    RoleId = "roleId",
    UserId = "userId",
    AllDevicePlatforms = "allDevicePlatforms",
    DevicePlatform = "devicePlatform",
    AllLocations = "allLocations",
    InsideCorpnet = "insideCorpnet",
    AllTrustedLocations = "allTrustedLocations",
    LocationId = "locationId",
    AllDevices = "allDevices",
    DeviceFilter = "deviceFilter",
    DeviceState = "deviceState",
    UnknownFutureValue = "unknownFutureValue",
    DeviceFilterIncludeRuleNotMatched = "deviceFilterIncludeRuleNotMatched",
    AllDeviceStates = "allDeviceStates",
    AnonymizedIPAddress = "anonymizedIPAddress",
    UnfamiliarFeatures = "unfamiliarFeatures",
    NationStateIPAddress = "nationStateIPAddress",
    RealTimeThreatIntelligence = "realTimeThreatIntelligence",
    InternalGuest = "internalGuest",
    B2bCollaborationGuest = "b2bCollaborationGuest",
    B2bCollaborationMember = "b2bCollaborationMember",
    B2bDirectConnectUser = "b2bDirectConnectUser",
    OtherExternalUser = "otherExternalUser",
    ServiceProvider = "serviceProvider",

