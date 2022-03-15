class GenreSQL():
    def __init__(self,cursor):
        self.cursor = cursor

    def add_new_genre(self,value):
        query = f"""
        INSERT INTO genre(name)
        VALUES ('{value}');
        """    
        self.cursor.execute(query)
        print("New genre added succsessfully")

    def get_genre(self,id):
        query = f"""
        SELECT * FROM genre WHERE id={id};
        """
        self.cursor.execute(query)
        return self.cursor.fetchone()


    def get_all_genres(self):
        query = """
        SELECT * FROM genre;
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def delete_genre(self,id):
        query = f"""
        DELETE FROM genre WHERE id={id};
        """
        self.cursor.execute(query)
        print("Genre deleted succsessfully")


    def update(self,id,value):
        query= f"""
        UPDATE genre SET name={value} WHERE id={id};
        """
        self.cursor.execute(query)
        print("Genre updated succsessfully")           
