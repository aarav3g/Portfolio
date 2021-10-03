from earsketch import * 

init() 

setTempo(110) 

bass1 = HIPHOP_BASSSUB_001 

brass = ENTREP_THEME_BRASS 

orch = ENTREP_THEME_ORCH 

drums = HIPHOP_DUSTYGROOVE_003 

drums2 = RD_UK_HOUSE_SOLODRUMPART_18 



  

MusList = [drums2, drums, orch, brass, bass1] 

  

reversedList = reverseList(MusList) 

  

for measure in range(1, 6): 

  index = measure - 1 

  track = measure 

  fitMedia(reversedList[index], track, measure, 9.47) 

  

def mus_function(start, end): 

  fitMedia(bass1, 5, start, end) 

   

  

mus_function(1, 5) 

  

setEffect(1, VOLUME, GAIN, -5) 

  

setEffect(3, REVERB, MIX, 0.1, 1.0, 0.5, 3.0) 

  

finish() 
