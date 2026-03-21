def employee(**details):
    for k,v in details.item():
        print(k,":",v)
employee(name="kalyani",id=101,dept="IT")