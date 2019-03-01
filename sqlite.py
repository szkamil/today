import sqlite3
# from class_definition import Blocked_request

try:
    conn = sqlite3.connect(':memory:')
    # conn = sqlite3.connect('blocked_req.db')
    # Create cursor
    c = conn.cursor()
    c.execute("""CREATE TABLE test(
                postId integer,
                id integer,
                name text,
                email text,
                body text
                )""")
    def insert_record(blck):
        # use context manager, no need to commit at the end
        with conn:
            c.execute("INSERT INTO blocked_id VALUES (?, ?, ?, ?)",
                      (blck.user_id, blck.id, blck.title, blck.completed))





    def get_recored_by_id(id):
        # select stmt no need to be commited
        c.execute("SELECT * FROM blocked_id where user_id=:user_id", {'user_id':id})
        return c.fetchall()
    def update_record(blck, completed):
            with conn:
                c.execute("""UPDATE blocked_id SET completed= :completed
                WHERE user_id=:user_id AND id=:id""",
                          {'user_id': blck.user_id, 'id': blck.id, 'completed': completed}
                          )


    def remove_record(blck):
        with conn:
            c.execute("DELETE from blocked_id WHERE user_id=:user_id",
                      {'user_id': blck.user_id})

    #
    blck_1 = Blocked_request(4, 5, 'class created', 'yes')
    blck_2 = Blocked_request(5, 5, 'class2 created', 'yes2')

    insert_record(blck_1)
    insert_record(blck_2)
    print(get_recored_by_id(4 ))
    # User ? ? ? + tuple to prevent sql injection
    # c.execute("INSERT INTO blocked_id VALUES (?, ?, ?, ?)", (blck_1.user_id, blck_1.id, blck_1.title, blck_1.completed))

    # second methond
    # c.execute("INSERT INTO blocked_id VALUES (:user_id, :id, :title, :completed)",
    #           {'user_id': blck_2.user_id, 'id': blck_2.id,
    #            'title': blck_2.title, 'completed': blck_2.completed})
        #
    # c.execute("""INSERT INTO blocked_id VALUES
    # (2, 3, "example 2", "third example")
    # """)
        # conn.commit()
    # comma requird to create a tuple
    # c.execute("SELECT * FROM blocked_id where user_id = ?", (1,))
    c.execute("SELECT * FROM blocked_id")
    # print(c.fetchall())

except:
    pass
finally:
    conn.close()