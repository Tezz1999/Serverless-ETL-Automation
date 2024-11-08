CREATE TABLE UserProfile (
    ResponseId INT PRIMARY KEY,
    Age VARCHAR(50),
    Employment VARCHAR(100),
    RemoteWork VARCHAR(50),
    EdLevel VARCHAR(100),
    Country VARCHAR(100),
    CompTotal DECIMAL(15, 2),
    ConvertedCompYearly DECIMAL(15, 2)
);

CREATE TABLE ProfessionalTech (
    ResponseId INT,
    DevType VARCHAR(100),
    OrgSize VARCHAR(50),
    PurchaseInfluence VARCHAR(50),
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
    OpSysPersonalUse VARCHAR(100),
    OpSysProfessionalUse VARCHAR(100),
    OfficeStackAsyncHaveWorkedWith TEXT,
    OfficeStackAsyncWantToWorkWith TEXT,
    OfficeStackSyncHaveWorkedWith TEXT,
    OfficeStackSyncWantToWorkWith TEXT,
    CONSTRAINT fk_techstackusage_userprofile FOREIGN KEY (ResponseId) REFERENCES UserProfile(ResponseId)
);

CREATE TABLE AIInteraction (
    ResponseId INT,
    SOAI VARCHAR(50),
    AISelect TEXT,
    AISent VARCHAR(50),
    AIAcc VARCHAR(50),
    AIBen TEXT,
    AIToolInterested TEXT,
    AIToolUsing TEXT,
    CONSTRAINT fk_aiinteraction_userprofile FOREIGN KEY (ResponseId) REFERENCES UserProfile(ResponseId)
);

CREATE TABLE SurveyInteraction (
    ResponseId INT,
    SOVisitFreq VARCHAR(50),
    SOAccount VARCHAR(10),
    SOPartFreq VARCHAR(50),
    SOComm VARCHAR(50),
    CONSTRAINT fk_surveyinteraction_userprofile FOREIGN KEY (ResponseId) REFERENCES UserProfile(ResponseId)
);
