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