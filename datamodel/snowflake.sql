CREATE TABLE Donors (
  Donor VARCHAR(255) PRIMARY KEY,
  Donor_Type VARCHAR(20),
  Donor_Address VARCHAR(255),
  City_State_Zip VARCHAR(100),
  Donor_Reported_Occupation VARCHAR(255),
  Donor_Reported_Employer VARCHAR(255)
);

CREATE TABLE Recipients (
  Recipient VARCHAR(255) PRIMARY KEY
);

CREATE TABLE Dates (
  Contribution_Date DATE PRIMARY KEY,
  Contribution_Year INT
);

-- Optional Dimension Tables
CREATE TABLE Report_Types (
  Report_Filed VARCHAR(255) PRIMARY KEY
);

CREATE TABLE Contribution_Types (
  Contribution_Type VARCHAR(255) PRIMARY KEY
);

CREATE TABLE Contributions (
  Transaction INT PRIMARY KEY,
  Recipient VARCHAR(255) REFERENCES Recipients(Recipient),
  Contribution_Date DATE REFERENCES Dates(Contribution_Date),
  Contribution_Amount DECIMAL(10,2),
  Donor VARCHAR(255) REFERENCES Donors(Donor),
  In_Kind_Description VARCHAR(255),
  Out_of_State_PAC_ID VARCHAR(20),
  Correction VARCHAR(10),
  View_Report VARCHAR(255),
  FOREIGN KEY (Contribution_Type) REFERENCES Contribution_Types(Contribution_Type),  -- Add if using optional table
  FOREIGN KEY (Report_Filed) REFERENCES Report_Types(Report_Filed)  -- Add if using optional table
);
