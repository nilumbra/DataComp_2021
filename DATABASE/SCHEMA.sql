CREATE TABLE questions(
    id INTEGER PRIMARY KEY NOT NULL ,
    user_id INTEGER NOT NULL,
    category_id SMALLINT NOT NULL,
    content TEXT, 
    created TIMESTAMP
);

CREATE TABLE answers(
    id INTEGER PRIMARY KEY NOT NULL, 
    user_id INTEGER NOT NULL,
    question_id INTEGER NOT NULL,
    parent_answer_id INTEGER NOT NULL, 
    content TEXT NOT NULL,
    is_best BOOLEAN NOT NULL,
    created TIMESTAMP
);

CREATE TABLE users(
    id INTEGER PRIMARY KEY,
    generation_id SMALLINT NOT NULL,
    prefecture_id SMALLINT NOT NULL,
    created TIMESTAMP
);

 CREATE TABLE children(
        id integer PRIMARY KEY,
        user_id INTEGER,
        birthday DATE, 
        sex SMALLINT
);

CREATE TABLE IF NOT EXISTS public.search
(
    user_id integer,
    word text COLLATE pg_catalog."default",
    created timestamp without time zone
);

--------------- INDEX ----------------
-- INDEX FOR TABLE::answers 
DROP INDEX public.answers_id_index;
CREATE UNIQUE INDEX answers_id_index
    ON public.answers USING btree
    (id ASC NULLS LAST)
;

DROP INDEX public.answers_question_id_index;
CREATE INDEX answers_question_id_index
    ON public.answers USING btree
    (question_id ASC NULLS LAST)
    TABLESPACE pg_default;

DROP INDEX public.answers_user_id;
CREATE INDEX answers_user_id
    ON public.answers USING btree
    (user_id ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE INDEX answers_created_index
    ON public.answers USING btree
    (created ASC NULLS LAST)
;


-- INDEX FOR TABLE::questions 
CREATE INDEX questions_created_index
    ON public.questions USING btree
    (created ASC NULLS LAST)
;


CREATE INDEX questions_user_id_index
    ON public.questions USING btree
    (user_id ASC NULLS LAST)
    TABLESPACE pg_default;


-- INDEX FOR TABLE::search 
DROP INDEX public.created_index_date;
CREATE INDEX created_index_date
    ON public.search USING btree
    (created ASC NULLS LAST)
    TABLESPACE pg_default;


DROP INDEX public.search_user_id_index;
CREATE INDEX search_user_id_index
    ON public.search USING btree
    (user_id ASC NULLS LAST)
    TABLESPACE pg_default;