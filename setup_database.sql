CREATE DATABASE IF NOT EXISTS EXPLOIT_CVE;
USE EXPLOIT_CVE;

CREATE TABLE exploit_cve(
    id              INT unsigned NOT NULL AUTO_INCREMENT, # Unique ID for the record
    exploit            VARCHAR(256) NOT NULL, # Name of the cat
    cve           VARCHAR(256) NOT NULL, # Owner of the cat            
    PRIMARY KEY     (id) # Make the id the primary key
);

SHOW TABLES;
DESCRIBE exploit_cve;