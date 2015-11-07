#imports
try:
    print "Importing Modules"
    import mymultiprocessing
    from mymultiprocessing import Process
    import sys
    print "Imports Finished"
except ValueError as e:
    print "error importing", e
    raw_input()

#list of all classes to kill
all_classes = []
all_classes_count = 0

def allclasses(name):
    global all_classes, all_classes_count
    all_classes.append(name)
    all_classes_count+=1

#main_window class
try:
    class main_window:
        def __init__(self):
            print "Hello! Welcome to Population."
            raw_input()
except:
    e = sys.exc_info()[0]
    print "whoops! Something went wrong."
    print e
    raw_input("Press Enter to exit ")


try:
    main_proc = Process(target=main_window())
    #main_proc.start()
    #main_proc.join()
    allclasses("main_proc")
except:
    e = sys.exc_info()[0]
    print "whoops! Something went wrong."
    print e
    raw_input("Press Enter to exit ")


#kill all classes(processes)
try:
    for i in all_classes:
        str((all_classes[i])).terminate()
except:
    e = sys.exc_info()[0]
    print "whoops! Something went wrong."
    print e
    raw_input("Press Enter to exit ")

raw_input()
