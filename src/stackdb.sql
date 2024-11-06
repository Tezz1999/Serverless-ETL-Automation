-- Create Database
CREATE DATABASE StackOverflowSurveyDB;
GO

-- Use the created Database
USE StackOverflowSurveyDB;
GO

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
    ResponseId INT FOREIGN KEY REFERENCES UserProfile(ResponseId),
    DevType VARCHAR(100),
    OrgSize VARCHAR(50),
    PurchaseInfluence VARCHAR(50),
    TechList TEXT,
    BuyNewTool TEXT
);

CREATE TABLE TechPreferences (
    ResponseId INT FOREIGN KEY REFERENCES UserProfile(ResponseId),
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
    ToolsTechWantToWorkWith TEXT
);

CREATE TABLE TechStackUsage (
    ResponseId INT FOREIGN KEY REFERENCES UserProfile(ResponseId),
    OpSysPersonalUse VARCHAR(100),
    OpSysProfessionalUse VARCHAR(100),
    OfficeStackAsyncHaveWorkedWith TEXT,
    OfficeStackAsyncWantToWorkWith TEXT,
    OfficeStackSyncHaveWorkedWith TEXT,
    OfficeStackSyncWantToWorkWith TEXT
);

CREATE TABLE AIInteraction (
    ResponseId INT FOREIGN KEY REFERENCES UserProfile(ResponseId),
    SOAI VARCHAR(50),
    AISelect TEXT,
    AISent VARCHAR(50),
    AIAcc VARCHAR(50),
    AIBen TEXT,
    AIToolInterested TEXT,
    AIToolUsing TEXT
);

CREATE TABLE SurveyInteraction (
    ResponseId INT FOREIGN KEY REFERENCES UserProfile(ResponseId),
    SOVisitFreq VARCHAR(50),
    SOAccount VARCHAR(10),
    SOPartFreq VARCHAR(50),
    SOComm VARCHAR(50)
);
