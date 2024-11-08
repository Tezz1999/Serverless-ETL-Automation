CREATE DATABASE StackOverflowSurveyData;

\c StackOverflowSurveyData

CREATE TABLE UserProfile (
    ResponseId INT PRIMARY KEY,
    Age VARCHAR(100),
    Employment TEXT,
    RemoteWork VARCHAR(100),
    EdLevel VARCHAR(150),
    Country VARCHAR(100),
    CompTotal DECIMAL(15, 2),
    ConvertedCompYearly DECIMAL(15, 2)
);

CREATE TABLE ProfessionalTech (
    ResponseId INT,
    DevType TEXT,
    OrgSize VARCHAR(100),
    PurchaseInfluence VARCHAR(100),
    TechList TEXT,
    BuyNewTool TEXT,
    CONSTRAINT fk_professionaltech_userprofile FOREIGN KEY (ResponseId) REFERENCES UserProfile(ResponseId)
);

CREATE TABLE TechPreferences (
    ResponseId INT,
    LanguageHaveWorkedWith TEXT,
    LanguageWantToWorkWith TEXT,
    DatabaseHaveWorkedWith TEXT,
    DatabaseWantToWorkWith TEXT,
    PlatformHaveWorkedWith TEXT,
    PlatformWantToWorkWith TEXT,
    WebframeHaveWorkedWith TEXT,
    WebframeWantToWorkWith TEXT,
    MiscTechHaveWorkedWith TEXT,
    MiscTechWantToWorkWith TEXT,
    ToolsTechHaveWorkedWith TEXT,
    ToolsTechWantToWorkWith TEXT,
    CONSTRAINT fk_techpreferences_userprofile FOREIGN KEY (ResponseId) REFERENCES UserProfile(ResponseId)
);

CREATE TABLE TechStackUsage (
    ResponseId INT,
    OpSysPersonalUse TEXT,
    OpSysProfessionalUse TEXT,
    OfficeStackAsyncHaveWorkedWith TEXT,
    OfficeStackAsyncWantToWorkWith TEXT,
    OfficeStackSyncHaveWorkedWith TEXT,
    OfficeStackSyncWantToWorkWith TEXT,
    CONSTRAINT fk_techstackusage_userprofile FOREIGN KEY (ResponseId) REFERENCES UserProfile(ResponseId)
);

CREATE TABLE AIInteraction (
    ResponseId INT,
    SOAI TEXT,
    AISelect TEXT,
    AISent TEXT,
    AIAcc TEXT,
    AIBen TEXT,
    AIToolInterested TEXT,
    AIToolUsing TEXT,
    CONSTRAINT fk_aiinteraction_userprofile FOREIGN KEY (ResponseId) REFERENCES UserProfile(ResponseId)
);

CREATE TABLE SurveyInteraction (
    ResponseId INT,
    SOVisitFreq VARCHAR(100),
    SOAccount VARCHAR(50),
    SOPartFreq VARCHAR(100),
    SOComm VARCHAR(100),
    CONSTRAINT fk_surveyinteraction_userprofile FOREIGN KEY (ResponseId) REFERENCES UserProfile(ResponseId)
);