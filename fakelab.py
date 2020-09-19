import os
from IPython.display import HTML, clear_output
from IPython.display import Javascript
from IPython.display import Image
from google.colab.output import eval_js
import sys
clear_output()
import tensorflow as tf

if len(tf.config.list_physical_devices('GPU'))==0:
  print ('Please use GPU to run the program.')
  sys.exit(0)
  
get_ipython().system_raw("curl https://raw.githubusercontent.com/ankanbhunia/DeepFaceLab/master/GIF.gif > /tmp/GIF.gif") 
  


if not os.path.isfile('/tmp/done'):
  if not os.path.isdir('/content/drive/'):
    from google.colab import drive; drive.mount('/content/drive', force_remount=True) 
   
  Image(open("/tmp/GIF.gif",'rb').read())
  print ('Please wait for few minutes... ')
  get_ipython().system_raw('pip uninstall -y tensorflow; pip install tensorflow-gpu==1.13.2; git clone https://github.com/ankanbhunia/deeplabs ; cp -r deeplabs/* /content; rm -r deeplabs; python install_.py; touch /tmp/done')


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
Image(open("/tmp/GIF.gif",'rb').read())
print("Project URL: "+eval_js("google.colab.kernel.proxyPort(%d)"% (8000)))

get_ipython().system_raw('python3 app.py')
