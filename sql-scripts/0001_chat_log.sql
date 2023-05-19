-- Create the chat_log table
CREATE TABLE chat_log (
    uuid UUID PRIMARY KEY,
    user_uuid UUID,
    timestamp TIMESTAMP,
    message TEXT
);