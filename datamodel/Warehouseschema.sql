CREATE TABLE contributions (
  contribution_id INT PRIMARY KEY AUTO_INCREMENT,
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
  donor_id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  donor_type ENUM('individual', 'entity'),
  address VARCHAR(255),
  city VARCHAR(100),
  state VARCHAR(

CREATE TABLE recipients (
  recipient_id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  type ENUM('candidate', 'officeholder', 'committee')
);

CREATE TABLE dates (
  date_id INT PRIMARY KEY AUTO_INCREMENT,
  date DATE NOT NULL,
  year INT NOT NULL
);