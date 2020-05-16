from datetime import datetime

log_file ="example2.log"


def read_log(log):
    """
    open the logifle and print contents to the terminal
    """
    #   "r" = read
    with open(log, "r") as f:
        print(f.read())

def write_log(log, name):
    """
    Add new logfile entry with a datestamp
    """
    #   here we will set up a log time using the "datetime.now" function.
    #   "str" is string.. convert datetime.now to a str.
    log_time =str(datetime.now())
    with open(log, "a") as f:
        #   "a" = append
        #   any functionality that happens after the 'with' statement will apply
        #   to the (log, "a") log file; referenced as 'f'.
        f.writelines("Entry logged at: {} by {}\n".format(log_time, name))
        #   writelines is a method attached to 'f'.

#   entry  point for program.
if __name__ == '__main__':
    #   input is a reserved keyword in Python.
    name = input("what's your name?")

    #   add entry to log ifle.
    print("adding new log entry")
    #   create log file if one doesn't already exist and adds the name.
    write_log(log_file, name)
    print("")
    
    #   access starting log file
    print("log file contents")
    print("-----------------")
    read_log(log_file)

#   write log and read log were the two methods used in this script. 

#   "with" is a directive that defines a target file, its working state (append,
#   (read, write), and give us a way to interact with the object (log_time in
#   this case).
