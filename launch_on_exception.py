from ipdb import launch_ipdb_on_exception
x = 40
with launch_ipdb_on_exception():
    while 1:
        x -= 1
        print(40/x)
