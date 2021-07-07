--
-- PostgreSQL database dump
--

-- Dumped from database version 13.3 (Debian 13.3-1.pgdg100+1)
-- Dumped by pg_dump version 13.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: test; Type: DATABASE; Schema: -; Owner: test
--

\connect test

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: taskstatus; Type: TYPE; Schema: public; Owner: test
--

CREATE TYPE public.taskstatus AS ENUM (
    'todo',
    'in_progress',
    'done'
);


ALTER TYPE public.taskstatus OWNER TO test;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: task; Type: TABLE; Schema: public; Owner: test
--

CREATE TABLE public.task (
    name character varying NOT NULL,
    status public.taskstatus NOT NULL,
    start_datetime timestamp without time zone,
    end_datetime timestamp without time zone
);


ALTER TABLE public.task OWNER TO test;

--
-- Name: COLUMN task.name; Type: COMMENT; Schema: public; Owner: test
--

COMMENT ON COLUMN public.task.name IS 'Task name';


--
-- Name: COLUMN task.status; Type: COMMENT; Schema: public; Owner: test
--

COMMENT ON COLUMN public.task.status IS 'Task status';


--
-- Name: COLUMN task.start_datetime; Type: COMMENT; Schema: public; Owner: test
--

COMMENT ON COLUMN public.task.start_datetime IS 'Start date and time of this task';


--
-- Name: COLUMN task.end_datetime; Type: COMMENT; Schema: public; Owner: test
--

COMMENT ON COLUMN public.task.end_datetime IS 'End date and time of this task';


--
-- Data for Name: task; Type: TABLE DATA; Schema: public; Owner: test
--

COPY public.task (name, status, start_datetime, end_datetime) FROM stdin;
\.


--
-- Name: task task_pkey; Type: CONSTRAINT; Schema: public; Owner: test
--

ALTER TABLE ONLY public.task
    ADD CONSTRAINT task_pkey PRIMARY KEY (name);


--
-- Name: ix_task_name; Type: INDEX; Schema: public; Owner: test
--

CREATE INDEX ix_task_name ON public.task USING btree (name);


--
-- PostgreSQL database dump complete
--

