# Liskov Substitution Principle

# Derived classes must be substitutable for their base classes.

# File class that a user can only be read and not write
class I_Readable_SQL_File:
    def Load_Text():
        print("read readable file")
        return "text 1,"


# File class that a user can only write and not read
class I_Writable_SQL_File:
    def Save_Text(self):
        print("sError")
        return


# An sqlfile implements both readable and writable files
# which means it can be both written and read
class SQLFile(I_Readable_SQL_File, I_Writable_SQL_File):
    def __init__(self):
        return
    # Read an sql file

    def Load_Text(self):
        print("read  sql file")
        return "text 1,"
    # Save the text to the sql file

    def Save_Text(self):
        print("save text to sql file")


# Read only sql file implements only readable file class
class Read_Only_Sql_File(I_Readable_SQL_File):
    def __init__(self):
        self.filepath = ""
        self.filetext = ""
    # Read text from the file

    def Load_Text(self):
        print("read file")
        return "text 1,"


# Sql file manager to save and read from multiple files.
class Sql_File_Manager:

    # Get all the text from a list of sql files
    def Get_Text_From_Files(self, sql_files):
        string = ""
        for i in range(len(sql_files)):
            string += sql_files[i].Load_Text()
        return string

    # Save text to a given list of sql files
    def Save_Text_To_Files(self, sql_files):
        for i in range(len(sql_files)):
            sql_files[i].Save_Text()
        return


if __name__ == '__main__':
    sql_f_m = Sql_File_Manager()

    sqf1 = SQLFile()
    sqf2 = SQLFile()
    rdf1 = Read_Only_Sql_File()
    rdf2 = Read_Only_Sql_File()

    files = []
    save_files = []
    files.append(sqf1)
    files.append(sqf2)
    files.append(rdf1)
    files.append(rdf2)

    save_files.append(sqf1)
    save_files.append(sqf2)

    sql_f_m.Get_Text_From_Files(files)
    sql_f_m.Save_Text_To_Files(save_files)
