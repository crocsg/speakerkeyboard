systemctl stop kspeaker
cp kspeaker.service /etc/systemd/system
systemctl enable kspeaker
systemctl start kspeaker
systemctl status kspeaker
