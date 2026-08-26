CREATE DATABASE IF NOT EXISTS attendance_tracker;

USE attendance_tracker;

CREATE TABLE IF NOT EXISTS participants (
    id INT AUTO_INCREMENT PRIMARY KEY,
    participant_id VARCHAR(20) NOT NULL UNIQUE,
    name VARCHAR(50) NOT NULL,
    attendance ENUM('Present', 'Absent') NOT NULL DEFAULT 'Absent'
);