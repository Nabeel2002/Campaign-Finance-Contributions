CREATE TABLE contributions (
  contribution_id INTEGER PRIMARY KEY AUTOINCREMENT,
  donor_id INT NOT NULL,
  recipient_id INT NOT NULL,
  date_id INT NOT NULL,
  amount DECIMAL(10,2),
  in_kind_value DECIMAL(10,2),
  FOREIGN KEY (donor_id) REFERENCES donors(donor_id),
  FOREIGN KEY (recipient_id) REFERENCES recipients(recipient_id),
  FOREIGN KEY (date_id) REFERENCES dates(date_id)
);

CREATE TABLE donors (
  donor_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(255) NOT NULL,
  donor_type VARCHAR(50), -- Using VARCHAR instead of ENUM
  address VARCHAR(255),
  city VARCHAR(100),
  state VARCHAR(100)
);

CREATE TABLE recipients (
  recipient_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(255) NOT NULL,
  type VARCHAR(50) -- Using VARCHAR instead of ENUM
);


CREATE TABLE dates (
  date_id INTEGER PRIMARY KEY AUTOINCREMENT,
  date DATE NOT NULL,
  year INT NOT NULL
);
