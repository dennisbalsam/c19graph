--
-- PostgreSQL database dump
--

-- Dumped from database version 13.1
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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: contact; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.contact (
    pid1 integer,
    pid2 integer
);


ALTER TABLE public.contact OWNER TO root;

--
-- Name: people; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.people (
    pid integer NOT NULL,
    name character varying(80),
    age integer,
    infected boolean
);


ALTER TABLE public.people OWNER TO root;

--
-- Data for Name: contact; Type: TABLE DATA; Schema: public; Owner: root
--

COPY public.contact (pid1, pid2) FROM stdin;
1	2
2	3
3	4
4	5
5	6
6	7
7	8
8	9
9	10
10	1
11	12
12	13
13	14
14	15
15	16
16	11
17	18
17	19
17	20
21	22
21	23
23	24
21	25
10	21
\.


--
-- Data for Name: people; Type: TABLE DATA; Schema: public; Owner: root
--

-- 1-10 cycle 1, (2) and (8) are infected
-- 11-16 cycle 2, (13) is infected
-- 17-20 disjoint graph, no infected	
-- 21-25 subgraph, connected by one node to cycle 2
COPY public.people (pid, name, age, infected) FROM stdin;
1	Joe Blow	25	f
2	John Ron	32	t
3	Betty Spagetty	40	f
4	Kurtis Bennett	57	f
5	Ronaldo Rodriguez	77	f
6	Henry Finnegan	69	f
7	Rickie Fritz	12	f
8	Claire Nava	64	t
9	Fatima Evans	80	f
10	Marwah Hume	39	f
11	Dani Doyle	18	f
12	Reem Hendricks	25	f
13	Bobby Bullock	55	f
14	Joshua Stewart	47	f
15	Craig Frame	25	f
16	Nathanial Leech	32	f
17	Haidar Edwards	69	f
18	Ezra Bloom	80	f
19	Shawn Dalby	54	f
20	Ewen Ayers	27	f
21	Taya Espinoza	22	f
22	Eira Greenwood	36	f
23	Viktor Maxwell	20	f
24	Rida Peterson	19	f
25	Clarence Southern	44	f
\.


--
-- Name: people people_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.people
    ADD CONSTRAINT people_pkey PRIMARY KEY (pid);


--
-- Name: contact contact_pid1_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.contact
    ADD CONSTRAINT contact_pid1_fkey FOREIGN KEY (pid1) REFERENCES public.people(pid);


--
-- Name: contact contact_pid2_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.contact
    ADD CONSTRAINT contact_pid2_fkey FOREIGN KEY (pid2) REFERENCES public.people(pid);


--
-- PostgreSQL database dump complete
--

