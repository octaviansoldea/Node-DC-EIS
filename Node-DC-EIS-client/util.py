# Copyright (c) 2016 Intel Corporation 
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import time
import os

def get_current_time():
  """
  #  Desc  : Function returns current date and time
  #  Input : None
  #  Output: Return current date and time in specific format for all log messages
  """
  currentTime=time.strftime("%d-%m-%Y %H:%M:%S")
  return currentTime

def record_start_time(start_MT):
  """
  # Desc  : Function to record start time
  # Input : None
  # Output: Returns start time of measuring time phase
  """
  with start_MT.get_lock():
    start_MT.value = time.time()
  

def record_end_time(end_MT):
  """
  # Desc  : Function to record end time
  # Input : None
  # Output: Returns end time of measuring time phase
  """
  with end_MT.get_lock():
    end_MT.value = time.time()
  

def printlog(log, log_lock, phase, start_MT, end_MT, MT_req,url_type,request_num,url,start,end,response_time,total_length):
  """
  # Desc  : Function to Generate per request details in a templog file
  #         checks all the requests in MT phase are within the start and end time 
  #         of measuring time phase
  # Input : log file to collect per request data
  #         phase of each request(ramp-up, ramp-down, measuring-time)
  #         request number, URL , start and end time of each request,
  #         response time of each request
  # Output: Returns per request details in a templog file
  """
  with phase.get_lock():
    phase_local = phase.value

  with start_MT.get_lock():
    start_MT_local = start_MT.value
  with end_MT.get_lock():
    end_MT_local = end_MT.value

  if phase_local ==1:
    if not ((start >= start_MT_local and end_MT_local == 0) or (end_MT.value > start_MT_local and end <= end_MT_local)):
      phase_local = 2
    else:
      with MT_req.get_lock():
        MT_req.value += 1
  options = {0: "RU", 1: "MT", 2: "RD", 3: "SD"}
  phase_local = options[phase_local]
  log_str = phase_local+","+str(request_num)+","+str(url)+","+str(start)+","+str(end)+","+str(response_time)+","+str(total_length)+","+str(url_type)
  log_lock.acquire()
  print >> log, log_str
  log.flush()
  log_lock.release()

def check_startfile(rundir):
  """
  # Desc  : Function to check if a file exists
  # Input : run directory
  # Output: Returns true if the file exists
  """
  while True:
    if(os.path.exists(os.path.join(rundir,"start.syncpt"))):
      break

def create_indicator_file(rundir,file_name,instance_id,string_towrite):
  """
  # Desc  : Function to create indicator files
  # Input : run directory, the file name to be created, instance ID, 
  #         string to be written in the new file created
  # Output: creates a new indicator file
  """
  print "[%s] Creating indicator file." % get_current_time()
  with open(os.path.join(rundir, '%s%s.syncpt' % (file_name, instance_id)),
            'w') as ind_file:
    if string_towrite:
        ind_file.write(string_towrite)


def calculate_throughput(log_dir,concurrency,cpuCount, start_MT, end_MT, MT_req):
  """
  # Desc  : Function to calucalte throughput for each run
  # Input : run directory, concurrency ,the number of processes 
  # Output: generates a summary throughput file 
  """

  with start_MT.get_lock():
    start_MT_local = start_MT.value
  with end_MT.get_lock():
    end_MT_local = end_MT.value
  with MT_req.get_lock():
    MT_req_local = MT_req.value


  throughput = MT_req_local/(end_MT_local-start_MT_local)
  throughput = round(throughput,2)
  try:
    fp_throughput = open(os.path.join(log_dir,"throughput_info.txt"), "w")
  except IOError as e:
    print("Error: %s File not found throughput_info.txt")
    return None
  print >> fp_throughput,"Concurrency is:"+str(concurrency)
  print >> fp_throughput,"Number of processess:"+str(cpuCount)
  print >> fp_throughput,"Measuring time window start time is:"+str(start_MT_local)
  print >> fp_throughput,"Measuring time end time is:"+str(end_MT_local)
  print >> fp_throughput,"Elapsed time is:"+str(end_MT_local-start_MT_local)
  print >> fp_throughput,"Total measuring time requests:"+str(MT_req_local)
  print >> fp_throughput,"Throughput is:"+str(throughput)
  fp_throughput.close()

  
