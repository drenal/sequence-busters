# This is a quick and not foolproof tutorial to create a Python Machine Learning environment
- First of you should look it Python is installed in your system. The easieast ways to do it are 
```
which python
```
or
```
python --version
```
- If Python is not installed AND YOU HAVE ROOT PRIVILEGE you can do 
```
sudo apt-get install python
```
- If you don't have root privilege then you can install python from the source for your user. This is complicated and it requires many steps.

- Now it's necessary to check if we have pip installed in our system. We can also do
```
which pip
```
or 
```
pip --version
```
- If you don't have it installed AND YOU HAVE ROOT PRIVILEGE you can do
```
sudo apt install python3-pip
```
- If you want to install it for your user only you can do
```
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py --user
```
- Now there is necessary to install pyenv to create and administrate our virtual environment
```
curl https://pyenv.run | bash
```
Remember that after doing this installation we should add pyenv to the path. For doing that you should add the following lines to YOUR PATH. The path file is usually located in `~/.bashrc`.
```
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
After that we should restart the shell
```
exec "$SHELL"
```
Then you can install your favorite python version. You cna check a list of all the possibilities by doing
```
pyenv install --list
```
For instance 
```
pyenv install 3.8-dev
```
Then you can create your python environment with the following syntaxis
```
pyenv virtualenv <python_version> <environment_name>
```
for example
```
pyenv virtualenv 3.8-dev Bio_hack_2021
```
- Now we can access our new python virtual environment by using the command
```
pyenv local Bio_hack_2021
```
Now your python environment should be active, now if you do 
```
pip list
```
you will realize there is no many modules installed so we should install them.
```
pip install pandas scipy numpy plotly seaborn tensorflow sklearn torch
```
- This should be enough to work basic scripts. If we want to use an Nvidia GPU, you should follow the instructions to install CUDA 11. After CUDA 11 is installed you can run the following script to check it's working properly
```
nvidia-smi
```
Then you ca install tensorflow with GPU support using the following lines
```
pip install tensorflow-gpu
```
After this you can check it's working properly with tensorflow with the following script
```
import tensorflow as tf
if tf.test.gpu_device_name():
    print('Default GPU Device: {}'.format(tf.test.gpu_device_name()))
else:
    print("Please install GPU version of TF")
```
The output should be 
```
Default GPU Device: /device:GPU:0
```
