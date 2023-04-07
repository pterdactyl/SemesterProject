/*
 * Copyright (c) 2023.
 */

use SemesterProject;
DELIMITER $$

DROP EVENT IF EXISTS clean_sinedata $$

CREATE PROCEDURE clean_data()
BEGIN
    TRUNCATE TABLE dashboard_sinedata;
    TRUNCATE table dashboard_heartbeatdata;
end $$


CREATE DEFINER =`root`@`%`
    EVENT `clean_sinedata`
    ON SCHEDULE EVERY 5 MINUTE STARTS now()
    ON COMPLETION NOT PRESERVE ENABLE
    DO
    BEGIN
        SIGNAL SQLSTATE '01000' SET MESSAGE_TEXT = 'clean_sinedata started';
        CALL clean_data;
        SIGNAL SQLSTATE '01000' SET MESSAGE_TEXT = 'clean_sinedata finished';
    END $$