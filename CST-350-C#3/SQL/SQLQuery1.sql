CREATE TABLE [dbo].[ContactInfo] (
[Id] INT IDENTITY (1,1) NOT NULL, 
[Name] NVARCHAR (50) NULL,
[PhoneNumber] NVARCHAR (50) NULL,
[Address] NVARCHAR (50) NULL,
[City] NVARCHAR (50) NULL,
[Zip] Int (50) NULL,
PRIMARY KEY CLUSTERED ([Id] ASC)
);