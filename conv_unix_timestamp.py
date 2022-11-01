from datetime import datetime 

def conv_epoch(mod_time):
  ### converting milliseconds by substracting 1000
  epoch_timestamp = mod_time/1000
  lst_updtd_time = datetime.fromtimestamp(epoch_timestamp).strftime('%m-%d-%y')
  return lst_updtd_time
  
if __name__ == "__main__":
conv_epoch(unix_timestamp)
