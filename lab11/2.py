import psycopg2

# Connect to the PostgreSQL database
conn= psycopg2.connect(host="localhost", dbname="postgres", user="postgres",
                       password="dilnaz", port="5433")
cur = conn.cursor()

# Function that returns all records based on a pattern
cur.execute("""
CREATE OR REPLACE FUNCTION get_records_by_pattern(pattern VARCHAR(255))
RETURNS TABLE (id INT, first_name VARCHAR(255), last_name VARCHAR(255), phone_number VARCHAR(20))
AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM PhoneBook WHERE first_name ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;
""")

# Procedure to insert new user by name and phone, update phone if user already exists
cur.execute("""
CREATE OR REPLACE PROCEDURE insert_update_user(
    p_first_name VARCHAR(255),
    p_last_name VARCHAR(255),
    p_phone_number VARCHAR(20)
)
AS $$
BEGIN
    INSERT INTO PhoneBook (first_name, last_name, phone_number)
    VALUES (p_first_name, p_last_name, p_phone_number)
    ON CONFLICT (first_name) DO UPDATE
    SET phone_number = p_phone_number;
END;
$$ LANGUAGE plpgsql;
""")

# Procedure to insert many new users by list of name and phone
cur.execute("""
CREATE OR REPLACE PROCEDURE insert_many_users(users_data TEXT[])
AS $$
DECLARE
    user_data TEXT;
    user_name VARCHAR(255);
    user_phone VARCHAR(20);
BEGIN
    FOREACH user_data IN ARRAY users_data
    LOOP
        user_name := split_part(user_data, ',', 1);
        user_phone := split_part(user_data, ',', 2);
        
        IF LENGTH(user_phone) != 10 THEN
            RAISE EXCEPTION 'Invalid phone number format: %', user_phone;
        END IF;
        
        INSERT INTO PhoneBook (first_name, phone_number)
        VALUES (user_name, user_phone);
    END LOOP;
END;
$$ LANGUAGE plpgsql;
""")

# Function to querying data from the tables with pagination
cur.execute("""
CREATE OR REPLACE FUNCTION get_records_with_pagination(limit_val INT, offset_val INT)
RETURNS TABLE (id INT, first_name VARCHAR(255), last_name VARCHAR(255), phone_number VARCHAR(20))
AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM PhoneBook LIMIT limit_val OFFSET offset_val;
END;
$$ LANGUAGE plpgsql;
""")

# Procedure to deleting data from tables by username or phone
cur.execute("""
CREATE OR REPLACE PROCEDURE delete_user(username VARCHAR(255))
AS $$
BEGIN
    DELETE FROM PhoneBook WHERE first_name = username;
END;
$$ LANGUAGE plpgsql;
""")

# Close the cursor and commit the transaction
conn.commit()
cur.close()
conn.close()
