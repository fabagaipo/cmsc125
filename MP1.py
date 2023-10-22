# imports
from os import system
from time import sleep
from random import randint, randrange
from math import modf
from typing import Optional, List
from termcolor import cprint

MAX_VAL: int = 30 # max value for resources and user
MAX_CHAR_WIDTH: int = 30
DEBUG: bool = False
DEBUG_DATA: bool = False
DEBUG_DISABLE_LOOP: bool = False

class Process:
  def __init__(self, user: int, resource: int, currTime: Optional[int] = None):
    self._user: int = user
    self._resource: int = resource
    self._currTime: int = randint(1, MAX_VAL) if currTime is None else currTime
    self._initTime: int = self._currTime
    self._startTime: int = 0
    self._endTime: int = self._currTime
    self._isActive: bool = False
    self._isDone: bool = False

  def user(self):
    return self._user

  def resource(self):
    return self._resource

  def currTime(self):
    return self._currTime

  def startTime(self):
    return self._startTime

  def endTime(self):
    return self._endTime

  def isActive(self):
    return self._isActive

  def isDone(self):
    return self._isDone

  def addTime(self, time: int):
    self._startTime += time
    self._endTime += time

  def tick(self):
    if self._isDone:
      return
    if not self._isActive:
      if self._startTime == 0:
        self._isActive = True
      self._startTime -= 1
    else:
      if self._currTime == 0:
        self._isActive = False
        self._isDone = True
      self._currTime -= 1

  def printActive(self):
    if self._currTime == 0:
      return "DONE"
    elif self._isActive:
      return "ACTIVE"
    else:
      return ""

  def printStartTime(self):
    return ("Start Time: " + str(self._startTime + 1) if not self._isActive else "")

  def printCurrTime(self):
    dec: float
    integer: float
    (dec, integer) = modf((self._initTime - self._currTime) / self._initTime * MAX_CHAR_WIDTH)

    return ("█" * int(integer) + "░" * (MAX_CHAR_WIDTH - int(integer)) +
                "\n" + str(self._initTime - self._currTime) + "/" +
                str(self._initTime) +
                "\n" if self._isActive else "░" * MAX_CHAR_WIDTH + "\n")

  def __str__(self):
    return (self.printActive() + "\n[ process " +
                str(self._resource) + ":" + str(self._user) + " ]" +
                "\nUser: " + str(self._user) + "\n\n" +
                self.printCurrTime() + self.printStartTime() + "\n")

Resource = List[Process]
Processes = List[Resource]

class OperatingSystem:
  def __init__(self):
    self._users = self.delDuplicates([randint(1, MAX_VAL) for i in range(0, randint(1, MAX_VAL))])
    self._resources = self.delDuplicates([randint(1, MAX_VAL) for i in range(0, randint(1, MAX_VAL))])
    self._usersCount: int = len(self._users)
    self._resourcesCount: int = len(self._resources)
    self._users.sort()
    self._resources.sort()
    self._processes: Processes = [[None for i in range(self._users[-1] + 1)] for i in range(self._resources[-1] + 1)]

    if DEBUG_DATA:
      self.createDebugProcesses()
    else:
      self.createProcesses()
      self.cleanProcesses()
    self.calculateETA()

  def createDebugProcesses(self):
    self._usersCount = 3
    self._resourcesCount = 1
    self._processes = [ [None, Process(1, 1, 1), Process(1, 2, 1), Process(1, 3, 1)], ]

  def createProcesses(self):
    for resource in self._resources:
      maxProcesses: int = randint(0, self._usersCount)
      users = self._users.copy()

      if DEBUG:
        print("[ createProcesses ] users: " + str(self._users))
        print("[ createProcesses ] resources: " + str(self._resources))
        print("[ createProcesses ] processes: " + str(self._processes))
        print("[ createProcesses ] maxProcesses: " + str(maxProcesses))
        print("[ createProcesses ] users: " + str(users))

      for j in range(maxProcesses):
        user: int = users[randrange(0, len(users))]
        self._processes[resource][user] = Process(user, resource)

        users.remove(user)

    if DEBUG:
      print("[ createProcesses ] processes: " + str(self._processes))

  def cleanProcesses(self):
    for index, resource in enumerate(self._processes):
      if index not in self._resources:
        if DEBUG:
          print("[ cleanProcesses ] index: " + str(index))
        self._processes[index] = None

    if DEBUG:
      print("[ cleanProcesses ] processes: " + str(self._processes))

  def calculateETA(self):
    if DEBUG:
      print("[ calculateETA ] initial processes: \n")
      self.printProcesses(self._processes)

    for user in self._users:
      userProcesses: List[Process] = []
      for resource in self._processes:
        if resource is None:
          continue

        if resource[user] is not None:
          self.calculateTTSResource(resource, user)
          userProcesses.append(resource[user])
      self.checkConcurrency(userProcesses)

  def calculateTTSResource(self, resource: Resource, user: int):
    if DEBUG:
      print("[ calculateTTSResource ] user: " + str(user))
      print("[ calculateTTSResource ] resource: " + str(resource[user].resource()))

    for i in range(user - 1, 0, -1):
      process = resource[i]

      if DEBUG:
        print(process)

      if process is None:
        continue

      else:
        if DEBUG:
          print("[ calculateTTSResource ] process.endTime(): " + str(process.endTime()))
          print("[ calculateTTSResource ] resource[userIndex].startTime(): " + str(resource[user].startTIme()))
        resource[user].addTime(process.endTime() - resource[user].startTime())
        break

    if DEBUG:
      print("[ calculateTTSResource ] after calculate:\n")
      self.printProcesses(self._processes)

  def checkConcurrency(self, processes: List[Process]):
    processes.sort(key=lambda x: x.startTime())
    if DEBUG:
      print("[ checkConcurrency ] init")
      print("[ checkConcurrency ] userProcess: \n")
      for process in processes:
        if process is not None:
          print(process)

    for outerIndex in range(len(processes)):
      outerProcess = processes[outerIndex]
      for innerIndex in range(outerIndex + 1, len(processes)):
        innerProcess = processes[innerIndex]
        if DEBUG:
          print("[ checkConcurrency ] outerProcess: \n")
          print(outerProcess)
          print("[ checkConcurrency ] innerProcess: \n")
          print(innerProcess)
        if(outerProcess.endTime() > innerProcess.startTime() and innerProcess.endTime() > outerProcess.startTime()):
          if DEBUG:
            print("[ checkConcurrency ] if: " + str(outerProcess.endTime() > innerProcess.startTime() and innerProcess.endTime() > outerProcess.startTime()))

          innerProcess.addTime(outerProcess.endTime() - innerProcess.startTime())

  def delDuplicates(self, items):
    return list(dict.fromkeys(items))

  def run(self):
    seconds: int = -1
    newProcesses: Processes = [[process for process in resource if process is not None] if resource is not None else None for resource in self._processes]
    while True:
      if not DEBUG:
        system('cls')

      cprint("Windows Home CMSC 125\n", attrs=["bold"])
      print("Users: ", end="")
      cprint(self._users, attrs=["bold"])
      print("Resources: ", end="")
      cprint(self._resources, attrs=["bold"])
      cprint("\n======== ", "white", end="")
      print("TIME: " + str(seconds) + "s", end="")
      cprint(" ========\n", "white")
      self.printProcesses(newProcesses)

      for resources in newProcesses:
        if resources is None:
          continue
        for process in resources:
          if process is not None:
            process.tick()
      newProcesses[:] = [[process for process in resource if process is None or not process.isDone()] if resource is not None else None for resource in newProcesses]

      shouldEnd: bool = True
      for resources in newProcesses:
        if resources is None:
          continue
        if len(resources) > 0:
          if DEBUG:
            print("[ run ] len(resources)" + str(len(resources) > 0))
          shouldEnd = False

      if shouldEnd:
        break

      seconds += 1

      if not DEBUG:
        sleep(1)

  def printProcesses(self, processes: List[Process]):
    for index, resource in enumerate(processes, 0):
      if resource is None:
        continue

      cprint("-" * MAX_CHAR_WIDTH + "\n", "yellow")

      if index < 10:
        cprint("-------| Resource " + str(index) + " |-------\n", "blue")
      else:
        cprint("-------| Resource " + str(index) + " |-------\n", "blue")

      if len(resource) > 0:
        for p in resource:
          if p is not None:
            if p.currTime() == 0:
              cprint(p, "green")
            elif p.isActive():
              print(p)
            else:
              cprint(p, attrs=["dark"])
      else:
        cprint("\n No Processes in Waiting \n", "red")
    cprint("\n" + "-" * MAX_CHAR_WIDTH, "yellow")

  def processes(self):
    return self._processes

  def __str__(self):
    return("Users: " + str(self._usersCount) + "\nResources: " + str(self._resourcesCount))

def main():
  if DEBUG:
    print("[ main ] init")
  os: OperatingSystem = OperatingSystem()
  if DEBUG:
    print("[ main ] after calculateETA()")

  if not DEBUG_DISABLE_LOOP:
    os.run()

main()
