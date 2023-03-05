alias k3s='KUBECONFIG=$HOME/.kube/token.yaml kubectl --context=default'
k3s apply -f ingress-nginx.yaml