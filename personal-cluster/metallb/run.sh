alias k3s='KUBECONFIG=/Users/nicolas.mmb/.kube/k3s_token.yaml kubectl --context=default'
k3s apply -f https://raw.githubusercontent.com/metallb/metallb/v0.12.1/manifests/namespace.yaml
k3s apply -f https://raw.githubusercontent.com/metallb/metallb/v0.12.1/manifests/metallb.yaml
k3s create secret generic -n metallb-system memberlist --from-literal=secretkey="$(openssl rand -base64 128)"
k3s apply -f config.yaml