alias k3s='KUBECONFIG=$HOME/.kube/token.yaml kubectl --context=default'
k3s apply -f components.yaml

echo "\n\n"
echo "-----------------------------------------------------------------------------------------"
echo "--> The response needs contains the pods with resources usages"
k3s top pods -A
echo "-----------------------------------------------------------------------------------------"