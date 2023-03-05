# Step 1:
## Install Metrics Server - Read the Docs:
  - GitHub: [LINK](https://github.com/kubernetes-sigs/metrics-server#installation)

# Step 2: 
## Install Metrics Server:
  - Access MetricsServer directory

# Step 3:
## Run command to download metrics server file:
  - Download the file components.yaml
```bash
wget https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```
  
# Step 4:
  - Needs Change de Metrics Server file(components.yaml)
  - Add the following lines `Kind:Deployments` from Metrics Server file(components.yaml), in container context:

```bash
        command:
        - /metrics-server
        - --kubelet-insecure-tls
        - --kubelet-preferred-address-types=InternalIP
```

# Step 5:
## Run command to install metrics server:
  - Run and wait
```bash
./run.sh
```