-- 4.10. Find all Courses by Client’s Phone Number
-- url: https://judge.softuni.org/Contests/Practice/Index/4297#9

CREATE OR REPLACE FUNCTION fn_courses_by_client(
    IN phone_num VARCHAR(20),
    OUT number_of_courses INT
)
AS
$$
BEGIN

    SELECT count(c1.id)
    INTO number_of_courses
    FROM clients c1
             JOIN courses c2 ON c1.id = c2.client_id
    WHERE c1.phone_number = phone_num;
END;
$$
    LANGUAGE plpgsql;

-- Test examples
SELECT fn_courses_by_client('(803) 6386812');
SELECT fn_courses_by_client('(831) 1391236');
SELECT fn_courses_by_client('(704) 2502909');