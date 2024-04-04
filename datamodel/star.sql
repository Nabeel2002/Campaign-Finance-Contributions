CREATE TABLE Contributions_Fact (
    contribution_id INT PRIMARY KEY,
    donor_id INT,
    recipient_id INT,
    contribution_date DATE,
    contribution_amount DECIMAL(10,2),
    contribution_type VARCHAR(50),
    in_kind_description VARCHAR(255),
    out_of_state_pac_id VARCHAR(50),
    correction VARCHAR(50),
    report_filed VARCHAR(50),
    transaction INT,
    FOREIGN KEY (donor_id) REFERENCES Donors_Dim(donor_id),
    FOREIGN KEY (recipient_id) REFERENCES Recipients_Dim(recipient_id)
);

CREATE TABLE Donors_Dim (
    donor_id INT PRIMARY KEY,
    donor_name VARCHAR(255),
    donor_type VARCHAR(50),
    donor_address VARCHAR(255),
    city_state_zip VARCHAR(100),
    donor_reported_occupation VARCHAR(100),
    donor_reported_employer VARCHAR(100)
);

CREATE TABLE Recipients_Dim (
    recipient_id INT PRIMARY KEY,
    recipient_name VARCHAR(255)
);
