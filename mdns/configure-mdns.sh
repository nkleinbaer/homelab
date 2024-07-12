chmod +x /home/nick/homelab/mdns/publish-mdns-addresses.sh
cp /home/nick/homelab/mdns/publish-mdns.service /etc/systemd/system
chown root:root /etc/systemd/system/publish-mdns.service
systemctl enable publish-mdns
systemctl start publish-mdns.service
