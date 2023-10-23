
class preprocesor:
    def __init__(self,name,age,etc):
        #Attributes
        self.name = name
        self.age = age
        self.etc = etc

        # method
        def remove_rows(self,df,columns):
            data = df.dropna(subset=[columns])
            return data

preprocesor(df,nume, columsn).remove:rows()