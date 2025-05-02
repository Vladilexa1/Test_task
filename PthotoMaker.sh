echo 'gpu mem=128' | sudo tee -a /boot/firmware/config.txt
echo 'dtoverlay=imx219' | sudo tee -a /boot/firmware/config.txt
sudo apt install python3-opencv -y
sudo apt install python3-picamera2 -y
git clone https://github.com/Vladilexa1/Test_task.git
mkdir ./Test_task/img