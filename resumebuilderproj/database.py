import sqlite3

def connect():
    return sqlite3.connect("data.db")

def create_tables(conn):
    with conn:
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS role (role_id integer PRIMARY KEY, role_desc text UNIQUE);")
        c.execute("CREATE TABLE IF NOT EXISTS resume (resume_id integer PRIMARY KEY, user_id text NOT NULL, resume_type_id integer, role_id integer, FOREIGN KEY(role_id) REFERENCES role (role_id));")
        c.execute("CREATE TABLE IF NOT EXISTS resume_output (resume_id integer, output_id integer, output_desc text, FOREIGN KEY (resume_id) REFERENCES resume (resume_id));")
        c.execute("CREATE TABLE IF NOT EXISTS resume_asset (resume_id integer, asset_id integer, asset_desc text,  FOREIGN KEY (resume_id) REFERENCES resume (resume_id));")
        c.execute("CREATE TABLE IF NOT EXISTS resume_skill (resume_id integer, user_id text, skill_id integer,skill_type_id text, skill_desc text, skill_competency_id integer, FOREIGN KEY (resume_id) REFERENCES resume (resume_id));")
        c.execute("CREATE TABLE IF NOT EXISTS resume_summary (resume_id integer, user_id text, summary_id integer, summary_desc text, FOREIGN KEY (resume_id) REFERENCES resume (resume_id));")
        c.execute("CREATE TABLE IF NOT EXISTS resume_qualification (resume_id integer, user_id text, qualification_id integer, qualification_desc text, FOREIGN KEY (resume_id) REFERENCES resume (resume_id));")
        c.execute("CREATE TABLE IF NOT EXISTS resume_project (resume_id integer, user_id text, project_id integer, project_desc text, project_role_desc text, FOREIGN KEY (resume_id) REFERENCES resume (resume_id));")
        c.execute("CREATE TABLE IF NOT EXISTS resume_proj_resp (resume_id integer, user_id text, project_id integer, proj_resp_id text, proj_resp_desc text, FOREIGN KEY (resume_id) REFERENCES resume (resume_id));")
        c.execute("CREATE TABLE IF NOT EXISTS resume_proj_prob_solved (resume_id integer, user_id text, project_id integer, proj_prob_solved_id integer, proj_prob_solved_desc text, FOREIGN KEY (resume_id) REFERENCES resume (resume_id));")
        c.execute("CREATE TABLE IF NOT EXISTS resume_proj_techtool (resume_id integer, user_id text, project_id integer, techtool_id integer, techtool_desc text, FOREIGN KEY (resume_id) REFERENCES resume (resume_id));")
        c.execute("CREATE TABLE IF NOT EXISTS resume_int_hobby (resume_id integer, user_id text, int_hobby_id integer, int_hobby_desc text, FOREIGN KEY (resume_id) REFERENCES resume (resume_id));")
        
def insert_role(conn, role_desc):
    with conn:
        conn.execute("INSERT INTO role (role_desc) VALUES (?);", (role_desc,))
                     
def get_role_by_role_desc(conn, role_desc):
    with conn:
        c = conn.cursor()
        c.execute("SELECT * FROM role WHERE role_desc=:role_desc;", {'role_desc': role_desc})
        return c.fetchall()

def get_role_by_id(conn, id):
    with conn:
        c = conn.cursor()
        c.execute("SELECT * FROM role WHERE role_id=:id;",{'id':id})
        return c.fetchone()
   
def get_role_list(conn):
    with conn:
        c = conn.cursor()
        c.execute("SELECT role_desc FROM role GROUP BY role_desc")
        return c.fetchall()

def update_role(conn, id, role_desc):
    with conn:
        c = conn.cursor()
        c.execute("UPDATE role SET role_desc=? where role_id=?;", (role_desc, id))
        return c.execute("SELECT * from role where role_id=?;",(id,)).fetchone()
        
def remove_role_id(conn,id):
    with conn:
        conn.execute("DELETE from role WHERE id = :id;",{'id' : id})
        
