-- Select the database
USE hbtn_0c_0;

-- Convert the database character set and collation
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the table character set and collation
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the name field character set and collation
ALTER TABLE first_table MODIFY COLUMN `name` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
