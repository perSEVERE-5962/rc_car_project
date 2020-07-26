# import any of the required libraries for the command

from threading import Thread

# create the class that extends the Thread class
# see https://thispointer.com/create-a-thread-using-class-in-python/ for a tutorial
# see https://www.programiz.com/python-programming/class for an additional tutorial
class CommandTemplate(Thread):
    "Put a description of your class here in quotes"

    # create the constructor to initialize the class
    # you can specify as many parameters as needed, with or without defaults
    # see https://www.programiz.com/python-programming/function-argument for a tutorial
    def __init__(self, value1=0, value2=0):
        # Call the Thread class's init function
        Thread.__init__(self)        
        self._running = True
        self.value1 = value1
        self.value2 = value2
    
    # Called when the command is initially scheduled.
    def initialize(self):
        # TODO: implement the logic to initialize the command
        print("initializing")

    # Called every time through the loop 
    def execute(self):
        # TODO: implement the logic to execute
        print("executing")

    # Called once the command ends or is interrupted
    def end(self):
        self._running = False
        print("ending")

    # Returns true when the command should end
    def isFinished(self):
        return self._running == False

    # Override the run() function of Thread class
    def run(self):
        while self.isFinished() == False:
            # TODO: add your command logic here

            self.execute()
            
'''
The following is an example of how to use this class from your main script

def main():
   # Create an object of Thread
   th = CommandTemplate()
   # start the thread
   th.start()
   # wait for thread to finish
   th.join()

if __name__ == '__main__':
   main()
'''