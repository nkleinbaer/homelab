cd /mnt/data
mkdir -p prometheus/data grafana/data && \
sudo chown -R 472:472 grafana/ && \
sudo chown -R 65534:65534 prometheus/
cd ~/homelab/monitoring
sudo chown -R 472:472 grafana/ && \
sudo chown -R 65534:65534 prometheus/
