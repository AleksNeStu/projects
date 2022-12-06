#1
#start of the function
import cProfile; prof = cProfile.Profile(); prof.enable()

#function return
prof.disable(); prof.dump_stats('/tmp/results.profile')



#2
import cProfile
def sum(a, b):
    return a+b
if __name__ == '__main__':
    pr = cProfile.Profile()
    pr.enable()
    sum(2, 3)
    pr.disable()
    pr.print_stats()


#It’s possible to store the output of the result in a file instead of showing stdout
#pr.dump_stats("result.txt")
