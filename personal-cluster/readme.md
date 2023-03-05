# Step 1:
## Remove all K3S data to the Servers
  - Access Ansible directory 

```bash
ansible-playbook -i hosts.yaml remove-k3s.yaml
```

# Step 2:
## Install K3S on the Servers
  - Access Ansible directory 
  
```bash
ansible-playbook -i hosts.yaml install-k3s.yaml
```
  
# Step 3 - Optional:
## Reboot the Servers
  - Access Ansible directory 

```bash
ansible-playbook -i hosts.yaml reboot.yaml
```

# Step 4:
## Configure MetalLB
  - Access MetalLB directory
```bash
  ./run.sh
```

# Step 5:
## Configure Ingress
  - Standard Ingress Class: `kubernetes.io/ingress.class: nginx-manager`
  - Access Ingress directory
  - Run and wait
```bash
  ./run.sh
```

# Step 6 - Optional:
# Deploy the Demo Application
  - Access Deploy directory
```bash
  ./run.sh
```

# Step 7:
## Configure Metrics Server
  - Access Metrics directory
