import os
from IPython.display import HTML, clear_output
from IPython.display import Javascript
from IPython.display import Image
from google.colab.output import eval_js
import sys
clear_output()

ipy = get_ipython()
ipy.magic("tensorflow_version 1.x")

import tensorflow as tf

if not tf.test.is_gpu_available():
  print ('Please use GPU to run the program.')
  sys.exit(0)
  


if not os.path.isfile('/tmp/done'):
  if not os.path.isdir('/content/drive/'):
    from google.colab import drive; drive.mount('/content/drive', force_remount=True) 
    
  clear_output()

  print ('Please wait for few minutes... ')
  get_ipython().system_raw('git clone https://github.com/ankanbhunia/deeplabs ; cp -r deeplabs/* /content; rm -r deeplabs; python install_.py; touch /tmp/done')


def show_port(port, height=400):
  display(Javascript("""
  (async ()=>{
    fm = document.createElement('iframe')
    fm.src = await google.colab.kernel.proxyPort(%s)
    fm.width = '95%%'
    fm.height = '%d'
    fm.frameBorder = 0
    document.body.append(fm)
  })();
  """ % (port, height) ))
clear_output()

print ("""


  .-.            ___               ___         ___      
 /    \         (   )             (   )       (   )     
 | .`. ;  .---.  | |   ___   .--.  | |   .---. | |.-.   
 | |(___)/ .-, \ | |  (   ) /    \ | |  / .-, \| /   \  
 | |_   (__) ; | | |  ' /  |  .-. ;| | (__) ; ||  .-. | 
(   __)   .'`  | | |,' /   |  | | || |   .'`  || |  | | 
 | |     / .'| | | .  '.   |  |/  || |  / .'| || |  | | 
 | |    | /  | | | | `. \  |  ' _.'| | | /  | || |  | | 
 | |    ; |  ; | | |   \ \ |  .'.-.| | ; |  ; || '  | | 
 | |    ' `-'  | | |    \ .'  `-' /| | ' `-'  |' `-' ;  
(___)   `.__.'_.(___ ) (___)`.__.'(___)`.__.'_. `.__.   
                                                        
                                                        

"""
)

print("Project URL: "+eval_js("google.colab.kernel.proxyPort(%d)"% (8000)))

print("""
                                                                                                                                                                                                 
                                                                                                                                           
  ______  ______  ______  ______  ______  ______  ______  ______  ______  ______  ______  ______  ______  ______  ______  ______  ______  ______  ______  ______  ______ 
 |______||______||______||______||______||______||______||______||______||______||______||______||______||______||______||______||______||______||______||______||______|
                                                                                                                                                                         
""")


get_ipython().getoutput("python3 app.py")
