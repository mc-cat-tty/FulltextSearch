-- Esperimenti
SELECT 'There are two cats in the room'::tsvector;  -- 'There' 'are' 'cats' 'in' 'room' 'the' 'two'
SELECT to_tsvector('english', 'There are two cats in the room');  -- 'cat':4 'room':7 'two':3
SELECT 'Cats & Rooms'::tsquery;  -- 'Cats' & 'Rooms'
SELECT to_tsquery('english', 'Cats | Rooms');  -- 'cat' | 'room'
SELECT 'There are two cats in the room'::tsvector @@ 'cat & room'::tsquery;  -- false
SELECT to_tsvector('english', 'There are two cats in the room') @@ to_tsquery('english', 'CAT & Room');  -- true
SELECT to_tsvector('english', 'There is a critical error') @@ to_tsquery('english', 'critical <-> error');  -- true
SELECT to_tsvector('english', 'There is a error which is not critical') @@ to_tsquery('english', 'error <4> critical');  -- true

-- Creazione tabelle
CREATE TABLE ricette(titolo varchar, autore varchar, corpo varchar);
INSERT INTO ricette VALUES ('La Pizza', 'Gennaro', 'Impastare e stirare, per poi cuocere nel forno a legna');
INSERT INTO ricette VALUES ('La Cotoletta', 'Leonardo', 'Impastare, Farcire, impanare, infine friggere');
SELECT titolo || ' ' || autore AS doc FROM ricette;
CREATE INDEX body_idx ON ricette USING gin(to_tsvector('italian', corpo));
SELECT titolo FROM ricette WHERE to_tsvector('italian', titolo || ' ' || corpo) @@ to_tsquery('italian', 'la & impastare');
SELECT titolo FROM ricette WHERE to_tsvector('italian', titolo || ' ' || corpo) @@ to_tsquery('italian', 'impanare <2> friggere');

ALTER TABLE ricette ADD COLUMN titolo_ts tsvector;
UPDATE ricette set titolo_ts = to_tsvector(titolo);
CREATE INDEX titolo_idx ON ricette USING gin(titolo_ts);