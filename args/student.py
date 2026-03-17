
def student_detail(*args:tuple):

    print(args)
    print(args[0],args[3])

student_detail("vipin",2345,5679,"vipin@gmail.com","cs")

def employee_detail(**kwargs:dict):

    print(kwargs)
    print(kwargs.get("name"))
employee_detail(name="hari",dept="hr",salary=256346)