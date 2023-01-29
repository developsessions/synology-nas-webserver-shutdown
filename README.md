# Synology NAS DiskStation Webserver Shutdown

A simple python app which lets you shutdown your Synology DiskStation NAS via the Web Browser to save energy consumption.

## Usage

Do the following steps to install the package.<br>
You can also watch my YouTube video where I teach you how to install this package https://youtu.be/93Ly_U7mgkM

1. Install Python3 from the DiskStation package manager
2. Transfer the `webserver_shutdown.py` and `webserver_shutdown.conf` file from your PC via scp to your NAS<br>
   `scp webserver_shutdown* youruser@192.168.1.2:/tmp`
3. Login via SSH (e.g. [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)) on your Synology NAS
4. Move the uploaded files to its destination<br>
   `sudo mv /tmp/webserver_shutdown.py /usr/`<br>
   `sudo mv /tmp/webserver_shutdown.conf /etc/init/`
5. Reboot the DiskStation
   `sudo reboot`
6. Access the webpage via (replace the IP 192.168.1.2 with that IP of your DiskStation)<br>
   `http://192.168.1.2:8080`

   ![](img/synology_shutdown_screenshot.png)
